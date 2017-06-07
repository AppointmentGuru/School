import click, sys
from subprocess import call

@click.command()
def init(*args, **kwargs):
    """Run a playbook"""
    cmds = []
    init_local_setup = ['ansible-playbook', 'ansible/bootstrap.yml']
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
def cli(*args, **kwargs):
    click.echo(args)
    init()

if __name__ == '__main__':
    init()
