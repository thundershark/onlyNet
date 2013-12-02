__author__ = 'salamander'
import subprocess,os,time
import threading
import re

#os.chdir('../')
pingTime = 1
restartTime = 3
startTime = 10
vpnComand = os.getcwd() + '/vpnEmulator.sh'
def decode(string):
    '''декод данных из bash'''
    return  string.decode('utf8')

def createShell(cmd, inarg=False):
    '''simple create subprocess'''
    if inarg:
        return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def successRead(shell):
    '''построчное чтение из потока с шелла'''
    line = True
    while line:
        line = decode(shell.stdout.readline( ))
        yield line

def connected():
    ''' проверяет есть ли соединение (пинг)'''''
    return False

def mainStream():
    '''основной поток выполнения программы'''
    while 1:
        if not connected():
            #kill other therads
            vpnStart()
        time.sleep(1)



def vpnStart():
    '''запуск vpn'''
    #запустить openvpn
    #парсить вывод1
    #сообщить обо всем в main
    vpn = createShell(vpnComand)
    for line in successRead(vpn):
        print(line)




def main():
    mainStream()

if __name__ == '__main__':
    main()