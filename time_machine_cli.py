import click
from time_machine_api import *

#Needs to be done: Create a check metod in api

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
    pprint(api.get_datasets())

@datasets.command(help="Create a new dataset")
@click.option("--name", required=True, help="Name of the new dataset")
@click.pass_obj
def create(api,name):
    if api.create_dataset({"name": f"hybrid/{name}"}):
        pprint(f"Dataset created with name: {name}")
    else:
        pprint("Error creating dataset or invalid dataset format")

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
    pprint(api.get_snapshots())

@snapshots.command(help="Create a new snapshot")
@click.option("--ds-name", required=True, help="Name of the dataset")
@click.option("--ss-name", required=False, help="Name of the snapshot")
@click.pass_obj
def create(api,ds_name,ss_name):
    if ds_name == "hybrid":
        if ss_name:
            r = api.create_snapshot({"dataset": f"{ds_name}"})
        else:
            r = api.create_snapshot({"dataset": f"{ds_name}" , "snapshot": f"{ss_name}"})
    else:
        if ss_name:
            r = api.create_snapshot({"dataset": f"hybrid/{ds_name}"})
        else:
            r = api.create_snapshot({"dataset": f"hybrid/{ds_name}" , "snapshot": f"{ss_name}"})
    if r.status_code == 200:
        pprint("Snapshot created")
    elif r.staus_code == 404:
        pprint("Dataset not found")
    else:
        pprint("Error creating snapshot or invalid dataset format")

@snapshots.command(help="Delete a snapshot")
@click.option("--name", required=True, help="Name of the snapshot")
@click.pass_obj
def delete(api,name):
    pprint(f"hybrid/{name}")
    if name.split("@")[0] == "hybrid":
        r = api.delete_snapshot({"name": f"{name}"})
    else:
        r = api.delete_snapshot({"name": f"hybrid/{name}"})
    if r.status_code == 200:
        pprint("Snapshot deleted")
    else:
        pprint("Error deleting snapshot or invalid format")


@snapshots.command(help="Rename a snapshot")
@click.option("--name", required=True, help="Name of the snapshot to be renamed( dataset@snapshot_name)")
@click.option("--new-name", required=True, help="New name of the snapshot( dataset@new_snapshot_name)")
@click.pass_obj
def rename(api,name,new_name):
    if name.split("@")[0] == "hybrid":
        r = api.rename_snapshot({"from_name" : f"{name}", "rename_to" : f"{new_name}"})
    else:
        r = api.rename_snapshot({"from_name" : f"hybrid/{name}", "rename_to" : f"hybrid/{new_name}"})
    if r.status_code == 200:
        pprint("Snapshot renamed")
    else:
        pprint("Error renaming snapshot or invalid dataset format")

@snapshots.command(help="Rollback to a snapshot")
@click.option("--name", required=True, help="Name of the snapshot to be rolledbacked to.")
@click.pass_obj
def rollback(api,name):
    if name.split("@")[0] == "hybrid":
        r = api.rollback_snapshot({"name":f"{name}"})
    else:
        r = api.rollback_snapshot({"name":f"hybrid/{name}"})
    if r.status_code == 200:
        pprint("Rollback succes")
    elif r.status_code == 404:
        pprint("Snapshot not found")
    else:
        pprint("Error rolling back to this snapshot")

#Under construction
@snapshots.command(help="Clone a snapshot")
@click.option("--ds", required=True, help="Name of the new dataset to be cloned into.")
@click.option("--name", required=True, help="Name of the snapshot to be cloned.")
@click.pass_obj
def clone(api,ds,name):
    r = api.clone_snapshot({"dataset": f"hybrid/{ds}", "snapshot": f"hybrid/{name}"})
    if r.status_code == 200:
        pprint("Clone succes")
    elif r.status_code == 404:
        pprint("Snapshot not found")
    else:
        pprint("Error creating clone or invalid snapshot / dataset name")

if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        pass
