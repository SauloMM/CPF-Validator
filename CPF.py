teste = input("CPF: ") # DIGITE SEU CPF COM OU SEM MÁSCARA
cpf = '{}.{}.{}-{}'.format(teste[:3], teste[3:6], teste[6:9], teste[9:]) # Aplica máscara no valor
if len(teste) <= 11:
    teste = teste.zfill(11)
    print(cpf)

elif len(teste) >11:
    print(teste)
