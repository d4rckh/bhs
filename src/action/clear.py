from os import system
from src.util.run_cmd import open as run_cmd
from src.util.cRes import cRes as res
from src.util.checkPort import checkPort

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        self.requiredPorts = []
        pass

    def run(self):
	system("clear")	
