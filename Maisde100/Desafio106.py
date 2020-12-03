from time import sleep
config = ('\033[m',
          '\033[0;30;41m',
          '\033[0;30;42m',
          '\033[0;30;43m',
          '\033[0;30;44m',
          '\033[0;30;45m',
          '\033[7;30m');


def ajuda(com):
  titulo(f'Acessando manual do comando \'{com}\'', 4)
  print(config[6], end='')
  help(com)
  print(config[0], end='')
  sleep(2)


def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(config[cor], end='')
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)
  print(config[0], end='')
  sleep(1)


comando = ''
while True:
  titulo('SISTEMA DE AJUDA PyHELP', 2)
  comando = str(input('Funcao ou Biblioteca > '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
titulo('ATE LOGO!', 1)