import pandas as pd
import re

# Função para processar cada linha de dados
def process_line(line):

    linhaCerta = line[3:]

    linhaSemAspas = linhaCerta.replace('""', '"')

    linhaArrumada = linhaSemAspas[:-3]

    # expressão regular para encontrar vírgulas seguidas por qualquer caractere que não seja uma aspa dupla ou um dígito
    pattern = r',([^"0-9])'

    # substituir vírgulas por ponto e vírgula quando a condição for atendida
    linhaFinal = re.sub(pattern, r';\1', linhaArrumada)

    return linhaFinal

# o process line retorna uma string

#funcao pra pegar a string gerada no process line e converter em uma lista

#def stringToLista(string):




def organizaCsv():

    file_path = 'C:/Users/andre/Downloads/rym.csv'

    # Ler o arquivo CSV como texto
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    # o lines é o nosso input e o método process_line funciona baseado no input 

    # Supomos que a célula com as colunas está na primeira linha
    column_cell = lines[0] 
    
    print(process_line(lines[1]))

    # Remover as aspas adicionais e dividir a string para obter os nomes das colunas
    columns = column_cell.strip().replace('"', '').split(',')
    # Ignorar o primeiro valor que é duplicado (nesse caso a string vazia)
    columns = columns[1:]

    # Criar uma lista para armazenar as linhas processadas
    processed_data = []

    listaTeste = []
    listaTeste.append(process_line(lines[1]))
    print(listaTeste)

    # Processar cada linha de dados a partir da segunda linha
    for line in lines[1:]:
        processed_line = process_line(line)
        if processed_line and len(processed_line) == len(columns):
            processed_data.append(processed_line)

    # Criar o DataFrame com os dados processados
    df = pd.DataFrame(processed_data, columns=columns)

    # Exibir o DataFrame
    print(df)

def main():
    organizaCsv()

if __name__ == "__main__":
    main()

def linhas_arrumadas(linha):

    Numeros = [1,2,3,4,5,6,7,8,9,0]

    #troca as , do lado dos ints por ;

    #não sei se é assim que seleciona o char específico da string em python 

    for i in linha:
        if (linha[i] == Numeros):
            if (linha[i + 1] == ','):
                linha[i + 1] = ' ; ' #tirar os espaços dps

    #troca os "","" por ; para separar as palavras

    linha.replace(' "","" ' , ' ; ') #tirar os espaços dps

    # aqui era pra tirar as "" que sobraram dps de trocar as "","" entre as palavras, não sei se tem um método só pra tirar, se tiver é melhor usar ele

    linha.replace(' "" ' , ' ') #tirar os espaços dps

    #troca o final de cada linha que é "; por " (basicamente só tirando o ; do final pq estamos usando ele como separador de colunas agora)

    linha.replace(' "; ' , ' " ' ) #tirar os espaços dps 

    return linha