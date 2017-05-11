import click, sys
from subprocess import call

@click.group()
def app():
    pass

@click.group()
def service():
    pass

@click.command()
def release():
    print ('create a release')

@click.command()
@click.option('--do-token', prompt='Your digitalocean token',
              help='Your digital ocean API token.')
def init(do_token, *args, **kwargs):
    """Run a playbook"""
    cmds = []
    init_local_setup = [
        'ansible-playbook', 'ansible/bootstrap.yml',
        '-e', '"do_token={}"'.format(do_token)
    ]
    init_swarm = ['ansible-playbook', 'ansible/provision.swarm.yml']


    cmds.append(init_local_setup)
    for cmd in cmds:
        click.echo(" ".join(cmd))
        call(cmd)

@click.command()
def test(name):
    click.echo('hello!')

@click.command()
def cli(*args, **kwargs):
    click.echo(args)
    init()
