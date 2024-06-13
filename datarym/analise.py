import pandas as pd
import re
import csv
import io


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

def stringToLista(string):

    # Usar io.StringIO para tratar a string como um arquivo
    input_string = io.StringIO(string)

    # Usar csv.reader para ler a string
    reader = csv.reader(input_string)

    # Converter a linha lida em uma lista
    fields = next(reader)

    return fields

# o método stringToLista retorna uma lista da linha (string)

def organizaCsv():

    file_path = 'C:/Users/andre/Downloads/rym.csv'

    # Ler o arquivo CSV como texto
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # o lines é o nosso input e o método process_line funciona baseado no input 

    # Supomos que a célula com as colunas está na primeira linha
    column_cell = lines[0] 

    # Remover as aspas adicionais e dividir a string para obter os nomes das colunas
    columns = column_cell.strip().replace('"', '').split(',')
    # Ignorar o primeiro valor que é duplicado (nesse caso a string vazia)
    columns = columns[1:]

    # Criar uma lista para armazenar as linhas processadas
    processed_data = []

    # listaTeste = []
    # listaTeste.append(stringToLista(process_line(lines[1])))
    # print(listaTeste)

    processed_line = []

    for line in lines[1:10]:
        processed_line = stringToLista(process_line(line))
        if processed_line and len(processed_line) == len(columns):
            processed_data.append(processed_line)


    # Processar cada linha de dados a partir da segunda linha

    for line in lines[9:]:
        processed_line = stringToLista(process_line(line))
        processed_line.pop(0)
        if processed_line and len(processed_line) == len(columns):
            processed_data.append(processed_line)


    # Criar o DataFrame com os dados processados
    df = pd.DataFrame(processed_data, columns=columns)

    # Exibir o DataFrame
    print(df)


def inputUsuario(): # botar df de parametro

    print("-" * 30 + " RECOMENDADOR MUSICAL " + "-" *  30)

    escolha = input('Digite um gênero musical:   ')



def main():

    # gerando o dataframe e organizando o csv
    organizaCsv()
    inputUsuario()


if __name__ == "__main__":
    main()

