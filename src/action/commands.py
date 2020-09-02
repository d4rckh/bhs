from rich.console import Console
from rich.table import Table
from src.util.run_cmd import open as run_cmd

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        self.requiredPorts = []
        pass

    def run(self):
        if self.args[1] == "s":
            for store in self.ses.stores:
                if store.name == "commandStore":
                    for key in store.val.keys():
                        if key == self.args[2]:
                            print(store.val[key])
                            break
                            
                    break
                        

        if self.args[1] == "v":
            console = Console()

            table = Table(show_header=True, header_style="bold green")
            table.add_column("Name", style="bold yellow", width=12)
            
            for store in self.ses.stores:
                if store.name == "commandStore":
                    for key in store.val.keys():
                        table.add_row(key)
                    break
            console.print(table)
