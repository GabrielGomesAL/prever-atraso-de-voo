import pandas as pd
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from src.utils import save_data

def etl_process():
    df = pd.read_csv(RAW_DATA_PATH)
    
    # Limpeza básica
    df = df.dropna()  # remove linhas nulas
    df['weather'] = df['weather'].str.lower()  # padroniza
    
    # Transformação de features
    df = pd.get_dummies(df, columns=['airline', 'weather'], drop_first=True)
    
    # Salvar
    save_data(df, PROCESSED_DATA_PATH)
    print(f"ETL concluído, dados salvos em {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    etl_process()
