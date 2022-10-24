import click
from rich.table import Table
from rich.console import Console
from rich.progress import track
from .constants import COMMANDS_NAMES
from .select import pick
from .generators import (
    generate_dpy, generate_pycord, generate_nextcord, generate_disnake
)
console = Console()


@click.group()
def cli():
    pass


@cli.command()
def help():
    table = Table(title='Zoolkit help menu.',
                  caption="<> - This is required arg\n[] - This is optional arg", )
    table.add_column("Commands", style='cyan')
    table.add_column("Usages", style='cyan')
    table.add_column("Descriptions", style='cyan')
    for i in COMMANDS_NAMES:
        table.add_row(i["name"], i["description"], i["usage"])
    console.print(table)


@cli.command()
def create():
    # Select api wrapper
    wrapper_title = 'Please choose a discord api wrapper: '
    wrapper_options = ["discord.py", "pycord", "nextcord", "disnake"]
    wrapper_selected, wrapper_index = pick(
        wrapper_options, wrapper_title, indicator='>')

    # Select generator type (template or cog)
    generator_title = "Please choose a generator type: "
    generator_options = ["Basic bot", 'Advance Bot', 'Cog']
    generator_selected, generator_index = pick(
    generator_options, generator_title, indicator='>')

    #Index to function
    calls = {
        0: generate_dpy,
        1: generate_pycord,
        2: generate_nextcord,
        3: generate_disnake
    }
    for i, f in calls.items():
        if wrapper_index == i:
            return f(i)
