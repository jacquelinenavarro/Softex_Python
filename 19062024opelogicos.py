# O operador 'and' retorna 'True' se todas as expressões booleanas combinadas por ele forem verdadeiras.
#Exemplo:
# idade = 20;
# possui_carta_credito = True

# if idade > 18 and possui_carta_credito:
#     print("Você pode fazer compras online!")

idade = int(input("Digite a sua idade: "))
possui_carta_credito = True

if idade >= 18 and possui_carta_credito:
    print("Você pode fazer compras online!")

else:
    print("Você é menor de idade, logo não poderá realizar compras online.")