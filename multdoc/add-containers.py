import yaml
import os
import sys

DOCKER_COMPOSE = "docker-compose.yaml"

def add_container():
    try:
        if not os.path.exists(DOCKER_COMPOSE):
            with open(DOCKER_COMPOSE, 'r') as f:
                docker_compose_config = yaml.safe_load(f)
    except:
        sys.exit(1)