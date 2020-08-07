import os
import subprocess

import click


@click.command()
@click.option('--name', default='', help='your name')
def cli(name):
    """
    Say hello 

    :param name: Your name
    :return: A greeting to you
    """
    # cmd = 'echo hello {0}'.format(name)
    # return subprocess.call(cmd, shell=True)
    click.echo('hello {}'.format(name))