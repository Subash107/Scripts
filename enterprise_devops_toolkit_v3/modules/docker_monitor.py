import docker
import logging

def check_containers():
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)
        stopped = []

        for container in containers:
            if container.status != "running":
                msg = f"Container {container.name} is {container.status}"
                logging.warning(msg)
                stopped.append(msg)

        return stopped
    except Exception as e:
        logging.error(f"Docker error: {str(e)}")
        return []
