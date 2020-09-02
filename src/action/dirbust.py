from src.util.run_cmd import open as run_cmd
from src.util.cRes import cRes as res
from src.util.checkPort import checkPort

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        self.requiredPorts = ["80"]
        pass

    def run(self):
        
        out = run_cmd(["python3", "/home/d4rckh/Desktop/dirsearch/dirsearch.py", "-u", "http://" + self.ses.target, "-w", 
                    "/home/d4rckh/Desktop/bhs/wordlist",
                    "-e", "php,txt,zip"])

        return(res("commandStore", "dirbust", "".join(out)))
