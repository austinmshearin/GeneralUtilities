"""
Package for communicating with AWS Cognito user management
"""
# Standard Imports
import boto3
import hashlib
import hmac
import base64


class Cognito_Client:
    """
    Client for communicating with AWS Cognito user management
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initializes the Cognito client

        Parameters
        ----------
        client_id: str
            The ID of the app client used to communicate with the Cognito user pool
        client_secret: str
            The secret key for the app client to authenticate the communication
        """
        self.client = boto3.client('cognito-idp', region_name='us-west-2')
        self.client_id = client_id
        self.client_secret = client_secret

    def gen_secret_hash(self, email: str) -> str:
        """
        Generate the secret hash key used for authentication

        Parameters
        ----------
        email: str
            Email of the user

        Returns
        -------
        str
            Secret hash string used to authenticate Cognito connections

        Notes
        -----
        https://stackoverflow.com/questions/37438879/unable-to-verify-secret-hash-for-client-in-amazon-cognito-userpools
        """
        key = bytes(self.client_secret, 'latin-1')
        msg = bytes(email + self.client_id, 'latin-1')
        new_digest = hmac.new(key, msg, hashlib.sha256).digest()
        return base64.b64encode(new_digest).decode()

    def authenticate_user(self, email: str, password: str) -> dict:
        """
        Authenticates a user using email and password combination

        Parameters
        ----------
        email: str
            Email of the user
        password: str
            Users password

        Returns
        -------
        dict
            Authentication results
            {
                "Message": str,
                "Error": str (optional, uncaptured errors)
            }
        """
        try:
            # Attempt to authenticate the user with Cognito
            authentication = self.client.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": email,
                    "PASSWORD": password,
                    "SECRET_HASH": self.gen_secret_hash(email)
                },
                ClientId=self.client_id
            )
            # Successful authentication, but new password is required
            if "ChallengeName" in authentication:
                if authentication["ChallengeName"] == "NEW_PASSWORD_REQUIRED":
                    return {"Message": "New Password Required"}
            # Successful authentication
            else:
                return {"Message": "Successful"}
        # Invalid username and password combination
        except self.client.exceptions.NotAuthorizedException:
            return {"Message": "Not Authorized"}
        # Too many sign in attempts
        except self.client.exceptions.TooManyRequestsException:
            return {"Message": "Too Many Requests"}
        # User has not confirmed the account
        except self.client.exceptions.UserNotConfirmedException:
            return {"Message": "User Not Confirmed"}
        # Forced password reset
        except self.client.exceptions.PasswordResetRequiredException:
            return {"Message": "Password Reset Required"}
        # Any non captured exceptions will throw an error
        except Exception as e:
            return {"Message": "Unexpected Error", "Error": e}

    def sign_up(self, name: str, email: str, password: str) -> dict:
        """
        Initializes the sign up routine

        Parameters
        ----------
        name: str
            The users name
        email: str
            The users email
        password: str
            The users password

        Returns
        -------
        dict
            sign up results
            {
                "Message": str,
                "Error": str (optional, uncaptured errors)
            }

        Notes
        -----
        User must verify the account by clicking the link sent to the users email before sign up is complete
        """
        try:
            # Attempt to sign up the user with Cognito
            self.client.sign_up(
                ClientId=self.client_id,
                SecretHash=self.gen_secret_hash(email),
                Username=email,
                Password=password,
                UserAttributes=[
                    {
                        "Name": "name",
                        "Value": name
                    }
                ]
            )
            # Successful sign up
            return {"Message": "Successful"}
        # Email is already associated with an account
        except self.client.exceptions.UsernameExistsException:
            return {"Message": "Username Exists"}
        # Cognito encounters an invalid password
        except self.client.exceptions.InvalidPasswordException:
            return {"Message": "Invalid Password"}
        # Too many requests have been made
        except self.client.exceptions.TooManyRequestsException:
            return {"Message": "Too Many Requests"}
        # Any non captured exceptions will throw an error
        except Exception as e:
            return {"Message": "Unexpected Error", "Error": e}

    def resend_confirmation(self, email: str) -> dict:
        """
        Sends another confirmation email to the users email to verify the account

        Parameters
        ----------
        email: str
            The users email

        Returns
        -------
        dict
            resend confirmation results
            {
                "Message": str,
                "Error": str (optional, uncaptured errors)
            }
        """
        try:
            # Attempt to resend the confirmation code to the users email
            self.client.resend_confirmation_code(
                ClientId=self.client_id,
                SecretHash=self.gen_secret_hash(email),
                Username=email,
            )
            # Successful confirmation code sent
            return {"Message": "Succcessful"}
        # Too many requests have been made
        except self.client.exceptions.TooManyRequestsException:
            return {"Message": "Too Many Requests"}
        # Too many requests have been made
        except self.client.exceptions.LimitExceededException:
            return {"Message": "Too Many Requests"}
        # Email not associated to an account, should not occur
        except self.client.exceptions.UserNotFoundException:
            return {"Message": "User Not Found"}
        # Any non captured exceptions will throw an error
        except Exception as e:
            return {"Message": "Unexpected Error", "Error": e}

    def forgot_password(self, email: str) -> dict:
        """
        Initiates the forgot password routine

        Parameters
        ----------
        email: str
            The users email

        Returns
        -------
        dict
            forgot password results
            {
                "Message": str,
                "Error": str (optional, uncaptured errors)
            }

        Notes
        -----
        Cognito will send an email with a confirmation code to the users email  
        The confirmation code is needed for the user to set a new password  
        """
        try:
            # Attempt to initialize the forgot password routine
            self.client.forgot_password(
                ClientId=self.client_id,
                SecretHash=self.gen_secret_hash(email),
                Username=email
            )
            # Successfully started the forgot password routine
            return {"Message": "Successful"}
        # Too many requests have been made
        except self.client.exceptions.TooManyRequestsException:
            return {"Message": "Too Many Requests"}
        # Too many requests have been made
        except self.client.exceptions.LimitExceededException:
            return {"Message": "Too Many Requests"}
        # Any non captured exceptions will throw an error
        except Exception as e:
            return {"Message": "Unexpected Error", "Error": e}

    def confirm_forgot_password(self, email: str, confirmation_code: str, new_password: str) -> dict:
        """
        Confirm the forgot password routine and set a new password

        Parameters
        ----------
        email: str
            The users email
        confirmation_code: str
            The confirmation code sent to the users email when the forgot password routine was initiated
        new_password: str
            A new password for the users account

        Returns
        -------
        dict
            confirm forgot password results
            {
                "Message": str,
                "Error": str (optional, uncaptured errors)
            }
        """
        try:
            # Attempt to set new password with email confirmation code
            self.client.confirm_forgot_password(
                ClientId=self.client_id,
                SecretHash=self.gen_secret_hash(email),
                Username=email,
                ConfirmationCode=confirmation_code,
                Password=new_password
            )
            # Successfully changed password
            return {"Message": "Successful"}
        # Email does not exist or code does not match
        except self.client.exceptions.CodeMismatchException:
            return {"Message": "Code Mismatch"}
        # Provided recovery code has expired
        except self.client.exceptions.ExpiredCodeException:
            return {"Message": "Expired Code"}
        # Cognito encounters an invalid password
        except self.client.exceptions.InvalidPasswordException:
            return {"Message": "Invalid Password"}
        # User exceeds the limit for a requested AWS resource
        except self.client.exceptions.LimitExceededException:
            return {"Message": "Too Many Requests"}
        # User exceeds the limit for a requested AWS resource
        except self.client.exceptions.TooManyRequestsException:
            return {"Message": "Too Many Requests"}
        # Any non captured exceptions will throw an error
        except Exception as e:
            return {"Message": "Unexpected Error", "Error": e}
