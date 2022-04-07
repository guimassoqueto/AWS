import boto3

# Create SQS client
sqs = boto3.client('sqs')

#Create a SQS in AWS and paste the link here
queue_url = 'URL'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Name': {
            'DataType': 'String',
            'StringValue': 'Gui'
        },
        'LastName': {
            'DataType': 'String',
            'StringValue': 'Mass'
        },
        'Age': {
            'DataType': 'Number',
            'StringValue': '30'
        }
    },
    MessageBody=(
        'GuiMass.'
    )
)

print(response['MessageId'])