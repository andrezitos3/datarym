import pandas as pd
import re
import csv
import io
from time import sleep
from autoChrome import pesquisarBanda


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

    # for da primeira até a nona linha porque por algum motivo ele mostra as dezenas

    for line in lines[1:10]:
        processed_line = stringToLista(process_line(line))
        if processed_line and len(processed_line) == len(columns):
            processed_data.append(processed_line)


    # for a partir da décima linha, excluindo o primeiro index desnecessário

    for line in lines[9:]:
        processed_line = stringToLista(process_line(line))
        processed_line.pop(0)
        if processed_line and len(processed_line) == len(columns):
            processed_data.append(processed_line)


    # Criar o DataFrame com os dados processados
    df = pd.DataFrame(processed_data, columns=columns)

    # Exibir o DataFrame
    # print(df)

    return df

# Função para formatar a string
def formatar_strings_lista_input(s):
    # Inicialmente, definimos o primeiro caractere como maiúsculo
    s = s.capitalize()
    # Iteramos sobre os caracteres da string
    resultado = []
    for i in range(len(s)):
        # Se o caractere atual for um espaço ou hífen, o próximo caractere deve ser maiúsculo
        if s[i] in [' ', '-']:
            resultado.append(s[i])
            if i + 1 < len(s):
                resultado.append(s[i + 1].upper())
        # Caso contrário, apenas adicionamos o caractere atual
        elif i == 0 or s[i-1] not in [' ', '-']:
            resultado.append(s[i])
    # Retornamos a string formatada
    return ''.join(resultado)

# essa funcao deixa a primeira letra da string maiuscula, e depois de um espaco ou um hifen tambem fica maiuscula


def remove_brackets(strings):
    cleaned_strings = []
    for string in strings:
        cleaned_string = re.sub(r'\[.*?\]', '', string)  # Regex para encontrar colchetes e conteúdo entre eles
        cleaned_strings.append(cleaned_string.strip())   # Remover espaços extras que podem ser deixados
    return cleaned_strings

# essa funcao é pra lidar com o possível erro de input com o selenium, quando a wikipedia acaba retornando índices na lista de generos (tira os colchetes)


def inputUsuario(): 

    print("-" * 30 + " RECOMENDADOR MUSICAL " + "-" *  30)

    opcaoinicial = input('deseja escolher uma banda/artista ou digitar gêneros musicais? \n escolha 1 para banda/artista e 2 para generos \n').strip()
    
    listaGen = []

    escolha = ''

    while True:

        if opcaoinicial == '1':
            
            escolha = input("Digite uma banda ou um artista para descobrir álbuns parecidos! \n")
            listaGen = remove_brackets(pesquisarBanda(escolha))
            break

        elif opcaoinicial == '2':
            escolha = input("Digite um ou mais gêneros musicais ---  obs: separe por vírgulas caso seja mais de um \n")
            listaGen = stringToLista(escolha)
            break

        else:
            print('opcao invalida! escolha entre 1 e 2')
            opcaoinicial = input('deseja escolher uma banda/artista ou digitar gêneros musicais? \n escolha 1 para banda/artista e 2 para generos \n').strip()


    print('')

    # Remover espaços no início de cada string
    listaFormat = [s.strip() for s in listaGen]

    # Aplicar a formatação em todas as strings da lista
    lista_final = [formatar_strings_lista_input(s) for s in listaFormat]

    return lista_final

    #print(generos)


def recomenda(df, escolhas):

    generos = df[['release_name','artist_name', 'primary_genres']]

    #verifica se tem o input escolha dentro do DataFrame generos para ver se o genero que o usuario existe 
    #for coluna, generos in generos.items():
    #    print(f'colunas: {coluna}')
    #    print(f'generos: {generos}', sep='\n')
    
    pd.set_option('display.max_rows', None)

    # Filtrando o DataFrame
    mask = generos['primary_genres'].str.contains('|'.join(escolhas), case=False, na=False)
    generos_filtrado = df[mask]

    # print(generos_filtrado[['release_name', 'artist_name', 'primary_genres']])

    return generos_filtrado

# a funcao recomenda gera o dataframe filtrado de acordo com as preferencias do usuario

def sortear(df):

    # Selecionando 10 linhas aleatórias do DataFrame filtrado

    generos_aleatorios = df.sample(n=10)

    print('pesquisando...\n')

    sleep(2)

    print('certo! aqui está 10 albuns de acordo com suas preferências')
    print('-' * 90)
    print(generos_aleatorios[['release_name', 'artist_name', 'primary_genres']])

    
def main():

    print('')

    # gerando o dataframe e organizando o csv
    albuns = organizaCsv()


    while True:

        escolhas = inputUsuario()

        print(f'gêneros musicais identificados: {escolhas}')
        print('')

        try:
            filtro = recomenda(albuns, escolhas)

            if len(escolhas) == 0:
                print("Não achei uma banda/artista com esse nome")

            else:
                sortear(filtro)

        except ValueError:
            print("Não foi possivel identificar o gênero")


        print('-' * 90)

        opcao = input('deseja pesquisar outros albuns? : ')
        if opcao == 'n' or opcao == 'nao' or opcao == 'Nao':
            break

    print('')
    print('encerrando o programa.... até mais!\n')

if __name__ == "__main__":
    main()

