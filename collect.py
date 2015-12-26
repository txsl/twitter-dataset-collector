import subprocess

try:
    p = subprocess.check_output(['./run.sh', 'a', 'b'])
    print p
except subprocess.CalledProcessError as shexec:
    print shexec.returncode, shexec.output, 'error!'