"""
Package for communicating with AWS s3
"""
# Standard Imports
import subprocess

def sync(source: str, destination: str):
    """
    Calls the AWS CLI aws s3 sync command through subprocess

    Parameters
    ----------
    source, destination: str
        Filepath on local system or s3 bucket object
        Either source or destination must be an s3 object

    Notes
    -----
    Local directories can be full or relative filepaths
        "C:/Users/User/Documents/FolderToUpload"
        "Documents/FolderToUpload"
    s3 must be a full path and folders can be used with a backslash
        "s3://bucket"
        "s3://bucket/folder"
    """
    sync_stmt = "aws s3 sync \"{0}\" \"{1}\" --quiet"
    subprocess.run(
        sync_stmt.format(source, destination),
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

def move(source: str, destination: str):
    """
    Calls the AWS CLI aws s3 mv command through subprocess

    Parameters
    ----------
    source, destination: str
        Filepath on local system or s3 bucket object
        Either source or destination must be an s3 object

    Notes
    -----
    Local directories can be full or relative filepaths
        "C:/Users/User/Documents/FolderToUpload"
        "Documents/FolderToUpload"
    s3 must be a full path and folders can be used with a backslash
        "s3://bucket"
        "s3://bucket/folder"
    """
    mv_stmt = "aws s3 mv \"{0}\" \"{1}\" --quiet --recursive"
    subprocess.run(
        mv_stmt.format(source, destination),
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
