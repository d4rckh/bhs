class Store:
    def __init__(self):
        self.name = "commandStore"
        self.description = "This store stores the command outputs"
        self.val = {}

    def update(self, cmd, output):
        self.val[cmd] = output