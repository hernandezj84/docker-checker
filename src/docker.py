"""Docker module"""

import docker
from src.requests_helper import send_message

def is_docker_running(container_name):
    """Checks if given container_name is running"""
    docker_client = docker.from_env()
    try:
        container = docker_client.containers.get(container_name)
        container_state = container.attrs["State"]
        print(container_state)
        return(container_state)
    except docker.errors.NotFound as e:
        send_message(f"Container {container_name} not found")


