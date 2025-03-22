
from IPython.display import display
import pandas as pd


def eda_preliminar(df):
    display (df.sample(5))

    print('------------------------')

    print('INFO')  
    display (df.info())
    
    print('------------------------')

    print('NULOS')
    display (round(df.isnull().sum()/df.shape[0]*100,2))
  
    print('------------------------')

    print('DUPLICADOS')
    display (df.duplicated().sum())


    print('------------------------')

    print('DESCRIBE')
    display (df.describe().T)


    print('------------------------')


    print('DESCRIBE COLUMNAS OBJECT')
    display(df.describe(include = 'O').T) 


    print('------------------------')

    print('VALUE COUNTS')
    for col in df.select_dtypes(include = 'O').columns:
        print(df[col].value_counts())
        print('------------------')


    print('------------------------')



def calcular_nulos(df):
    """Devuelve el porcentaje de nulos de cada columna

    Args:
        df (dataframe): dataframe a analizar

    Returns:
        tupla: Dos series de pandas con los datos numéricos de nulos y los datos porcentuales
    """
    numero_nulos = df.isnull().sum()
    porcentaje_nulos = (round(df.isnull().sum()/df.shape[0]*100,2))

    return numero_nulos, porcentaje_nulos



def calcular_solo_col_nul(dataframe, umbral=10):
    #En el umbral lo que le quiero decir a la funcion es, si hay nulos por debajo de un 10% me haces una cosa,
    # y si los nulos están por encima del 10% me haces otra cosa. Lo dejamos en 10% salvo que queramos poner otro valor
    #linea que selecciona solo las columnas con nulos
    columns_with_nulls = dataframe.columns[dataframe.isnull().any()]
    #crear dataframe vacío y le digo que me saque la columna con nulos, el tipo de columna,
    # numero de nulos y su porcentaje de nulos
    null_columns_info = pd.DataFrame(
        {"Column":columns_with_nulls,
         "Datatype":[dataframe[col].dtype for col in columns_with_nulls],
         "NullCount": [dataframe[col].isnull().sum() for col in columns_with_nulls],
         "Null%":[((dataframe[col].isnull().sum()/dataframe.shape[0]) * 100) for col in columns_with_nulls]}
    )

    display(null_columns_info)
    high_null_cols =  null_columns_info[null_columns_info['Null%'] > umbral]['Column'].tolist()
    low_null_cols =  null_columns_info[null_columns_info['Null%'] <= umbral]['Column'].tolist()
    return high_null_cols, low_null_cols



def medidas_tendencia_dispersion(df, col):
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode()[0] if not df[col].mode().empty else None  # Evita errores si no hay moda y coge la primera de haber más de una
    minimo = df[col].min()
    maximo = df[col].max()
    
    print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}, Min: {minimo}, Max: {maximo}")
