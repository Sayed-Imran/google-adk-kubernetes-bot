# Kubernetes Assistant Agent

A Google Agent Development Kit (ADK) powered assistant that interacts with Kubernetes clusters to provide information about resources.

## Overview

This repository contains a Kubernetes Assistant Agent built with Google's Agent Development Kit (ADK) that can help you manage and monitor your Kubernetes clusters through natural language conversations. The agent leverages the Google Gemini model to understand user queries and uses Kubernetes API functions to retrieve information from your cluster.

## Features

The Kubernetes Assistant can:

- List all namespaces in your Kubernetes cluster
- List deployments in a specific namespace
- List pods in a specific namespace
- List services in a specific namespace
- Retrieve all resources (deployments, pods, services) in a specific namespace

## Prerequisites

- Python 3.10+
- Google API key for Gemini access
- Kubernetes configuration file set up on your machine
- Required Python packages:
  - `google-adk`
  - `kubernetes`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sayed-imran/google-adk-kubernetes-bot.git
   cd google-adk-kubernetes-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install google-adk kubernetes
   ```

3. Set up your Google API key:
   ```bash
   export GOOGLE_API_KEY="your-api-key"
   ```

4. Ensure your Kubernetes configuration is properly set up and accessible.

## Usage

Run the agent using the following command:

```bash
adk web
```

## Structure

- `kubernetes-bot/`
  - `agent.py`: Contains the agent implementation and setup with Gemini model
  - `tools/`
    - `tools.py`: Contains Kubernetes API functions used by the agent
  - `__init__.py`: Package initialization file
