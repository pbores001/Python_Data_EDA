# Análisis Exploratorio de Datos (EDA) - Campañas de Marketing Bancarias

Este proyecto tiene como objetivo realizar un **análisis exploratorio de los datos** relacionados con las campañas de marketing directo de una institución bancaria portuguesa. Las campañas de marketing se basaron en llamadas telefónicas, y el análisis está orientado a comprender las interacciones con los clientes, sus características y la tasa de conversión a productos bancarios (depósitos a plazo).

## Objetivo del Proyecto

El objetivo principal del proyecto es aplicar los conocimientos adquiridos en el módulo "Python for Data" para realizar un análisis exploratorio de datos utilizando **Python**, **Pandas** y **Visual Studio Code**. Se busca transformar, limpiar, analizar y visualizar los datos con el fin de extraer insights útiles para la toma de decisiones en el contexto de las campañas de marketing bancarias.

## Requisitos del Proyecto

Para completar este proyecto, se deben cubrir los siguientes puntos:

- **Transformación y limpieza de los datos**: Identificar y corregir datos erróneos, manejar los datos faltantes y realizar las modificaciones adecuadas en las columnas y tipos de datos.
- **Análisis descriptivo de los datos**: Utilizar estadísticas descriptivas para describir las principales características de los datos, como medias, medianas, desviaciones estándar, correlaciones, etc.
- **Visualización de los datos**: Crear gráficos significativos utilizando librerías como `matplotlib`, `seaborn`, etc., para ilustrar patrones y relaciones importantes.
- **Informe explicativo**: Presentar un informe con los hallazgos y conclusiones basadas en el análisis realizado.

## Herramientas Utilizadas

Este proyecto ha sido realizado utilizando las siguientes herramientas:

- **Python**: Lenguaje de programación utilizado para el análisis y manipulación de los datos.
- **Pandas**: Librería principal para la manipulación de datos y análisis.
- **Visual Studio Code**: Editor de código utilizado para escribir y ejecutar los scripts de Python.

## Datos

Los datos utilizados en este proyecto provienen de dos fuentes principales:

1. **Dataset: bank-additional.csv**  
   Este archivo contiene datos sobre las interacciones de los clientes con el banco durante las campañas de marketing telefónico. Las columnas principales son:
   - `age`: Edad del cliente.
   - `job`: Ocupación del cliente.
   - `education`: Nivel educativo del cliente.
   - `contact`: Método de contacto utilizado.
   - `duration`: Duración de la última interacción.
   - `campaign`: Número de contactos realizados durante la campaña.
   - `y`: Indicador de si el cliente ha suscrito el producto (Sí/No).
   - Entre otras columnas relacionadas con el comportamiento y situación del cliente.

2. **Dataset: customer-details.xlsx**  
   Este archivo contiene información adicional sobre los clientes, como sus ingresos anuales, la cantidad de niños y adolescentes en su hogar, entre otros.

## Método de Entrega

El proyecto será entregado a través de un repositorio público de GitHub. El repositorio debe contener los siguientes archivos y carpetas:

- **Archivo `README.md`**: Este archivo, que describe los pasos seguidos durante el proyecto y el informe del análisis.
- **Carpeta `data/`**: Contendrá los archivos de datos originales y transformados.
- **Carpeta `notebooks/` o `scripts/`**: Contendrá los archivos Python o Jupyter notebooks utilizados para el análisis y visualización de los datos.

## Pasos del Proyecto

### 1. Carga de los Datos

Los datos fueron cargados desde los archivos proporcionados utilizando la librería **Pandas**.

### 2. Transformación y Limpieza de los Datos

En esta fase, se llevaron a cabo las siguientes tareas:

- **Identificación y tratamiento de valores faltantes**.
- **Conversión de columnas a los tipos de datos adecuados**.
- **Creación de nuevas columnas** para facilitar el análisis, como el mes de interacción con el cliente.
- **Filtrado y eliminación de registros duplicados o incorrectos**.

### 3. Análisis Descriptivo

Se realizaron análisis estadísticos para describir los datos, incluyendo:

- **Medias, medianas y desviaciones estándar** de variables como la edad, la duración de las llamadas y los ingresos.
- **Distribución de la variable de interés** (si el cliente ha aceptado el depósito o no).
- **Correlaciones** entre variables numéricas.

### 4. Visualización de los Datos

Se generaron gráficos con **matplotlib** y **seaborn** para ilustrar los patrones en los datos, como:

- **Distribución de la edad** y su relación con la aceptación del depósito.
- **Duración de las interacciones** por tipo de cliente (suscripción/no suscripción).
- **Relación entre el número de interacciones** y la conversión a producto.


## Resultados

### 1. Aceptación del Depósito a Plazo:

Porcentaje de Aceptación: 11.34% de los clientes aceptaron la oferta.

### 2. Clientes Propensos a Aceptar la Oferta:
- **Edad:** La mayoría de los clientes tienen entre 30 y 40 años. La edad no parece ser un factor clave en la aceptación, ya que las medianas de edad para los que aceptaron y los que no aceptaron son similares.
- **Trabajo:** Los clientes retirados tienen una tasa de aceptación mucho más alta (probablemente buscan inversiones seguras), mientras que los estudiantes tienen una tasa de rechazo mucho mayor (debido a ingresos bajos o inestabilidad económica).
- **Nivel Educativo:** Los analfabetos tienen una tasa de aceptación más alta, lo que podría deberse a una mayor confianza en el banco o falta de acceso a otras opciones financieras. Los universitarios también muestran mayor aceptación, probablemente por mayor conocimiento financiero o capacidad económica.
### 3. Duración de las Llamadas:
- **Llamadas Exitosas:** Las llamadas exitosas tienden a durar más (más de 4 minutos). Si una llamada dura menos de 4 minutos, la probabilidad de conversión disminuye.
- **Número de Intentos:** Los clientes que aceptan la oferta lo hacen generalmente en los primeros 1-2 intentos. Después de 3 intentos, la probabilidad de conversión disminuye significativamente.
### 4. Condiciones Económicas:
- **Tasa de Empleo:** La tasa de empleo parece influir en la decisión de aceptación del depósito. Personas con ciertas tasas de empleo tienen una mayor probabilidad de aceptar la oferta.
### 5. Interacción de Factores:
- **Edad + Educación:** La interacción entre la edad y la educación muestra una mayor diversidad en la aceptación del depósito en algunos niveles educativos, pero en general, la educación no es un factor determinante para la aceptación.
- **Duración de la Llamada + Factores Demográficos:** Las llamadas más largas y variadas están asociadas con una mayor probabilidad de aceptación, especialmente en clientes retirados.
