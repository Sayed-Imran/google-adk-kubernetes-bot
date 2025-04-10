from google.adk.agents import Agent
from .tools.tools import *

root_agent = Agent(
    name="kubernetes_assistant",
    model="gemini-2.0-flash-exp",
    instruction="You are a helpful assistant. Who can perform tasks of Kubernetes cluster management such as listing namesspaces, deployemnts, pods, and services. Answer the user's questions using the tools available and present response in Markdown format.",
    description="An assistant that can help you with your Kubernetes cluster",
    tools=[list_namespaces, list_deployments_from_namespace, list_pods_from_namespace, list_services_from_namespace, list_all_resources],
)
