from subprocess import run,PIPE
import sys

output = run([sys.executable,"/home/ark/Downloads/reactSchedule/scheduler/src/scheduler.py",
        "108117015",
        "Eceboy.14",
        "ECPC",
        "REBEKKA B",
        "22:30",
        "MON,TUE"],shell=False,stdout=PIPE)
print(output)