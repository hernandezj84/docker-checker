"""Run the implementation"""
import os
import time
from src.docker import is_docker_running
from src.requests_helper import send_message

CONTAINER_NAME = os.getenv('CONTAINER_NAME')
TIME_BETWEEN = os.getenv('TIME_BETWEEN')

if __name__ == "__main__":
    while True:
        running = is_docker_running(CONTAINER_NAME)
        if not running:
            send_message(f"Container {CONTAINER_NAME} is not running")
        time.sleep(str(TIME_BETWEEN))

