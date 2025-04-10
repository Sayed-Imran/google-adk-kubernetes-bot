from kubernetes import client, config

config.load_config()


api_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()


def list_namespaces() -> list:
    """
    List all namespaces in the Kubernetes cluster.
    
    Returns:
        list: A list of namespace names.
    """
    namespaces = api_v1.list_namespace()
    return [ns.metadata.name for ns in namespaces.items]

def list_deployments_from_namespace(namespace: str) -> list:
    """
    List all deployments in a specific namespace.

    Args:
        namespace (str): The namespace to list deployments from.

    Returns:
        list: A list of deployment names in the specified namespace.
    """
    deployments = apps_v1.list_namespaced_deployment(namespace)
    return [deploy.metadata.name for deploy in deployments.items]

def list_pods_from_namespace(namespace: str) -> list:
    """
    List all pods in a specific namespace.

    Args:
        namespace (str): The namespace to list pods from.

    Returns:
        list: A list of pod names in the specified namespace.
    """
    pods = api_v1.list_namespaced_pod(namespace)
    return [pod.metadata.name for pod in pods.items]

def list_services_from_namespace(namespace: str) -> list:
    """
    List all services in a specific namespace.

    Args:
        namespace (str): The namespace to list services from.

    Returns:
        list: A list of service names in the specified namespace.
    """
    services = api_v1.list_namespaced_service(namespace)
    return [svc.metadata.name for svc in services.items]

def list_all_resources(namespace: str) -> dict:
    """
    List all resources in a specific namespace.

    Args:
        namespace (str): The namespace to list resources from.

    Returns:
        dict: A dictionary containing lists of deployments, pods, and services for a specific namespace.
    """
    resources = {
        "deployments": list_deployments_from_namespace(namespace),
        "pods": list_pods_from_namespace(namespace),
        "services": list_services_from_namespace(namespace)
    }
    return resources


__all__ = [
    "list_namespaces",
    "list_deployments_from_namespace",
    "list_pods_from_namespace",
    "list_services_from_namespace",
    "list_all_resources"
]
