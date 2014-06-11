import docker
from .resources import DockerResource
from .interfaces import IDockerClient
from .api import get_docker_client


def includeme(config):
    settings = config.registry.settings
    reg = config.registry
    base_url = settings.get('pyramid_docker.base_url',
                            'unix://var/run/docker.sock')
    def register():
        client = docker.Client(base_url=base_url)
        reg.registerUtility(client,
                            IDockerClient)
    config.action('pyramid_docker',
                  register)


def resource_factory(request):
    client = get_docker_client(request)
    return DockerResource(client)
