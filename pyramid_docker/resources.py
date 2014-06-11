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
        return iter(DockerContainerResource(self, c)
                    for c in self.client.containers())

    def __getitem__(self, key):
        for c in self.client.containers():
            if c['Id'] == key:
                return DockerContainerResource(self, c)
        raise KeyError(key)


class DockerContainerResource(object):
    def __init__(self, parent, container_data):
        self.__parent__ = parent
        self.__name__ = container_data['Id']
        self.data = container_data

    def __str__(self):
        return ",".join(self.data["Names"])
