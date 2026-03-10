print("-" * 50)
print("Jogo - Pedra, Papel e Tesoura")
print("-" * 50)

'''
Regras do jogo:

- Pedra vence Tesoura
- Tesoura vence Papel
- Papel vence Pedra

'''

#opções de jogada
opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opções de jogada: {opcoes_validas}")

print()


#entrada do usuário
j1 = input("Jogador 1 - Escolha sua mão: ").lower().strip()
if j1 not in opcoes_validas:
    print("Jogada inválida! Tente novamente.")
    exit()
j2 = input("Jogador 2 - Escolha a mão: ").lower().strip()
if j2 not in opcoes_validas:
    print("Jogada inválida! Tente novamente.")
    exit()

print("-" * 50)
print()
print(f"Escolha do jogador 1: {j1}")
print(f"Escolha do jogador 2: {j2}")
print()

print("-" * 50)

#verificacao de vencendor

if j1 == j2:
    print("Empate!")
elif (j1 == "pedra" and j2 == "tesoura")or\
    (j1 == "tesoura" and j2 == "papel")or\
    (j1 == "papel" and j2 == "pedra"):
    print("Jogador 1 VENCEU, Parabéns!")

else:
    print()
    print("Jogador 2 VENCEU, Parabéns!")

print()
print("-" * 50)
