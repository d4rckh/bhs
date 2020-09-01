class cRes:
    def __init__(self, t, res):
        self.updateStore = True
        self.which = t
        self.ports = None
        self.target = None
        if t == "ports":
            self.ports = res
        if t == "target":
            self.target = res
        