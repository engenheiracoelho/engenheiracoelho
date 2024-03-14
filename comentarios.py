#Autor: Leticia 
#Versão: 1.0
#Data: 01/01/2022

#Métodos associados ao calculo de imposto da unidade xpto, que estão direcionados pelo time abc.

#Função para calcular a média de uma lista de números
def calcular_media(lista):
    #Soma os elementos da lista
    soma = sum(lista)
    #Calcula a média
    media = soma / len(lista)
    return media

#Função para verificar se um número é positivo
def verificar_positivo(numero):
    #Verifica se o número é maior que zero
    if numero > 0:
        return True
    else:
        return False

#Função para calcular o quadrado de um número
def calcular_quadrado(numero):
    #Retorna o número multiplicado por ele mesmo
    return numero * numero

#print("Olá, mundo!")

#Exemplo de uso das funções
numeros = [10, 20, 30, 40, 50]
print("Média:", calcular_media(numeros))
print("É positivo?", verificar_positivo(15))
print("Quadrado de 5:", calcular_quadrado(5))
