# Lógica de programação python - atividade 1

# Aluna: Jacqueline Navarro da Silva

# Implemente o programa conforme o contexto abaixo:
# Uma nutricionista identificou que seus pacientes não estavam consumindo água em quantidade adequada
# conforme seu peso. Como solução, ela requisitou a um programador o desenvolvimento de um programa. 
# Esse programa precisa conter as seguintes informações dos pacientes: nome, número do WhatsApp, peso e 
# altura. Posteriormente, o programa deve calcular e apresentar o consumo diário recomendado de água para
# cada paciente com base em seu peso. O programa também deve calcular IMC, seguindo as regras abaixo: 
# IMC abaixo de 18.5: Abaixo do peso, IMC entre 18.5 e 24.9: Peso normal, IMC entre 25 e 29.9: Sobrepeso,
# IMC entre 30 e 34.9: Obesidade grau 1 (leve), IMC entre 35 e 39.9: Obesidade grau 2 (moderada) e 
# IMC acima de 40: Obesidade grau 3 (mórbida). Em seguida exibir os resultados.

# Exemplo: Nome: Paulo - Whatsapp - 9 88776655, Peso: 90 - Altura: 1.7 - Consumo de água diário: 2.8 litros
# - IMC: 25 - Nível de obesidade: .Sobrepeso.

# Resolução da Atividade:

nome = input('Digite o nome do paciente: ')
whatsapp = input('Digite o whatsapp do paciente: ') 
peso = float(input('Digite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

imc = peso / (altura ** 2)
consumo_agua = peso * 0.0311

if imc < 18.5:
    nivel = 'Abaixo do peso'
elif imc < 25:
    nivel = 'Peso normal'
elif imc < 30:
    nivel = 'Sobrepeso'
elif imc < 35:
    nivel = 'Obesidade grau 1 (leve)'
elif imc < 40:
    nivel = 'Obesidade grau 2 (moderada)'
else:
    nivel = 'Obesidade grau 3 (mórbida)'

print(f'Nome: {nome} - Whatsapp: {whatsapp}, Peso: {peso}, Altura: {altura}, Consumo de água diário: {consumo_agua:.1f} litros, IMC: {imc:.1f}, Nível: {nivel}.')
