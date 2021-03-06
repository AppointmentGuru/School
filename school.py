import click, sys
from subprocess import call

@click.command()
@click.option('--do-token', prompt='Your digitalocean token',
              help='Your digital ocean API token.')
def init(do_token, *args, **kwargs):
    """Run a playbook"""
    cmds = []
    init_local_setup = [
        'ansible-playbook', 'ansible/bootstrap.yml',
        '-e', 'do_token={}'.format(do_token)
    ]
    init_swarm = [
        'ansible-playbook',
        'ansible/provision.swarm.yml',
        '-i',
        'ansible/inventory/digital_ocean.py'
    ]

    cmds.append(init_local_setup)
    cmds.append(init_swarm)

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

if __name__ == '__main__':
    init()
