import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'URL'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'All'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

body = response['Messages'][0]['MessageAttributes']
receipt_handle = response['Messages'][0]['ReceiptHandle']

#Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)