import click
from cloudcompose.cluster.cloudinit import CloudInit

@click.group()
def cli():
    pass

@cli.command()
def up():
    """
    creates a new cluster
    """
    print "in cluster up command"

@cli.command()
def down():
    """
    destroys an existing cluster
    """
    print "in cluster down command"

@cli.command()
def build():
    """
    builds the cloud_init script
    """
    print "in cluster build command"
    cloud_init = CloudInit('cloud-compose/cloud-compose.yml', 'cloud-compose/test.template.sh')
    print cloud_init.build()
