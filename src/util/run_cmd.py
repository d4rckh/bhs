import subprocess

def open(cmd):
    out = []

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        l = line.decode("utf-8")
        out.append(l)
        if not l.strip == "":
            print(l)

    p.stdout.close()
    p.wait()

    return out