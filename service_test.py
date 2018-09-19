import subprocess
import sys,os

PEM="myaws.pem"
USER="ec2-user"
commands="w"

os.system("ssh -i myaws.pem ec2-user@ec2-34-203-10-10.compute-1.amazonaws.com" + commands)