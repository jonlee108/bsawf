import os
import subprocess

import click


@click.command()
@click.argument('name', default='')
def cli(name):
    """
    Say hi 

    :option name: Your name
    :return: A greeting to you
    """
    # cmd = 'echo hello {0}'.format(name)
    # return subprocess.call(cmd, shell=True)
    click.echo('hi {}'.format(name))