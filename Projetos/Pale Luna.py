from time import sleep
import sys

acao = "variable"

print('''Você está em uma sala escura. A luz da lua raia pela janela.
Há OURO no canto da sala, junto com uma PÁ e uma CORDA.
Tem uma PORTA no LESTE.

Comando?

Você vê uma PORTA aqui.''')

while True:
    acao = str(input(">")).upper().strip()
    acao = acao.replace(" " , "")
    if acao == "PEGARPA" or acao == "PEGAROURO" or acao == "PEGARCORDA" or acao == "PEGARAPA" or acao == "PEGAROOURO" or acao == "PEGARACORDA":
        print("Pegou.")
    elif acao == "ABRIRPORTA" or acao == "ABRIRAPORTA":
        print("Você abriu a PORTA.")
    elif acao == "LESTE":
        break
    else:
        sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "NORTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e OESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "LESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "NORTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "NORTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o OESTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e OESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "OESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "NORTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o OESTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "LESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "LESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e OESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o OESTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "LESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "SUL":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, OESTE e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "OESTE":
    sys.exit(0)

print('''Pegue sua recompensa.
A LUA PÁLIDA SORRI PARA VOCÊ.
      


Você está em uma floresta. Existem caminhos  para o NORTE, SUL e LESTE.
      Comando?''')

acao = str(input(">")).upper().strip()
if acao != "NORTE":
    sys.exit(0)

print('''A LUA PÁLIDA SORRI LARGAMENTE.
Nâo há caminhos.
A LUA PÁLIDA SORRI LARGAMENTE.
O chão está macio.
A LUA PÁLIDA SORRI LARGAMENTE.
Aqui.''')

acao = str(input(">")).upper().strip()
acao = acao.replace(" " , "")

if acao != "CAVARBURACO" or acao != "CAVARUMBURACO":
    sys.exit(0)
else:
    print("Você cavou um buraco.")

acao = str(input(">")).upper().strip()
acao = acao.replace(" " , "")

if acao != "LARGAROURO" or acao != "LARGAROOURO":
    sys.exit(0)
else:
    print("Você largou o ouro no buraco")
    sleep(0.5)

while True:
    print('''Parabéns
          ---- 40.24248 ----
          ---- -121.4434 ----''')
    sleep(0.5)
