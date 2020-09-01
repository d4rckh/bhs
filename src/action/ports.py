from rich.console import Console
from rich.table import Table
from src.util.run_cmd import open as run_cmd

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        pass

    def run(self):

        for store in self.ses.stores:
            if store.name == "ports":
                self.ses.ports = store.val
                console = Console()

                table = Table(show_header=True, header_style="bold green")
                table.add_column("Port", style="bold yellow", width=12)
                table.add_column("Type", style="red")
                table.add_column("Service", justify="right", style="bold blue")

                for port in self.ses.ports:
                    table.add_row(
                        port[0], port[1], port[2]
                    )

                console.print(table)