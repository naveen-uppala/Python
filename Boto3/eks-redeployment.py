import boto3
import os
from kubernetes import client, config

def redeploy_eks_pods(cluster_name, namespace):
    try:
        # Load Kubernetes config
        config.load_kube_config()

        # Initialize Kubernetes API client
        api_instance = client.AppsV1Api()

        # List deployments in the specified namespace
        deployment_list = api_instance.list_namespaced_deployment(namespace)

        # Iterate over deployments and trigger an update
        for deployment in deployment_list.items:
            deployment_name = deployment.metadata.name
            print(f"Updating deployment {deployment_name} in namespace {namespace}...")
            # Patch the deployment to trigger a rolling update
            api_instance.patch_namespaced_deployment(
                name=deployment_name,
                namespace=namespace,
                body={"spec": {"template": {"metadata": {"annotations": {"kubectl.kubernetes.io/restartedAt": str(os.time())}}}}},
            )
            print(f"Deployment {deployment_name} updated successfully.")
    except Exception as e:
        print(f"Error redeploying pods in namespace {namespace}: {e}")

if __name__ == "__main__":
    # Set your AWS credentials and region
    aws_region = 'YOUR_AWS_REGION'

    # Set the name of the EKS cluster
    cluster_name = 'YOUR_CLUSTER_NAME'

    # Set the Kubernetes namespace where the deployments are located
    namespace = 'default'

    # Set up Boto3 client with your credentials and region
    boto3.setup_default_session(region_name=aws_region)

    # Redeploy pods in the EKS cluster
    redeploy_eks_pods(cluster_name, namespace)
