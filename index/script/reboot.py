from subprocess import Popen
import subprocess

def shutdown():
    with Popen(['/bin/bash', '-l', '-c', "sudo shutdown -r now"]
            , stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
        p.wait()
