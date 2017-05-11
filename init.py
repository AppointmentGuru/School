import click, sys
from subprocess import call

@click.command()
def ansible():
    """Run a playbook"""
    cmd = ['ansible-playbook', 'play.yml']
    call(cmd)


if __name__ == '__main__':
    ansible()