from src.util.run_cmd import open as run_cmd
from src.util.cRes import cRes as res

class Command:
    def __init__(self, args, session):
        self.args = args
        self.ses = session
        self.requiredPorts = []
        pass

    def run(self):
        result = run_cmd(["nmap", self.ses.target])

        ports = []

        for line in result:
            if "open" in line:
                parts = line.split("open")
                portntype = parts[0].strip()
                port = portntype.split("/")[0]
                ptype = portntype.split("/")[1]
                service = parts[1].strip()
                
                ports.append([port,ptype,service])
                
        return res("ports", "nmap", ports)