import boto3

def check_running_instances(region):
    # Initialize EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    try:
        # Get information about all running instances
        response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        # Extract instance information
        instances = response['Reservations']
        if instances:
            print("Running Instances:")
            for reservation in instances:
                for instance in reservation['Instances']:
                    print(f"Instance ID: {instance['InstanceId']}, Instance Type: {instance['InstanceType']}")
        else:
            print("No running instances found.")
    except Exception as e:
        print(f"Error checking running instances: {e}")

if __name__ == "__main__":
    # aws_region = 'us-east-2'

    # # Set up Boto3 client with your credentials and region
    # boto3.setup_default_session(region_name=aws_region)

    # Check for running instances
    check_running_instances()
