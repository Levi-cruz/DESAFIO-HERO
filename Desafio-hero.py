import time 
import sys

'''     Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, 
    depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
    Se XP for entre 1.001 e 2.000 = Bronze
        Se XP for entre 2.001 e 5.000 = Prata
            Se XP for entre 5.001 e 7.000 = Ouro
                Se XP for entre 7.001 e 8.000 = Platina
                    Se XP for entre 8.001 e 9.000 = Ascendente
                         XP for entre 9.001 e 10.000= Imortal
                            Se XP for maior ou igual a 10.001 = Radiante
            ## Saída

Ao final deve se exibir uma mensagem:
        "O Herói de nome *{nome}* está no nível de *{level}* ''' 

#InputDO  do nome (heroi)
nameHero =  input("INFORME O NOME DO HÉROI ! ")

#Definição de xp (heroi)
xp = int(input("DETERMINE A QUANTIDADE DE EXPERIÊNCIA DO SEU HÉROI ! "))

level = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]


if xp <= 1000:
    level = level[0]    #ferro

elif xp >= 1001 and xp <= 2000:
    level = level[1]    #bronze 

elif xp >= 2001 and xp <= 5000:
    level = level[2]    #prata

elif xp >= 5001 and xp <= 7000:
    level = level[3]    #ouro

elif xp >= 7001 and xp <= 8000:
    level = level[4]    #platina

elif xp >= 8001 and xp <= 9000:
    level = level[5]    #ascendente

elif xp >= 9001 and xp <= 10000:
    level = level[6]    #imortal

elif xp >= 10001:
    level = level[7]    #radiante

# A função 'sys.stdout.write()' é usada para escrever uma string na saída padrão.
sys.stdout.write("VERIFICANDO")

# A função 'sys.stdout.flush()' é usada para limpar o buffer de saída. 
sys.stdout.flush()

for _ in range(3):  # Número em 'range()'-->  quantos pontos serão impressos.
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)

print(f"\nO Herói de nome {nameHero} está no nível de {level}")