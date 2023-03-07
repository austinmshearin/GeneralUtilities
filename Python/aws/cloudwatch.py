"""
Package for communicating with AWS CloudWatch
"""

# Standard Imports
import boto3


def log_process_success(namespace: str, process: str, success: bool):
    """
    Record a custom metric in AWS CloudWatch for monitoring successful completion of processes

    Parameters
    ----------
    namespace: str
        The container for CloudWatch metrics
    process: str
        Name of the process being logged
    success: bool
        Whether the process completed successfully or not

    Notes
    -----
    The metric is logged by Failures so a count can be performed to determine the number of failures
        in CloudWatch over a time period
    """
    # Create cloudwatch connection
    cloudwatch = boto3.client('cloudwatch', region_name="us-east-2")

    # Convert success to failure count
    if success is True:
        failure = 0
    elif success is False:
        failure = 1
    else:
        raise Exception("Unexpected value for success: {}".format(success))

    # Insert the metric into CloudWatch    
    _ = cloudwatch.put_metric_data(
        Namespace = namespace,
        MetricData = [
            {
                'MetricName': "Failure",
                'Dimensions': [
                    {
                        'Name': "Process",
                        'Value': process
                    },
                ],
                'Value': failure,
                'Unit': "Count"
            },
        ]
    )
