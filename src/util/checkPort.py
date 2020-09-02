def checkPort(ses, port):
    for store in ses.stores:
        if store.name == "ports":
            ports = store.val["nmap"]
            for port in ports:
                if port == ports[0]:
                    return True
    return False