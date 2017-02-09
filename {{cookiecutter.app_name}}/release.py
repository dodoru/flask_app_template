#!/usr/bin/env python
import os
import ConfigParser
from manager import Manager
from functools import partial
from subprocess import check_call as _call

call = partial(_call, shell=True)

manage = Manager()

base_path = os.path.dirname(os.path.abspath(__file__))


@manage.command
def build_docker(suffix='', latest=False):
    '''
    :param part: ['major', 'minor', 'patch']
    :return: git tag amd docker build/tag/push
    '''
    config = ConfigParser.ConfigParser()
    config.read(".bumpversion.cfg")
    version = config.get('bumpversion', 'current_version')

    docker_host = config.get('docker', 'host')
    docker_name = config.get('docker', 'name')
    deploy_log = config.get('docker', 'deploy_log')
    image = "%s/%s:%s%s" % (docker_host, docker_name, version, suffix)

    call("docker build -t {image} .".format(image=image))
    call("docker push {image}".format(image=image))
    print(image)

    if latest:
        latest_tag = config.get('docker', 'latest_tag')
        latest_image = "%s/%s:%s" % (docker_host, docker_name, latest_tag)
        call("docker tag {image} {latest_image}".format(image=image, latest_image=latest_image))
        call("docker push {latest_image}".format(latest_image=latest_image))
        print(latest_image)

    call('echo {} >> {}'.format(image, deploy_log))


@manage.command
def deploy(part='patch', suffix=''):
    assert part in ['major', 'minor', 'patch']
    call("bumpversion %s" % part)
    build_docker(suffix)


if __name__ == "__main__":
    manage.main()
