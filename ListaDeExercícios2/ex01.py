import random

def JogoAdivinhacao():
    numero_secreto = random.randint(1, 100)
    
    while True:
        palpite = int(input("Tente adivinhar o número entre 1 e 100: "))
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!:", numero_secreto)
            break
        elif palpite < numero_secreto:
            print("Você está frio. Tente novamente.")
        else:
            print("Você está quente. Tente novamente.")

JogoAdivinhacao()