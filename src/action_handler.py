import src.bhssettings as settings
import src.util.cRes as cRes

def handle(cmd, args, ses):
    if cmd.strip() == "":
        return None
    if cmd == "target":
        return cRes.cRes("target", args[1])
    else:
        cFile = __import__("src.action." + cmd, fromlist=["Command"])
        cClass = cFile.Command(args, ses)
        return cClass.run()