import time 

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
        "O Herói de nome *{nome}* está no nível de *{nivel}* ''' 

#InputDO  do nome (heroi)
nome_heroi =  input("INFORME O NOME DO HÉROI ! ")

#Definição de xp (heroi)
xp = int(input("DETERMINE A QUANTIDADE DE EXPERIÊNCIA DO SEU HÉROI ! "))

nivel = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]


if xp <= 1000:
    nivel = nivel[0]    #ferro

elif xp >= 1001 and xp <= 2000:
    nivel = nivel[1]    #bronze 

elif xp >= 2001 and xp <= 5000:
    nivel = nivel[2]    #prata

elif xp >= 5001 and xp <= 7000:
    nivel = nivel[3]    #ouro

elif xp >= 7001 and xp <= 8000:
    nivel = nivel[4]    #platina

elif xp >= 8001 and xp <= 9000:
    nivel = nivel[5]    #ascendente

elif xp >= 9001 and xp <= 10000:
    nivel = nivel[6]    #imortal

elif xp >= 10001:
    nivel = nivel[7]    #radiante

print("VERIFICANDO ...")
time.sleep(1)

print(f"O Herói de nome {nome_heroi} está no nível de {nivel}")