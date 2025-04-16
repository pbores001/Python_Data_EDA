# IMPORT PYTHON LIBRARIES

#Importamos la slibrerías para hacer el EDA
import numpy as np
import pandas as pd

#Importo librería sys para añadir un 'path' a todo lo que escribamos.
#Es decir, para poder llamar a archivos de otras carpetas
import sys 
sys.path.append("..")

#Después importamos el archivo de funciones ('sp_limpieza.py') gracias a 'sys'
import src.sp_limpieza as sp
#Importamos importlib para poder recargar el módulo y reflejar los cambios actualizados
import importlib  
importlib.reload(sp) 

#Importamos funciones para interactuar con el sistema operativo
import os


#Librerías visualización de gráficos
import matplotlib.pyplot as plt
import seaborn as sns


#Visualizar todas las columnas
pd.set_option('display.max_columns', None)



# 1. Transformación y limpieza de datos

### 1.1. Importación y visión general de los datos

# LEER EL DATASET (bank information)

#Cargamos el primer archivo dentro de un dataframe le quitamos la columna 'Unnamed'
df_bank = pd.read_csv(r"data\original_data\bank-additional.csv", index_col = 0)


#Cargamos el segundo archivo dentro de un dataframe le quitamos la columna 'Unnamed'
df_customer = pd.read_excel(r"data\original_data\customer-details.xlsx", index_col= 0)



#Importamos la información general del dataset 'df_bank'

sp.eda_preliminar(df_bank)

#INFO
    # Aquí se pueden ver los nulos que hay en cada columna teniendo en cuenta el numero de datos en cada una,
    # respecto a las 43000 entries que presenta el dataframe. 
    # Por ejemplo, la columna 'age' tiene 37880 datos del total de 43000 entradas

#NULOS
    # Donde hay una cantidad notable de nulos es en las columnas 'Default_On_Payments' y 'Euribor_3_Months'.
    # Dado que ambas variables tienen más del 20% de valores nulos, eliminar esas filas significaría
    # perder una gran cantidad de información. Por lo tanto, la mejor opción es imputar los valores nulos.

#DUPLICADOS
    # No hay duplicados

#DESCRIBE
    # Para aquellas columnas int o float, las object o categoy no se incluyen en esta visualizacion
    # Aquí podemos ver los tipos de datos booleanos que serían 'default, housing y loan'.
    # Lo conveniente sería convertir los 1 por Sí, y los 0 por No -----> 1:Si,0:No

#DESCRIBE COLUMNAS OBJECT
    # Con esta sintaxis veo las estadísticas de los datos que son objetos





#Importamos la información general del dataset 'df_customer'

sp.eda_preliminar(df_customer)

#INFO
    #Vemos los tipos de datos por columna y los no nulos de 20115 entradas

#NULOS
    # No hay nulos

#DUPLICADOS
    # No hay duplicados

#DESCRIBE
    #Para aquellas columnas int o float, las object o category no se incluyen en esta visualizacion
    #Aquí podemos ver que no hay de datos booleanos.
    #Lo conveniente sería convertir Dt_Customer a antigüedad del cliente. 

#DESCRIBE COLUMNAS OBJECT
    #No hay datos de tipo objeto, ya que la fecha de antigëdad de los clientes esta correctamente catalogada como datetime.





### 1.2. Eliminar columnas redundantes o irrelevantes

df_bank.columns


df_bank.head(3)


#Eliminación de columnas irrelevantes de los dataframes

#Las columnas 'latitude' y 'longitude' las eliminamos ya que el análisis trata sobre campañas de marketing telefónicas
#de una institución bancaria para promocionar depósitos a plazo.
#Nos centramos en comportamientos de respuesta, canales de contacto, y características personales o económicas.
#Además para poder un análisis con variables geográficas harían falta más referencias geográficas o contexto (como ciudad, región),
#como saber cada punto del mapa que representa (urbano, rural, norte, sur...).
if 'latitude' in df_bank.columns and 'longitude' in df_bank.columns:
    df_bank = df_bank.drop(columns=['latitude', 'longitude'])

# Verificar que las columnas ya no estén
print(df_bank.columns)




### 1.3. Homogeinizar los nombres de las columnas

df_bank.columns


# Renombrar solo las columnas para hacerlas más intuitivas
df_bank = df_bank.rename(columns={
    'marital': 'marital_status', 
    'default': 'default_on_payments',
    'duration': 'last_int_duration', 
    'campaign': 'int_nr_campaign',
    'pdays': 'passed_days_last_int', 
    'previous': 'int_prior_campaign',
    'poutcome': 'last_campaign_outcome', 
    'emp.var.rate': 'rate_change_employment',
    'cons.price.idx': 'cons_price_idx', 
    'cons.conf.idx': 'cons_conf_idx',
    'euribor3m': 'euribor_3_months', 
    'nr.employed': 'nr_employed',
    'y': 'product_or_service'
})

# Aplicar la funcion title() a todos los nombres de columnas para estandarizar los nombres
#Colocamos de nuevo los nombres de las columnas con '_' por si se pasará el archivo a otros programas y hubiera errores de lectura
df_bank.columns = [col.replace('_', ' ').title().replace(' ', '_') for col in df_bank.columns]

# Mostrar los nombres para verificar
print(df_bank.columns)


df_customer.columns

# Renombrar solo las columnas para hacerlas más intuitivas
df_customer = df_customer.rename(columns={
    'Dt_Customer': 'customer_seniority'
})

# Aplicar la funcion title() a la columnas para estandarizar los nombres
df_customer.columns = [col.replace('_', ' ').title().replace(' ', '_') for col in df_customer.columns]

# Mostrar los nombres para verificar
print(df_customer.columns)



### 1.4. Homogeinizar datos categóricos

#Poner los datos de las columnas en minusculas los valores de las columnas que sean de tipo object/string.
for col in df_bank.select_dtypes(include= 'O').columns:
    df_bank[col] = df_bank[col].str.lower()
#df_bank[col] accede a los valores dentro de la columna, no al nombre.
#Si accedes a df_bank.columns, estás modificando los nombres de las columnas.
#Si accedes a df_bank[col] (sin .columns), estás modificando los valores dentro de la columna.
   

df_bank.sample(4)


### 1.5. Cambio tipo de datos y gestión de nulos

meses = {'enero': '01',
         'febrero': '02',
         'marzo': '03',
         'abril': '04',
         'mayo': '05',
         'junio': '06',
         'julio': '07',
         'agosto': '08',
         'septiembre': '09',
         'octubre': '10',
         'noviembre': '11',
         'diciembre': '12'}

df_bank.replace({'Date': meses}, regex=True, inplace=True)


#Después de esa conversión a formato fecha automaticamente se almacena internamente en un formato estándar de fecha (YYYY-MM-DD), que es el formato anglosajón.
# Lo dejamos así dando que los nombres y valores de las columnas están en inglés.
df_bank['Date'] = pd.to_datetime(df_bank['Date'], format = "%d-%m-%Y")



df_bank.sample(4)


df_bank.dtypes
#Comprobamos que Date es de tipo datetime




#Recoger aquellas columnas que deberían de ser float pero que son object

str_float = ['Cons_Price_Idx','Cons_Conf_Idx','Euribor_3_Months','Nr_Employed']
#convertir los valores object con ',' con '.' para poder transformarlos a float despues
for col in str_float:
    df_bank[col] = df_bank[col].str.replace(',','.')
    df_bank[col] = df_bank[col].apply(lambda x: float(x))

df_bank.dtypes


#Imputamos los nulos de Age por la mediana por ser una medida robusta frente a outliers y
# adecuada para variables numéricas con posible sesgo.
df_bank['Age'] = df_bank['Age'].fillna(df_bank['Age'].median())


#Ahora podemos pasar los valores de Age y Nr_Employed a int. No podíamos convertir la variable Age a integer float NaN a integer
str_int = ['Age', 'Nr_Employed']

for col in str_int:
    df_bank[col] = df_bank[col].apply(lambda x: int(x))



df_bank.dtypes

df_bank.head(5)



# Pasar a booleanos -----------> 1:Si,0:No
diccionario_mapeo = {1:'Yes', 0:'No'}
obj_bool = ['Default_On_Payments','Housing','Loan']

for col in obj_bool:
    df_bank[col] = df_bank[col].map(diccionario_mapeo)

df_bank.sample(3)



#Convertir a numerico los valores de la columna 'Product/service subscription '
df_bank["Product_Or_Service"] = df_bank["Product_Or_Service"].map({"yes": 1, "no": 0})



# Imputamos los valores nulos en 'Education' con 'unknown' porque se trata de una variable categórica, 
# y no queremos eliminar registros ni asignar un valor arbitrario que distorsione el análisis.
df_bank['Education'].fillna('unknown', inplace=True)



# Convertir a palabras legibles el nivel educativo
print(df_bank['Education'].unique())

education_mapping = {'basic.4y':'basic 4 years', 'high.school':'high school', 'basic.6y':'basic 6 years',
                     'basic.9y':'basic 9 years', 'professional.course':'professional course',
                     'university.degree':'university degree', 'illiterate':'illiterate'}


df_bank['Education'] = df_bank['Education'].replace(education_mapping)




# Función para reemplazar espacios con '_' en este caso para la columna Education
def quitar_espacios(df, col):
    df[col] = df[col].str.replace(' ', '_', regex=True)

# Aplicar la función a la columna 'Education'
quitar_espacios(df_bank, 'Education')

# Verificar cambios
print(df_bank['Education'].unique())



#Crear nuevas columnas a partir de la columna de Date

# Creamos variables temporales derivadas de 'Date' para analizar patrones de contacto por año.
# Esto puede ayudarnos a identificar cuales fueron los años más efectivos para la campaña.
df_bank['Contact_Year'] = df_bank['Date'].dt.year
df_bank['Contact_Year'] = df_bank['Contact_Year'].fillna(0).apply(lambda x: int(x))


#Sacamos mes de interaccion con el cliente durante la campaña
df_bank['Contact_Month'] = df_bank['Date'].dt.month
df_bank['Contact_Month'] = df_bank['Contact_Month'].fillna(0).apply(lambda x: int(x))


#Sacamos el día de la semana
df_bank['Contact_Day'] = df_bank['Date'].dt.day_name()


df_bank.dtypes


# Creamos variables temporales derivadas de 'Date' para analizar patrones de contacto por trimestre.
# Esto puede ayudarnos a identificar periodos más efectivos para la campaña.
df_bank['Quarter'] = df_bank['Date'].dt.quarter
df_bank['Quarter'] = df_bank['Quarter'].fillna(0).apply(lambda x: int(x))

df_bank.head(3)

df_customer


#Creamos una nueva columna donde ponga el total de hijos de los clientes independientemente de su edad.
#Interesa saber si tienen hijos o no y cuantos.
df_customer['Total_Children'] = df_customer['Kidhome'] + df_customer['Teenhome']
df_customer.drop(['Kidhome','Teenhome'], axis=1, inplace=True)

#calcular los dias de antigüedad que tienen los clientes desde 2012 al último día de 2014,
# ya que la información de los clientes es de 2012, 2013 y 2014. 
fecha_limite = pd.to_datetime('2014-12-31')

# Filtrar solo las filas donde la fecha de antigüedad es antes de 2015
df_customer = df_customer[df_customer['Customer_Seniority'] < '2015-01-01']

# Calculamos los días de antigüedad de los clientes desde su fecha de alta hasta el 31-12-2014 
# porque es el periodo de tiempo en el que se desarrollaron las campañas de marketing.
df_customer['Customer_Seniority_Days'] = (fecha_limite - df_customer['Customer_Seniority']).dt.days

# Ver los primeros resultados
df_customer[['Customer_Seniority', 'Customer_Seniority_Days']].head()


df_customer


#Teniendo en cuenta que las columnas 'Default_On_Payments' y 'Euribor_3_Months' tienen un porcentaje alto de nulos
# vamos a imputarlos ya que son columnas de información importante para el EDA, y su porcentaje de nulos es alto. 

#Pasamos los nulos de la columna de tasa de interés de referencia a 3 meses de los clientes a la mediana ya que son numéricos
# Usamos la mediana para mantener la distribución real de los datos. No introducir un sesgo artificial como lo haría la media.
df_bank['Euribor_3_Months'].fillna(df_bank['Euribor_3_Months'].median(), inplace=True)

#Pasamos los nulos de la columna de impagos de los clientes a la moda ya que son datos categóricos. 
# Si hay un nulo, es probable que la persona no tenga impago registrado (porque si lo tuviera, estaría en la base de datos).
# Para evitar perder datos y mantener la coherencia, los nulos se rellenan con "No", asumiendo que la mayoría no tiene impagos.
df_bank['Default_On_Payments'].fillna("No", inplace=True)  



#Aquí asignamos los valores de la definicion 'calcular_nulos' para el dataframe df_bank.   
#De esta manera podemos elegir si ver los nulos enteros o nulos porcentuales del dataframe deseado
numero_nulos_df_limpio ,porcentaje_nulos_df_limpio = sp.calcular_nulos(df_bank)

sp.calcular_nulos(df_bank)


porcentaje_nulos_df_limpio
#Ya no quedan nulos significantes


### 1.6. Combinar ambas tablas

# Ver la cantidad de IDs únicos en cada dataset
print(f"Total IDs en df_bank: {df_bank['Id_'].nunique()}")
print(f"Total IDs en df_customer: {df_customer['Id'].nunique()}")

# Ver cuántos IDs en df_bank existen en df_customer
common_ids = set(df_bank["Id_"]).intersection(set(df_customer["Id"]))
print(f"Número de IDs en común: {len(common_ids)}")


#Hacemos un merge de los dos datasets haciendo que el ID de clientes en mabas tablas sea el nexo de unión. 
#Queremos evaluar los clientes identificados rn el dataset de 'df_bank' ya que necesitamos valorar la campaña de marketing
# en funcion de sus características demográficas, como el ingreso anual, antiguedad y cantidad de hijos.
df_inner = df_bank.merge(df_customer, left_on="Id_", right_on="Id", how="inner")

df_inner


# Verificamos que la columna id de las dos tablas tengan el mismo tipo de dato. 
print(df_bank.dtypes, df_customer.dtypes)
#Las dos son str

df_inner_nulos_enteros, df_inner_nulos_porcentuales = sp.calcular_nulos(df_inner)

df_inner_nulos_porcentuales

#Eliminamos la columna duplicada de 'Id_' en el dataframe para que no nos salga dos veces
df_inner = df_inner.drop(columns=['Id_'])  # Elimina 'Id_', dejando solo 'Id'

df_inner


# Mover la columna 'Id' al final
cols = [col for col in df_inner.columns if col != 'Id']  # Lista sin 'Id'
cols.append('Id')  # Agregar 'Id' al final
df_inner = df_inner[cols]  # Reordenar columnas

df_inner.sample(4)


# 2. Análisis descriptivo de los datos

### 2.1. Resumen estadístico

#Ver estadísticas numéricas
df_inner.describe().T

#Ver estadísticas categóricas
df_inner.describe(include='O').T

# 3. Visualización de los datos.

### 3.1. Histogramas para la distribución de variables numéricas

#3.1. Distribución de variables numéricas
df_selected = df_inner.drop(['Date', 'Contact_Year', 'Customer_Seniority'], axis=1)
df_selected.hist(figsize=(12, 8), bins=30)
plt.xticks(rotation=45)
plt.tight_layout() # Ajustar automáticamente los elementos para que no se solapen los textos
plt.show()

#Para las columnas numéricas ponemos estos graficos menos en las columnas abajo mencionadas
#ya que no son muy representativas


### 3.2. Boxplots para detectar outliers

# Boxplots - Para detectar outliers
num_cols = df_inner.select_dtypes(include=['number']).columns  # Selección de variables numéricas
fig, axes = plt.subplots(nrows=len(num_cols) // 3 + 1, ncols=3, figsize=(15, 5 * (len(num_cols) // 3 + 1)))
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.boxplot(data=df_inner, x=col, ax=axes[i])
    axes[i].set_title(f'Boxplot de {col}')
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45)

for j in range(i + 1, len(axes)):  # Ocultar gráficos vacíos
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

#Aquí vemos que el porcentaje de nulos de las columnas con nulos son bajos, que no existen columnas con nulos de mas del 10% de umbral. 
high_null_cols, low_null_cols = sp.calcular_solo_col_nul(df_inner)

print(df_inner['Age'].describe())

df_inner['Age'].median()

print(df_inner['Cons_Price_Idx'].describe())

print(df_inner['Euribor_3_Months'].describe())

print(df_inner['Contact_Month'].describe())

print(df_inner['Quarter'].describe())

print(df_inner['Income'].describe())

print(df_inner['Numwebvisitsmonth'].describe())

print(df_inner['Total_Children'].describe())

print(df_inner['Customer_Seniority_Days'].describe())


### 3.3. Gráficos de barras para variables categóricas

# Principales variables categóricas
categorical_columns = ['Job', 'Marital_Status', 'Education', 'Default_On_Payments', 'Housing', 'Loan',
                       'Contact', 'Last_Campaign_Outcome', 'Product_Or_Service', 'Contact_Day']

fig, axes = plt.subplots((len(categorical_columns) + 2) // 3, 3, figsize=(15, 5 * ((len(categorical_columns) + 2) // 3)))
axes = axes.flatten()

for i, col in enumerate(categorical_columns):
    sns.countplot(data=df_inner, x=col, ax=axes[i], hue=col, legend=False)
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45, ha="right")

for j in range(i + 1, len(axes)):  # Ocultar gráficos vacíos
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()



#Clientes aceptaron el depósito a plazo
plt.figure(figsize=(5, 4)) 

ax1 = sns.countplot(data=df_inner, x=df_inner['Product_Or_Service'].replace({0:'no',1:'yes'}), palette=['salmon','skyblue'])
ax1.set_title('Distribución de clientes que aceptaron el depósito')
ax1.set_xlabel('Aceptó el depósito')
ax1.set_ylabel('Cantidad de clientes')

plt.show(ax1)

#Calculo la media de aceptación del depósito
acceptance_rate = df_inner['Product_Or_Service'].mean()*100
print(f'Porcentaje de aceptación:{acceptance_rate:.2f}%')



# Clientes más propensos a aceptar la oferta según:

# Edad vs. Suscripción
ax2 = sns.boxplot(data=df_inner, x=df_inner['Product_Or_Service'].replace({0:'no',1:'yes'}), y="Age", palette=['salmon','skyblue'])
ax2.set_title('Edad de clientes según aceptación del depósito')
plt.show()  

# Trabajo vs. Suscripción
ax3 = sns.barplot(data=df_inner, x="Job", y='Product_Or_Service', estimator=lambda x: sum(x) / len(x), palette=['salmon','skyblue'], ci=None)
ax3.set_title('Proporción de aceptación por ocupación')
plt.xticks(rotation=45)  # Rotar etiquetas en el eje X
plt.show()  

# Nivel educativo vs. Suscripción
ax4 = sns.barplot(data=df_inner, x="Education", y="Product_Or_Service", estimator=lambda x: sum(x) / len(x), palette=['salmon','skyblue'], ci=None)
ax4.set_title('Proporción de aceptación por educación')
plt.xticks(rotation=45)  # Rotar etiquetas en el eje X
plt.show() 



# Llamadas necesarias para convencer a los clientes

# Duración de la llamada vs. Conversión
ax5 =  sns.boxplot(data=df_inner, x=df_inner['Product_Or_Service'].replace({0:'no',1:'yes'}), y="Last_Int_Duration", palette=['salmon','skyblue'])
ax5.set_title('Duración de llamada según aceptación')
plt.show()

#Número de intentos vs. Conversión
ax6 = sns.boxplot(data=df_bank, x="Product_Or_Service", y="Int_Nr_Campaign", palette=['salmon','skyblue'])
ax6.set_title('Número de contactos según aceptación')
plt.show()



#Condiciones económicas que pueden favorecer a aceptar la decisión

# Ajustar el tamaño de la figura para ax7
plt.figure(figsize=(12, 6))  # Puedes cambiar el tamaño a tu preferencia

# Mes de la campaña vs. Tasa de éxito
ax7 = sns.barplot(data=df_inner, x="Contact_Month", y="Product_Or_Service", estimator=lambda x: sum(x) / len(x), palette=['skyblue','salmon'], ci=None )
ax7.set_title('Tasa de éxito por mes de contacto')

# Mostrar el gráfico
plt.show()

# Ajustar el tamaño de la figura para ax8 (si lo deseas)
plt.figure(figsize=(12, 6))  # También puedes ajustar el tamaño para ax8

# Tasa de empleo vs. Conversión
ax8 = sns.scatterplot(data=df_inner, x="Rate_Change_Employment", y="Product_Or_Service",palette=['skyblue','salmon'], alpha=0.5)
ax8.set_title("Tasa de empleo vs. Suscripción")

# Mostrar el gráfico
plt.show()


# Analizar la interacción entre edad y educación
ax9= sns.boxplot(data=df_inner, x="Education", y="Age", hue="Product_Or_Service", palette=['salmon','skyblue'])
plt.xticks(rotation=45)
ax9.set_title("Edad y educación vs. aceptación del depósito")
plt.show()


# Analizar la llamada en diferentes grupos de clientes según el tipo de trabajos
ax10 = sns.boxplot(data=df_inner, x="Job", y="Last_Int_Duration", hue="Product_Or_Service", palette=['salmon','skyblue'])
plt.xticks(rotation=45)
ax10.set_title("Duración de llamada por ocupación y aceptación")
plt.show() 



### 3.4. Heatmap de correlaciones

# Heatmap de correlaciones sin las columnas 'Passed_Days_Last_Int' y 'Int_Prior_Campaign' ya que no son representativas para el analisis
plt.figure(figsize=(12, 8))
corr_matrix = df_inner.drop(columns=['Passed_Days_Last_Int', 'Int_Prior_Campaign']).select_dtypes(include='number').corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm_r", fmt=".2f")
# Invertimos la escala de colores con 'coolwarm_r', para poner altos valores en azul y bajos en rojo
plt.show()



# 4. Guardar archivos limpios

#Guardar la tabla df_bank
df_bank.to_csv(r"data\datos_transformados\campana_marketing_banco_limpio.csv", index = False)

# Guardar la tabla de clientes
df_customer.to_csv(r"data\datos_transformados\customer_details_limpio.csv", index = False)

# Guardar la tabla unida de datos del banco y sus clientes
df_inner.to_csv(r"data\datos_transformados\bank_customers_limpio.csv", index = False)

