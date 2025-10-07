import subprocess 

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd):
    # Perbaikan: tidak menggunakan shell=True
    # Menggunakan daftar argumen agar tidak dieksekusi langsung oleh shell
    if isinstance(cmd, str):
        cmd = cmd.split()
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
