import boto3

# Create an SNS client
client = boto3.client("sns")

# Send your sms message.
client.publish(
    PhoneNumber="+9728549342",
    Message="Hello World!"
)