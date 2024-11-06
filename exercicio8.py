valor_hora=float(input('Digite o valor da sua hora: '))
horas_trabalhadas=int(input('Digite quantas horas você trabalha: '))
 

#Salário Bruto:
salario_bruto=valor_hora*horas_trabalhadas

#IR Conforme a tabela:
if salario_bruto <= 900:
    ir=0
    percentual_ir=0
elif salario_bruto <= 1500:
    ir=5
    percentual_ir=0.05
elif salario_bruto <= 2500:
    ir=10
    percentual_ir=0.1
else:
    ir = salario_bruto*0.20
    percentual_ir=20

#DescontoINSS 10%
inss=salario_bruto*0.10

#Total de descontos
total_descontos=ir+inss

#Calcular salário líquido
salario_liquido=salario_bruto-total_descontos

#Exibição da tela
print('\n--- Folha de Pagamento---')
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f'(-) IR ({percentual_ir}%): R${ir:.2f}')
print(f'(-) INSS (10%): R${inss:.2f}')
print(f'Total de Descontos: {total_descontos:.2f}')
print(f'Salário Líquido: {salario_liquido:.2f}')






















