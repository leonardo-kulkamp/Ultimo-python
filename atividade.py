import random

escolhas = ["Pedra", "Papel", "Tesoura"]

sua_escolha= input("Pedra, Papel ou Tesoura? ").lower()
bot = random.choice(escolhas).lower()
print(f"A sua escolha foi: {sua_escolha}")
print(f"O computador escolheu a opção: {bot}")

if sua_escolha == bot:
    print("Viiishhhh, deu empate!")
elif sua_escolha == "pedra" and bot == "tesoura":
        print("Aeeeeeeee,Você ganhou🥳🥳🥳")
elif sua_escolha == "papel" and bot == "pedra":
        print("Aeeeeeeee,Você ganhou🥳🥳🥳")
elif sua_escolha == "tesoura" and bot == "papel":
    print("Aeeeeeeee,Você ganhou🥳🥳🥳")
else:
    print("Que pena, mas na proxima vc consegue.")

          