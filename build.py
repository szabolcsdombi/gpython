import ccompiler

compiler = ccompiler.Compiler(python=True)
compiler.sources = ['gpython.c']
compiler.compile('build/gpython.exe')

with open('build/gpython.exe', 'rb') as f:
    exe = f.read().hex()

installer = f'''
import os
import sys

path = os.path.join(os.path.dirname(sys.executable), 'gpython.exe')
with open(path, 'wb') as f:
    f.write(bytes.fromhex("{exe}"))

print(f"Successfully installed at {{path}}")
'''

with open('gpython.py', 'w') as f:
    f.write(installer.strip() + '\n')
