import boto3

# Create a low-level service client by the name of 'ec2'
ec2 = boto3.client('ec2')

# Start the instance
response = ec2.start_instances(
  InstanceIds=[
      'i-0deebeac01cf98d54', # replace with your instance ID
  ]
)

# Print the response
print(response)
