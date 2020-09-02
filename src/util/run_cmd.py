import subprocess

def open(cmd):
    out = []

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        out.append(line.decode("utf-8"))
        
    p.stdout.close()
    p.wait()

    return out