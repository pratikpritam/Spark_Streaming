import boto3

aws_console = boto3.session.Session(profile_name="Prateek")
client_iam = aws_console.client(service_name="iam", region_name="ap-south-1")

# List all iam users using client object
response = client_iam.list_users()
for each_item in response['Users']:
    print(each_item['UserName'])