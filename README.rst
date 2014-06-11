======================
pyramid_docker
======================

INSTALL
======================

::

  $ pip install pyramid_docker


USAGE
===================

api
--------------------

::

  config.include('pyramid_docker')


resource factory
----------------------------

::

  config.set_root_factory('pyramid_docker.resource_factory')
