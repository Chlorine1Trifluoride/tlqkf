import subprocess, os, sys
try:import py7zr
except ImportError: 
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'py7zr'], check=True)
    import py7zr
def download():
    global directory
    directory = os.path.join('C:', 'Users', 'user', 'VirtualBox VMs')
    os.makedirs( directory, exist_ok=True )
    def get(a):
        number = str(a)
        return subprocess.Popen(['gh', 'release', 'download', '--repo', 'Chlorine1Trifluoride/UbuntuSetUp', '--pattern', f'CFD SIMULATOR.7z.{'0'*(3-len(number))}{number}', '--dir', directory], cwd=directory, shell=True)
    process = []
    for i in range(1, 80, 12):
        batch = list(range(i, i+12))
        for n in batch:
            p = get(n)
            process.append(p)
        for p in process: p.wait()
        process.clear()
try:
    download()
except:
    try:
        subprocess.run(['gh', 'auth', 'login'], check=True)
        download()
    except:
        subprocess.run(['winget', 'install', '--id', 'GitHub.cli', '-e'], check=True)
        subprocess.run(['gh', 'auth', 'login'], check=True)
        download()
with py7zr.SevenZipFile(os.path.join(directory, 'CFD SIMULATOR.7z.001'), mode='r') as archive: archive.extractall(path=directory)