import pandas as pd

def organizaCsv():
    
    file_path = 'C:/Users/andre/Downloads/rym.csv'

    df = pd.read_csv(file_path, sep='","', engine='python')

    # Configurar o Pandas para mostrar todas as linhas
    pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

    print(df)



def main():
    organizaCsv()

if __name__ == "__main__":
    main()
