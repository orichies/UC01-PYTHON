# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input(" Login: ")
senha = input( " Senha: ")

while senha == nome:
    senha = input(" Digite Sua Senha Diferente Do Login: ")

else:
    print(f" Login Efetuado! ")    