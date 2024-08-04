import boto3

def force_redeploy_all_ecs_services(cluster_name, region):
    # Initialize ECS client
    ecs_client = boto3.client('ecs', region_name=region)

    try:
        # List all services in the cluster
        response = ecs_client.list_services(cluster=cluster_name)
        service_arns = response['serviceArns']

        # Iterate over each service and force a redeployment
        for service_arn in service_arns:
            service_name = service_arn.split('/')[-1]
            print(service_name)
            response = ecs_client.update_service(cluster=cluster_name,service=service_name,forceNewDeployment=True)
            return response
            # force_redeploy_ecs_service(cluster_name, service_name)
    except Exception as e:
        print(f"Error listing or redeploying services in cluster '{cluster_name}': {e}")

if __name__ == "__main__":
    # Set your AWS credentials and region
    region = input("enter the region: ")

    # Set the name of the ECS cluster
    cluster_name = input("enter the cluster name: ")
 
    # Force redeploy all ECS services in the cluster
    force_redeploy_all_ecs_services(cluster_name, region)
