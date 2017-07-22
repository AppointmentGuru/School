import click, sys
from subprocess import call

@click.command()
def init(do_token, *args, **kwargs):
    """Run a playbook"""
    cmds = []
    init_swarm = [
        'ansible-playbook',
        'ansible/provision.swarm.yml',
        '-i',
        'ansible/inventory/digital_ocean.py'
    ]

    cmds.append(init_swarm)

    for cmd in cmds:
        click.echo(" ".join(cmd))
        call(cmd)

if __name__ == '__main__':
    init()
