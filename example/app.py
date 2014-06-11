from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def index(context, request):
    return dict()

def containers(context, request):
    return dict()


def main():
    config = Configurator(
        root_factory='pyramid_docker.resource_factory')
    config.include('pyramid_mako')
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_docker')
    config.add_view(index,
                    context='pyramid_docker.resources.DockerResource',
                    renderer="index.mako")
    config.add_view(containers,
                    context='pyramid_docker.resources.DockerContainerCollection',
                    renderer="containers.mako")
    app = config.make_wsgi_app()
    httpd = make_server('', 8080, app)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
