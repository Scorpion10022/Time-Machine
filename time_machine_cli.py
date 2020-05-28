import click
from time_machine_api import *

@click.group(help="Time Machine Api")
@click.option(
    "--verbose",
    "-v",
    default=False,
    is_flag=True,
    show_default=True,
    help="Enable debug output",
)
@click.pass_context
def cli(ctx, verbose):
    ctx.obj = TimeMachineApi()

#Pools Commands
@cli.group(help="Pools Commands")
@click.pass_context
def pools(ctx):
    pass

@pools.command(help="Get pools list")
@click.pass_obj
def get(api):
    pprint(api.get_pools())

#Datasets Commands
@cli.group(help="Datasets Commands")
@click.pass_context
def datasets(ctx):
    pass

@datasets.command(help="Get datasets list")
@click.pass_obj
def get(api):
    sys_datasets = api.get_datasets()
    pprint(sys_datasets)

@datasets.command(help="Create a new dataset")
@click.option("--name", required=True, help="Name of the new dataset")
@click.pass_obj
def create(api,name):
    if api.create_dataset({"name": f"hybrid/{name}"}):
        pass
    else:
        print("Error creating dataset or invalid dataset format")

@datasets.command(help="Delete a new dataset")
@click.option("--name", required=True, help="Name of the dataset to be deleted")
@click.pass_obj
def delete(api,name):
    r = api.delete_dataset({"name": f"hybrid/{name}"})
    if r.status_code == 200:
        pprint("Dataset deleted")
    elif r.status_code == 404:
        pprint("Dataset not found")
    else:
        pprint("Error deleting dataset or invalid dataset format")

@datasets.command(help="Rename a dataset")
@click.option("--name", required=True, help="Name of the dataset to be renamed")
@click.option("--new-name", required=True, help="New name of the dataset")
@click.pass_obj
def rename(api,name,new_name):
    r = api.rename_dataset({"from_name" : f"hybrid/{name}", "rename_to" : f"hybrid/{new_name}"})
    if r.status_code == 200:
        pprint("Dataset renamed")
    elif r.status_code == 404:
        pprint("Dataset not found")
    else:
        pprint("Error renaming dataset or invalid dataset format")

#Snapshots Commands
@cli.group(help="Snapshots Commands")
@click.pass_context
def snapshots(ctx):
    pass

@snapshots.command(help="Get snapshots list")
@click.pass_obj
def get(api):
    sys_snapshots = api.get_snapshots()
    pprint(sys_snapshots)


if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        pass
