import subprocess,time
from src import constants as cs
apps =[
    'aircrack-ng',
    'xterm'
]
print(f"{cs.bold_blue}")
for i in apps:
    subprocess.run(["sudo","apt","install",i])
    time.sleep(1)
print(f"{cs.bold_green} All done.")