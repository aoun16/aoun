#coding=utf-8
try:
    import os,sys,subprocess,requests
except ModuleNotFoundError:
    os.system('pip install requests futures bs4')
    os.system('python aoun.py')
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('a64'):
        os.system('curl -L https://github.com/aoun16/files/blob/main/hop/for_termux/aarch64/a64?raw=true > a64')
        os.system('chmod 777 a64')
        os.system('./a64')
    else:
        os.system('./a64')
elif 'arm' in str(current_os):
    if not os.path.isfile('a32'):
        os.system('curl -L https://github.com/aoun16/files/blob/main/hop/for_termux/arm/a32?raw=true > a32')
        os.system('chmod 777 a32')
        os.system('./a32')
    else:
        os.system('./a32')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    print('  Owner whatsapp: +92321-5822365\n\n')
    os.sys.exit()
