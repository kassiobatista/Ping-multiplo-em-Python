from os import system

from time import sleep


with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('\033[35m_/\033[m' *60)
        system('ping -n 2 {}'.format(ip))
        print('\033[35m_/\033[m' *60)
        sleep(5)