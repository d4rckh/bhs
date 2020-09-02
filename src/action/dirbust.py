from src.util.run_cmd import open as run_cmd
from src.util.cRes import cRes as res
from src.util.checkPort import checkPort
from src.bhssettings import dirbustCommand

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        self.requiredPorts = ["80"]
        pass

    def run(self):
        
        cm = []

        for e in dirbustCommand:
            cm.append(e.replace("(target)", self.ses.target))

        out = run_cmd(cm)

        return(res("commandStore", "dirbust", "".join(out)))
