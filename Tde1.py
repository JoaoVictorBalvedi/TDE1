import os
def uniao(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def intersecao(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def diferenca(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def produto_cartesiano(conjunto1, conjunto2):
    return {(x, y) for x in conjunto1 for y in conjunto2}

resultado = []


def calcular(arquivo):
    with open(arquivo, 'r') as f:
        num_operacoes = int(f.readline())
        
        for i in range(num_operacoes):
            operacao = f.readline().strip()
            elementos1 = set(f.readline().strip().split(','))
            elementos2 = set(f.readline().strip().split(','))
            
            if operacao == 'U':
                resultadou = uniao(elementos1, elementos2)
                resultado.append(f'União: Conjunto 1 {elementos1}, Conjunto 2 {elementos2}, Resultado: {resultadou}')
            elif operacao == 'I':
                resultadoi = intersecao(elementos1, elementos2)
                resultado.append(f'Interseção: Conjunto 1 {elementos1}, Conjunto 2 {elementos2}, Resultado: {resultadoi}')
            elif operacao == 'D':
                resultadod = diferenca(elementos1, elementos2)
                resultado.append(f'Diferença: Conjunto 1 {elementos1}, Conjunto 2 {elementos2}, Resultado: {resultadod}')
            elif operacao == 'C':
                resultadoc = produto_cartesiano(elementos1, elementos2)
                resultado.append(f'Produto Cartesiano: Conjunto 1 {elementos1}, Conjunto 2 {elementos2}, Resultado:\n{resultadoc}')
                    
        for i in resultado:
            print(f'{i}\n')



arquivo_txt = input('Digite o nome do arquivo a ser aberto (EX: "arquivo.txt"), ou tecle "ENTER" para ler o arquivo local. \n(Observação : Para a segunda opção, o arquivo deve estar entitulado como: "texto" e estar na mesma pasta do programa).\n')
if arquivo_txt == '':
    calcular("texto.txt")
else:
    calcular(arquivo_txt)