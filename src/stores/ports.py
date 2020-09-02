class Store:
    def __init__(self):
        self.val = {}
        self.name = "ports"
        self.description = "This store stores the ports on the machine (port, type, service); type \"ports\" to see ports"

    def update(self, key, val):
        self.val[key] = val