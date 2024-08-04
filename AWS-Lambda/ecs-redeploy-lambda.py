import boto3
import json


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


def lambda_handler(event, context):
    # Extract the cluster name from the event (e.g., from an API Gateway or another trigger)
    cluster_name = event.get('cluster_name')
    region = event.get('region')

    if not cluster_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing cluster name')
        }

    # Call the function to force redeploy all ECS services in the cluster
    force_redeploy_all_ecs_services(cluster_name, region)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully triggered redeployment of all ECS services.')
    }
