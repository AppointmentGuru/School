import click, sys
from subprocess import call

@click.command()
@click.option('--do-token', prompt='Your digitalocean token', help='Your digital ocean API token.')
def init(do_token, *args, **kwargs):
    """Run a playbook"""
    cmds = []
    init_local_setup = [
        'ansible-playbook', '/code/ansible/bootstrap.yml',
        '-e', 'do_token={}'.format(do_token)
    ]
    cmds.append(init_local_setup)

    for cmd in cmds:
        click.echo(" ".join(cmd))
        call(cmd)

if __name__ == '__main__':
    init()