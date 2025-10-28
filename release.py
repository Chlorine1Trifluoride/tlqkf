import subprocess, os
directory = os.path.join('C:', 'Users', 'user', 'VirtualBox VMs')
os.makedirs( directory, exist_ok=True )
def upload(a):
    number = str(a)
    return subprocess.Popen(['gh', 'release', 'create', 'v1.1', '--repo', 'Chlorine1Trifluoride/UbuntuSetUp', f'CFD SIMULATOR.7z.{'0'*(3-len(number))}{number}', '--dir', directory], cwd=directory, shell=True)
def release():    
    process = []
    for i in range(1, 100, 12):
        batch = list(range(i, i+12))
        for n in batch:
            p = upload(n)
            process.append(p)
        for p in process: p.wait()
        process.clear()
try: subprocess.run(['gh', 'release', 'view', 'v1.1'], shell=True); subprocess.run(['gh', 'release', 'delete', 'v1.1'], shell=True)
except: subprocess.run(['gh', 'release', 'create', 'v1.1', '--repo', 'Chlorine1Trifluoride/UbuntuSetUp', '--title', '제발 그냥 죽여주세요...', '--notes', '그냥 죽여 차라리.....'], shell=True)
