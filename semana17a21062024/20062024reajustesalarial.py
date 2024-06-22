# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
# colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input("Informe o valor do seu salário atual: R$ "))

if salario_atual <= 280.00:
    aumento = salario_atual * 0.20
    percentual_aumento = "20%"
elif salario_atual > 280.00 and salario_atual < 700.00:
    aumento = salario_atual * 0.15
    percentual_aumento = "15%"
elif salario_atual >= 700.00 and salario_atual < 1500.00: 
    aumento = salario_atual * 0.10
    percentual_aumento = "10%"
else:
    aumento = salario_atual * 0.05
    percentual_aumento = "5%"

novo_salario = salario_atual + aumento

print(f"o salário antes do reajuste: {salario_atual:.2f}\nO percentual de aumento aplicado: {percentual_aumento}\nO valor do aumento: R$ {aumento:.2f}\nO novo salário, após o aumento: R$ {novo_salario:.2f}")
