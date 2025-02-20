# 0.EXPLORATORY DATA ANALYSIS POINTS

#PREGUNTAS:S

#📌1.¿Cuántos clientes aceptaron el depósito a plazo? 
    # 🔹La variable objetivo suele ser "y", que indica si el cliente suscribió (yes) o no (no) el depósito.
    # 🔹Analizar cuántos dijeron "sí" vs. "no" nos ayuda a ver si los datos están balanceados o desequilibrados.


#📌2.¿Qué tipo de clientes son más propensos a aceptar la oferta?
    # 🔹Edad: ¿Los clientes más jóvenes o mayores aceptan más?
    # 🔹Trabajo: ¿Qué tipo de empleo tienen los clientes que aceptan?
    # 🔹Nivel educativo: ¿Importa el nivel de estudios en la decisión?


#📌3.¿Cuántas llamadas fueron necesarias para convencer a los clientes?
    # 🔹Duración de la última llamada (duration): ¿Las llamadas más largas aumentan la conversión?
    # 🔹Número de contactos (campaign): ¿Cuántas veces fue necesario llamar a un cliente antes de aceptar?


#📌4.¿Influyen las condiciones económicas en la decisión?
    # 🔹Mes de la campaña (month): ¿Hay meses con mejor respuesta?
    # 🔹Tasa de empleo (employment_rate): ¿El contexto económico afectó la decisión?


#📌5.¿Cómo interactúan los factores entre sí? 
    # 🔹¿La combinación de edad + educación influye en la decisión?
    # 🔹¿La duración de la llamada es más efectiva en ciertos grupos de clientes?




#🔸STEP 1: IMPORT PYTHON LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Visualizar todas las columnas
pd.set_option('display.max_columns', None)



#🔸STEP 2: READING DATASET

df_bank = pd.read_csv('bank-additional.csv', index_col = "id_")
df_bank.head(5)



#Ruta archivo del Excel - customer_details
file_path = "customer-details.xlsx"

# Leer todas las hojas (obtenemos un diccionario de DataFrames)
sheets_dict = pd.read_excel(file_path, sheet_name=None)

# Extraemos las hojas y asignamos el año usando 'map' sin bucles explícitos
df_customer_details = pd.concat(
    list(map(lambda df, year: df.assign(bank_registration_year=year), sheets_dict.values(), sheets_dict.keys())), 
    ignore_index=True).set_index("ID")

# Mostrar las primeras filas para verificar
df_customer_details.head()



# ENTENDIENDO LOS DATOS:
    #---columns
    #---shape
    #---dtypes
    #---head
    #---tail
    #---describe
    #---info


# Ver las columnas 
df_customer_details.columns


# Ver numero de filas y columnas 
df_customer_details.shape


# Ver tipo de datos 
df_customer_details.dtypes


# Ver primeras 3 filas
df_customer_details.head(3)


# Ver últimas 3 filas
df_customer_details.tail(3)


# Ver estadísticas generales
df_customer_details.describe()


# Ver detalles
df_customer_details.info()


# Ver las columnas 
df_bank.columns


# Ver numero de filas y columnas 
df_bank.shape


# Ver tipo de datos 
df_bank.dtypes


# Ver primeras 3 filas
df_bank.head(3)


# Ver últimas 3 filas
df_bank.tail(3)


# Ver estadísticas generales
df_bank.describe()


# Ver detalles
df_bank.info()



# 🔸STEP 3: DATA REDUCTION
    # Eliminación de columnas y filas irrelevantes
    # Renombrar columnas
    # Identificación de columnas duplicadas
    # Creación de características
    # Normalizar datos 


# 3.1. Eliminación de columnas y columnas irrelevantes de los dataframes 'df_bank' y 'df_customer' 
df_bank_clean = df_bank.drop(columns=['Unnamed: 0','marital','default','housing','loan','pdays','previous','poutcome'
                                      ,'cons.price.idx','cons.conf.idx','euribor3m','date','latitude','longitude'])


df_customer_details_cln = df_customer_details.drop(columns=['Unnamed: 0','Kidhome', 'Teenhome',
                     'NumWebVisitsMonth'])


# 3.2. Renombrar columnas
df_bank_clean = df_bank_clean.rename(columns={'age':'Customer age',
                              'job':'Job',
                              'education':'Education',
                              'contact':'Contact method',
                              'duration':'Last int duration',
                              'campaign':'Interactions in campaign',
                              'emp.var.rate':'Employment variation rate',
                              'nr.employed':'Employees number',
                              'y':'Product/service subscription',
                              'id_':'ID'
                        })


df_customer_details_cln = df_customer_details_cln.rename(columns={'Income':'Customer annual income',
                                       'Dt_Customer':'Registration date',
                                       'bank_registration_year':'Registration year'})



# 3.3. Identificar valores nulos y manejar missing values
df_bank_clean.isna().sum()



# Para ver el porcentaje de nulos en cada columna del dataframe
(df_bank_clean.isnull().sum()/(len(df_bank_clean)))*100



(df_customer_details_cln.isnull().sum()/(len(df_customer_details_cln)))*100



# Los nulos de 'Age' los sustituyo por la mediana
df_bank_clean['Customer age'].fillna(df_bank_clean['Customer age'].median(), inplace=True)



# Los nulos de 'Job' los sustituyo por la moda
df_bank_clean['Job'].fillna(df_bank_clean['Job'].mode()[0], inplace=True)



# Los nulos de 'Education' los sustituyo por 'Desconocido'
df_bank_clean['Education'].fillna('Desconocido', inplace=True)


# 3.4. Eliminar duplicados 
df_bank_clean = df_bank_clean.drop_duplicates()


df_customer_details_cln = df_customer_details_cln.drop_duplicates()



# 3.4. Normalizar datos

# Convertir a int la edad
def cambiar_a_int(num):
    """Transforma numero en tipo int

    Args:
        num (float or int): numero de argumento

    Returns:
        int: devuelve un numero transformado en int
    """
    return int(num)


df_bank_clean['Customer age'] = df_bank_clean['Customer age'].apply(cambiar_a_int)



# Convertir a palabras legibles el nivel educativo
print(df_bank_clean['Education'].unique())

education_mapping = {'basic.4y':'Basic 4 years', 'high.school':'High School', 'basic.6y':'Basic 6 years',
                     'basic.9y':'Basic 9 years', 'professional.course':'Professional Course',
                     'university.degree':'University Degree', 'illiterate':'Illiterate'}


df_bank_clean['Education'] = df_bank_clean['Education'].replace(education_mapping)



#Convertir 'Employees number' a int

# 1. Reemplazar la coma por un punto
df_bank_clean['Employees number'] = df_bank_clean['Employees number'].str.replace(',', '.')

# 2. Convertir a número decimal (float)
df_bank_clean['Employees number'] = pd.to_numeric(df_bank_clean['Employees number'], errors='coerce')

# 3. Eliminar los valores NaN que se han podido generar.
df_bank_clean = df_bank_clean.dropna(subset=['Employees number'])

# 4. Convertir a entero (int)
df_bank_clean['Employees number'] = df_bank_clean['Employees number'].astype('int')



#Convertir otras columnas con tipo object a category

df_bank_clean['Education'] = df_bank_clean['Education'].astype('category')

df_bank_clean['Job'] = df_bank_clean['Job'].astype('category')

df_bank_clean['Contact method'] = df_bank_clean['Contact method'].astype('category')



#Convertir a numerico los valores de la columna 'Product/service subscription '

df_bank_clean["Product/service subscription"] = df_bank_clean["Product/service subscription"].map({"yes": 1, "no": 0})



df_customer_details_cln['Registration year'] = df_customer_details_cln['Registration year'].astype('int')


# 🔸STEP 4: DATASETS COMBINATION 
    # Combinación de Datasets
    # Limpieza de nulos y duplicados
    # Generar nuevas columnas


#Combinación de los dos DATAFRAMES
df_merged = df_bank_clean.merge(df_customer_details_cln, left_on='id_', right_on='ID', how='left')

df_merged['Registration year'] = df_merged['Registration year'].astype('int')

#Calculo el porcentaje de nulos en cada columna del dataset 'merged'
(df_merged.isnull().sum()/(len(df_merged)))*100


# Sustituir nulos de 'Job' del dataframe 'merged'
df_merged['Job'].fillna(df_merged['Job'].mode()[0], inplace=True)


# Sustituir nulos de 'Education' del dataframe 'merged'
df_merged['Education'].fillna('Desconocido', inplace=True)


#Eliminar duplicados del dataframe 'merged'
df_merged = df_merged.drop_duplicates()


df_merged.isnull().sum()


# Eliminar nulos del dataset 'merged'
df_merged = df_merged.dropna(subset=['Customer annual income'])
df_merged.isnull().sum()



df_merged.head(2)

df_merged.dtypes


#Generar nueva columna del mes en que se contacto al cliente durante la campaña
# Crear una nueva columna 'Interaction month' con el mes en que se realizó la interacción

df_merged['Interaction month'] = df_merged['Registration date'].dt.month_name()

# Verificar los primeros registros
print(df_merged[['Registration date', 'Interaction month']].head())



#🔸STEP 5:GRAPHICS

#Distribucion de la edad
age_ax =sns.histplot(df_merged['Customer age'], bins=20, kde=True, color='salmon')
age_ax.set_title("Distribución de Edad")
plt.show()


plt.figure(figsize=(8, 4))  # Ajusta el tamaño para mejor visibilidad
sns.countplot(x=df_bank['job'], order=df_bank['job'].value_counts().index, palette="coolwarm")
plt.title("Frecuencia de Trabajos")
plt.xticks(rotation=45)  # Rota etiquetas para que sean legibles
plt.show()



#📌1. ¿Cuántos clientes aceptaron el depósito a plazo?

plt.figure(figsize=(5, 4)) 

ax1 = sns.countplot(data=df_merged, x=df_merged['Product/service subscription'].replace({0:'no',1:'yes'}), palette=['salmon','skyblue'])
ax1.set_title('Distribución de clientes que aceptaron el depósito')
ax1.set_xlabel('Aceptó el depósito')
ax1.set_ylabel('Cantidad de clientes')

plt.show(ax1)

#Calculo la media de aceptación del depósito
acceptance_rate = df_merged['Product/service subscription'].mean()*100
print(f'Porcentaje de aceptación:{acceptance_rate:.2f}%')



#📌2. ¿Qué tipo de clientes son más propensos a aceptar la oferta?

# Edad vs. Suscripción
ax2 = sns.boxplot(data=df_merged, x=df_merged['Product/service subscription'].replace({0:'no',1:'yes'}), y="Customer age", palette=['salmon','skyblue'])
ax2.set_title('Edad de clientes según aceptación del depósito')
plt.show()  

# Trabajo vs. Suscripción
ax3 = sns.barplot(data=df_merged, x="Job", y='Product/service subscription', estimator=lambda x: sum(x) / len(x), palette=['salmon','skyblue'], ci=None)
ax3.set_title('Proporción de aceptación por ocupación')
plt.xticks(rotation=45)  # Rotar etiquetas en el eje X
plt.show()  

# Nivel educativo vs. Suscripción
ax4 = sns.barplot(data=df_merged, x="Education", y="Product/service subscription", estimator=lambda x: sum(x) / len(x), palette=['salmon','skyblue'], ci=None)
ax4.set_title('Proporción de aceptación por educación')
plt.xticks(rotation=45)  # Rotar etiquetas en el eje X
plt.show() 



#📌3. ¿Cuántas llamadas fueron necesarias para convencer a los clientes?

# Duración de la llamada vs. Conversión
ax5 =  sns.boxplot(data=df_merged, x=df_merged['Product/service subscription'].replace({0:'no',1:'yes'}), y="Last int duration", palette=['salmon','skyblue'])
ax5.set_title('Duración de llamada según aceptación')
plt.show()

#Número de intentos vs. Conversión
ax6 = sns.boxplot(data=df_bank_clean, x="Product/service subscription", y="Interactions in campaign", palette=['salmon','skyblue'])
ax6.set_title('Número de contactos según aceptación')
plt.show()



#📌4. ¿Influyen las condiciones económicas en la decisión?

# Ajustar el tamaño de la figura para ax7
plt.figure(figsize=(12, 6))  # Puedes cambiar el tamaño a tu preferencia

# Mes de la campaña vs. Tasa de éxito
ax7 = sns.barplot(data=df_merged, x="Interaction month", y="Product/service subscription", estimator=lambda x: sum(x) / len(x), palette=['skyblue','salmon'], ci=None )
ax7.set_title('Tasa de éxito por mes de contacto')
plt.show()

# Ajustar el tamaño de la figura para ax8 (si lo deseas)
plt.figure(figsize=(12, 6))  # También puedes ajustar el tamaño para ax8

# Tasa de empleo vs. Conversión
ax8 = sns.scatterplot(data=df_merged, x="Employment variation rate", y="Product/service subscription",palette=['skyblue','salmon'], alpha=0.5)
ax8.set_title("Tasa de empleo vs. Suscripción")
plt.show()



# Ajustar el tamaño de la figura
plt.figure(figsize=(12, 6))  # Puedes cambiar el tamaño a tu preferencia

# Gráfico usando la columna 'Interaction month'
sns.countplot(data=df_merged, x='Interaction month', palette='coolwarm')

# Agregar título y mostrar
plt.title("Distribución de interacciones por mes")
plt.show()


#📌5. ¿Cómo interactúan los factores entre sí?

# Edad + Educación vs. Suscripción
ax9= sns.boxplot(data=df_merged, x="Education", y="Customer age", hue="Product/service subscription", palette=['salmon','skyblue'])
plt.xticks(rotation=45)
ax9.set_title("Edad y educación vs. aceptación del depósito")
plt.show()

#Duración de llamada en diferentes grupos
ax10 = sns.boxplot(data=df_merged, x="Job", y="Last int duration", hue="Product/service subscription", palette=['salmon','skyblue'])
plt.xticks(rotation=45)
ax10.set_title("Duración de llamada por ocupación y aceptación")
plt.show() 



#Guardar datos transformados

# Crear la carpeta si no existe
ruta_guardado = "datos_transformados"
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los archivos en la carpeta
#df.to_csv(os.path.join(ruta_guardado, 'datos_transformados.csv'), index=False)
df_merged.to_excel(os.path.join(ruta_guardado, 'datos_transformados.xlsx'), index=False)


























































