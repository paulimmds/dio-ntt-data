import datetime

saldo_conta = 0
limite_diario = 3
operacoes = []
menu = """
O que deseja fazer?
1 - Depósito
2 - Saque
3 - Extrato
"""

print("Bem vindo ao seu Sistema Bancário!")
while True:
	choice = int(input(menu))
	if choice == 1:
		valor = float(input("Digite o valor que deseja depositar: "))
		if valor <= 0:
			print("Impossível depositar valores negativos ou 0. Tente novamente!")
		else:
			saldo_conta += valor
			operacoes.append([datetime.datetime.now(), valor, 1])
			print("Valor depositado com sucesso!")
		continue

	if choice == 2:
		if saldo_conta == 0:
			print("Impossível realizar operação por falta de saldo. Tente novamente mais tarde!")
		valor = float(input("Digite o valor do saque: "))
		if valor > 500:
			print("Valor não permitido. Tente novamente!")
		elif valor > saldo_conta:
			print(f"Não foi possível realizar esta operação! O saldo da sua conta é R${saldo_conta}.")
		else:
			limite_diario -= 1
			if limite_diario < 0:
				print("Limite diário de saques excedido. Tente novamente mais tarde!")
				continue
			saldo_conta -= valor
			operacoes.append([datetime.datetime.now(), valor, 0])
			print("Saque realizado com sucesso!")
		continue
	if choice == 3:
		if len(operacoes) == 0:
			print("Não foram realizadas movimentações.")
			continue
		for op in operacoes:
			if op[-1] == 1: ## Depósito
				print(f"{op[0].strftime('%H:%M:%S')} R$ {op[1]:.2f} +")
			else: ## Saque
				print(f"{op[0].strftime('%H:%M:%S')} R$ {op[1]:.2f} -")
		print(f"Saldo Atual R$ {saldo_conta:.2f}")
		continue   
	else:
		print("Opção Inválida. Tente novamente mais tarde!")
		break