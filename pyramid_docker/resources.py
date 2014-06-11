class DockerResource(dict):
    __parent__ = __name__ = None
    def __init__(self, client):
        super(DockerResource, self).__init__()
        self.client = client
        self["containers"] = DockerContainerCollection(self, self.client)


class DockerContainerCollection(object):
    __name__ = "containers"
    def __init__(self, parent, client):
        self.__parent__ = parent
        self.client = client

    def __iter__(self):
        return iter(self.client.containers())
