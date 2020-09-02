import src.bhssettings as settings
import src.util.cRes as cRes
from src.util.checkPort import checkPort

def handle(cmd, args, ses):
    if cmd.strip() == "":
        return None
    if cmd == "target":
        return cRes.cRes("target", None, args[1])
    else:
        try:
            cFile = __import__("src.action." + cmd, fromlist=["Command"])
        except:
            return
        cClass = cFile.Command(args, ses)
        fail = False
        error = ""
        for port in cClass.requiredPorts:
            if not checkPort(ses, port):
                fail = True
                error = f"Port {port} is required to be open in order to use {cmd}! "
                break

        if fail:
            return print(error)
        else:
            return cClass.run()