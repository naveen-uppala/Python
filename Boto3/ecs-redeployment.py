import boto3

def force_redeploy_all_ecs_services(cluster_name):
    # Initialize ECS client
    ecs_client = boto3.client('ecs')

    try:
        # List all services in the cluster
        response = ecs_client.list_services(cluster=cluster_name)
        service_arns = response['serviceArns']

        # Iterate over each service and force a redeployment
        for service_arn in service_arns:
            service_name = service_arn.split('/')[-1]
            force_redeploy_ecs_service(cluster_name, service_name)
    except Exception as e:
        print(f"Error listing or redeploying services in cluster '{cluster_name}': {e}")

if __name__ == "__main__":
    # Set your AWS credentials and region
    aws_region = 'YOUR_AWS_REGION'

    # Set the name of the ECS cluster
    cluster_name = 'YOUR_CLUSTER_NAME'

    # Set up Boto3 client with your credentials and region
    boto3.setup_default_session(region_name=aws_region
    )

    # Force redeploy all ECS services in the cluster
    force_redeploy_all_ecs_services(cluster_name)
