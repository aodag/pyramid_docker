from .interfaces import IDockerClient


def get_docker_client(request):
    reg = request.registry
    return reg.getUtility(IDockerClient)
