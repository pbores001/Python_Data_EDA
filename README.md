# Análisis Exploratorio de Datos (EDA) - Campañas de Marketing Bancarias

Este proyecto tiene como objetivo realizar un **análisis exploratorio de los datos** relacionados con las campañas de marketing directo de una institución bancaria portuguesa. Las campañas de marketing se basaron en llamadas telefónicas, y el análisis está orientado a comprender las interacciones con los clientes, sus características y la tasa de conversión a productos bancarios (depósitos a plazo).

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
   - `marital`: El estado civil del cliente.
   - `education`: Nivel educativo del cliente.
   - `default: Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No).
   - `housing`: Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).
   - `loan`: Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).
   - `contact`: El método de contacto utilizado para comunicarse con el cliente.
   - `duration`: La duración en segundos de la última interacción con el cliente.
   - `campaign`: El número de contactos realizados durante esta campaña para este cliente.
   - `pdays`: Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.
   - `previous`: Número de veces que se ha contactado con el cliente antes de esta campaña.
   - `poutcome`: Resultado de la campaña de marketing anterior.
   - `emp.var.rate`: La tasa de variación del empleo.
   - `cons.price.idx`: El índice de precios al consumidor.
   - `cons.conf.idx`: El índice de confianza del consumidor.
   - `euribor3m`: La tasa de interés de referencia a tres meses.
   - `nr.employed`: El número de empleados.
   - `y`: Indica si el cliente ha suscrito un producto o servicio (Sí/No).
   - `date`: La fecha en la que se realizó la interacción con el cliente.
   - `contact_month`: Mes en el que se realizó la interacción con el cliente durante la campaña de marketing.
   - `contact_year`: Año en el que se realizó la interacción con el cliente durante la campaña de marketing.
   - `id_`: Un identificador único para cada registro en el dataset.

2. **Dataset: customer-details.xlsx**  
    - `Income`: Representa el ingreso anual del cliente en términos monetarios.
    - `Kidhome`: Indica el número de niños en el hogar del cliente.
    - `Teenhome`: Indica el número de adolescentes en el hogar del cliente.
    - `Dt_Customer`: Representa la fecha en que el cliente se convirtió en cliente de la empresa.
    - `NumWebVisitsMonth`: Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.
    - `ID`: Identificador único del cliente.

## Archivos

 El repositorio contiene los siguientes archivos y carpetas:

- **Archivo `README.md`**: Descripción de los pasos seguidos durante el proyecto y el informe del análisis.
- **Carpeta `data/`**: Contiene los archivos de datos originales (carpeta 'original_data') y transformados (carpeta 'datos_transformados').
- **Carpeta `src/`**: Contiene el archivo de soporte `sp.limpieza.py`. donde hay funciones usadas en el EDA. 
- **Archivo `eda_python.py`**: Contiene el código del análisis y la visualización de los datos.

## Pasos del Proyecto

### 1. Transformación y limpieza de datos

- **1.1. Importación y visión general de los datos (utilizando la librería Pandas).**
- **1.2. Eliminar las columnas redundantes o irrelevantes.**
- **1.3. Homogeinizar los nombres de las columnas**
- **1.4. Homogeinizar datos categóricos**
- **1.5. Cambio de tipo de datos y gestión de nulos**
- **1.6. Combinar ambas tablas**


### 2. Análisis descriptivo de los datos

- **2.1. Resumen estadístico**.


### 3. Visualización de datos

Aquí se emplearon las librerías de seaborn (https://seaborn.pydata.org/) y matplolib (https://matplotlib.org/)

- **3.1. Histogramas para la distribución de variables numéricas**.
- **3.2. Boxplots para detectar outliers**.
- **3.3. Gráficos de barras para variables categóricas**.
- **3.4. Heatmap de correlaciones**.


### 4. Guarcar archivos limpios

Se guardaron estos archivos generados


## Resultados

### 1. Aceptación del Depósito a Plazo:

Porcentaje de Aceptación: 4.59% de los clientes aceptaron la oferta. Lo que indica que la campaña del banco no fue exitosa. 

1. **Edad de los Clientes:**
   - La edad promedio de los clientes después del ajuste de valores atípicos es de aproximadamente 39.8 años.
   - Se detectaron valores de edad incorrectos (0 años), los cuales fueron reemplazados por la mediana (39 años).
   - Los clientes se distribuyen mayormente entre 19 y 61 años, sin sesgos significativos.

2. **Duración de la última interacción:**
   - La mayoría de las llamadas duran menos de 20 minutos, pero existen valores atípicos de hasta 116 minutos.
   - Estos valores extremos pueden deberse a problemas de registro, clientes indecisos o negociaciones extensas.

3. **Número de interacciones por campaña:**
   - Se identificaron outliers con hasta 42 intentos de contacto.
   - Esto puede explicarse por políticas agresivas de insistencia, dificultades para contactar a los clientes o errores en el registro de datos.

4. **Clientes en campañas previas:**
   - Ninguno de los clientes participó en campañas anteriores, lo que sugiere que la base de datos es exclusiva para el período de 2012-2014.

5. **Cambio en la tasa de empleo:**
   - Presenta una distribución uniforme con valores similares, sin variabilidad extrema.
   - La estabilidad en esta variable podría reflejar condiciones laborales homogéneas durante el período estudiado.

6. **Índice de Precios al Consumidor (Cons_Price_Idx):**
   - Tiene una distribución muy estable con variabilidad reducida.
   - Valores atípicos detectados sugieren momentos económicos puntuales fuera de lo habitual.

7. **Confianza del Consumidor (Cons_Conf_Idx):**
   - Consistentemente negativa, reflejando la crisis económica en Europa durante 2012-2014.
   - La distribución muestra que la percepción negativa fue estable, con ligeras variaciones hacia valores menos pesimistas.

8. **Euribor a 3 meses:**
   - Predominan valores bajos, con cierta dispersión hacia tasas más altas en momentos específicos.
   - La inestabilidad en los valores más altos puede estar relacionada con la lenta recuperación económica en Europa.

9. **Mes y Trimestre de Contacto:**
   - La mayoría de los contactos se realizaron en la segunda mitad del año, con un pico en noviembre.
   - La moda del trimestre es el cuarto, indicando que el banco intensificó sus campañas hacia el cierre del año.
   - Se detectaron valores erróneos en algunos registros de contacto (valor 0).

10. **Ingreso de los Clientes:**
    - La distribución es equilibrada y simétrica, sin sesgos hacia valores muy altos o bajos.
    - La moda está en un rango inferior a la mediana, sugiriendo una presencia significativa de clientes con ingresos más bajos.

11. **Total de Hijos:**
    - Distribución uniforme y simétrica con una moda en 2 hijos.
    - La base de datos muestra un máximo de 4 hijos por cliente.
    - No hay una concentración significativa en valores extremos.

12. **Valores Atípicos y Posibles Errores:**
    - Se detectaron clientes con edad 0, lo que sugiere un error en los datos. Se debería cambiar este valor a "Unknown".
    - La variable Passed_Days_Last_Int tiene un valor constante de 999 en todos los registros, lo que indica que no aporta información útil y podría eliminarse o revisarse.
    - La variable Int_Prior_Campaign tiene valores en su mayoría de 0, indicando que estos clientes no fueron contactados en la campaña anterior.

13. **Relación de clientes propensos a aceptar la oferta:**
    - **Edad:** La mayoría de los clientes tienen entre 30 y 40 años. La edad no parece ser un factor clave en la aceptación, ya que las medianas de edad para los que aceptaron y los que no aceptaron son similares.
    - **Trabajo:** Los clientes retirados tienen una tasa de aceptación mucho más alta (probablemente buscan inversiones seguras), mientras que los estudiantes tienen una tasa de rechazo mucho mayor (debido a ingresos bajos o inestabilidad económica).
    - **Nivel Educativo:** Los clientes con menos estudios tienen una tasa de aceptación más alta, lo que podría deberse a una mayor confianza en el banco o falta de acceso a otras opciones financieras. Los universitarios también muestran mayor aceptación, probablemente por mayor conocimiento financiero o capacidad económica.

14. **Relación de la duración de las llamadas:**
    - **Llamadas exitosas:** Las llamadas exitosas tienden a durar más (más de 4 minutos). Si una llamada dura menos de 4 minutos, la probabilidad de conversión disminuye.
    - **Número de intentos:** Los clientes que aceptan la oferta lo hacen generalmente en los primeros 1-2 intentos. Después de 3 intentos, la probabilidad de conversión disminuye significativamente.

15. **Relación de éxito de la campaña con las condiciones económicas de los clientes:**
    - **Tasa de empleo:** La tasa de empleo parece influir en la decisión de aceptación del depósito. Personas con ciertas tasas de empleo tienen una mayor probabilidad de aceptar la oferta.

16. **Interacción de factores:**
    - **Edad + Educación:** La interacción entre la edad y la educación muestra una mayor diversidad en la aceptación del depósito en algunos niveles educativos, pero en general, la educación no es un factor determinante para la aceptación.
    - **Duración de la llamada + Factores demográficos:** Las llamadas más largas y variadas están asociadas con una mayor probabilidad de aceptación, especialmente en clientes retirados.

**Conclusión General:**
- La base de datos refleja un contexto económico marcado por la crisis de la Eurozona, lo que afectó la confianza de los consumidores y posiblemente la receptividad a los productos financieros ofrecidos.
- La duración de las llamadas y el número de intentos de contacto sugieren que hubo clientes difíciles de convencer, lo que puede haber afectado las tasas de conversión.
- La distribución de los ingresos es diversa, lo que indica que el banco apuntó a una amplia variedad de clientes.
- Las campañas fueron más agresivas en el cuarto trimestre, especialmente en noviembre, posiblemente como estrategia de cierre de año, período ideal para reforzar la relación con los clientes y destacar la marca del banco de cara al próximo año.
- La estabilidad en el índice de precios y el empleo sugiere que las condiciones económicas eran predecibles, pero con un impacto negativo en la confianza de los consumidores, debido al contexto económico global.


