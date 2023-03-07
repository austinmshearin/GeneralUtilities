"""
Tools for interfacing with the AWS Secrets Manager
"""
# Standard Imports
import json
import boto3


def collect_secret(secret_name: str, region_name: str = "us-west-2") -> dict:
    """
    Collects a secret from AWS secrets manager

    Parameters
    ----------
    secret_name: str
        The full secret name
    region_name: str = "us-west-2"
        The AWS region where the secret is stored

    Returns
    -------
    dict
        The contents of the stored secret
    """
    aws_session = boto3.session.Session()
    secrets_client = aws_session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_response = secrets_client.get_secret_value(
        SecretId=secret_name
    )
    return json.loads(get_secret_response['SecretString'])
