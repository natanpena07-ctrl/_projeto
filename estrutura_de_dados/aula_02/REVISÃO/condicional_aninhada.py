# SE A IDADE FOR MAIOR OU IGUAL (>=) A 18
    # TEM HABILITAÇÃO?
    # SE TIVER, escreva pode dirigir!
    # SENÃO SE TIVER, escreva: Você precisa de uma habilitação para dirigir.
# SENÃO, escreva Você não tem idade para dirigir.

idade = 20
habilitacao = True

if idade >= 18:
    if habilitacao:
        print("Pode dirigir! 🚙")
    else:
        print("❌ Você precisa de uma habilitação para dirigir")
else:
    print("🤨 Você não tem idade para dirigir.")