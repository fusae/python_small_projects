import subprocess
import os

def iconv(path):
    command = 'iconv -f cp936 -t utf-8 {}'.format(path)

    res = subprocess.check_output(command, shell=True)
    res = res.decode('utf-8')
#    print(res)
#    print('--------------------------------------------------')

    with open(path, 'w') as f:
        f.write(res)

        f.close()

def traverse(path):
    names = os.listdir(path)
    for name in names:
        name = path + '/' + name
        if os.path.isdir(name):
            traverse(name)
#        print(name)
        if ('.txt' in name):
            print(name)
            iconv(name)

if __name__ == '__main__':
    path = 'THE-DIRECTORY'

    traverse(path)

