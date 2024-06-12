import pandas as pd
import re

# Função para processar cada linha de dados
def process_line(line):

    linhaCerta = line[3:]

    
    linhaSemAspas = linhaCerta.replace('""', '"')

    linhaFinal = linhaSemAspas[:-3]

    return linhaFinal

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
