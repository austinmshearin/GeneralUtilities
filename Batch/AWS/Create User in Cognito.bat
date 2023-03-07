set /p email="Email: "
set /p password="Password: "
set /p user_pool_id="Cognito user pool ID: "
aws cognito-idp admin-create-user --user-pool-id %user_pool_id% --username %email% --message-action SUPPRESS --user-attributes Name=email,Value=%email% Name=email_verified,Value=True
aws cognito-idp admin-set-user-password --user-pool-id %user_pool_id% --username %email% --password %password% --permanent