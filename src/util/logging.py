
from rich.console import Console
from rich.table import Table


def newSet(value, oldv, newv, by):
    console = Console()

    table = Table(show_header=True, header_style="bold green")
    table.add_column("Key", style="dim", width=12)
    table.add_column("Old Value")
    table.add_column("New Value", justify="right")
    table.add_column("BY", justify="right")
    table.add_row(
        value, oldv, newv, by
    )

    console.print(table)
