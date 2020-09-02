import os
import src.bhssettings as settings
import src.action_handler as ah
import src.util.logging

class Session:
    def __init__(self):
        self.target = "none"
        self.stores = []
        self.startStore()
        
        self.script("script.txt")
        
        self.listen()


    def listen(self):
        while True:
            UserInput = input(settings.prompt.replace("(target)", self.target))
            self.handleCmd(UserInput)

    def script(self, scriptFile):
        with open(scriptFile, "r") as script:
            lines = script.read().split("\n")
            for line in lines :
                self.handleCmd(line)

    def handleCmd(self, UserInput):
        args = UserInput.split(" ")
        out = ah.handle(args[0], args, self)
        if out:
            if out.which == "target":
                src.util.logging.newSet("target", self.target, out.val, "cmd(" + args[0] + ")")
                self.target = out.val
            else:
                if out.updateStore:
                    for store in self.stores:
                        if store.name == out.which:
                            store.update(out.key, out.val)

    def startStore(self):
        dire = os.listdir("./src/stores")
        for file in dire:
            if (file.startswith("__")):
                continue
            filename = file.split(".")[0]
        
            cFile = __import__("src.stores." + filename, fromlist=["Command"])  
            store = cFile.Store()
            self.stores.append(store)