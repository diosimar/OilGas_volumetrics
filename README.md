![analytics](https://img.shields.io/badge/Machine%20Learning-Oil%20inplace-green)

# Oil & Gas volumetrias ( OIP)

# Introducción 👇


<p style='text-align: justify;'>

El sector upstream de la industria del petróleo y el gas, a veces denominado exploración y producción (o E&P), se ocupa de localizar yacimientos para la extracción de petróleo y gas y la posterior perforación, recuperación y producción de crudo y gas natural. La producción de petróleo y gas es una industria increíblemente intensiva en capital, que requiere el uso de costosos equipos de maquinaria, así como trabajadores altamente cualificados. El sector upstream es muy amplio y abarca operaciones de perforación tanto en tierra como en alta mar.

¿Cómo sabe cuánto petróleo original en el lugar (OOIP) o gas original en el lugar (OGIP) está presente en nuestro yacimiento? Existen dos métodos de cálculo de hidrocarburos in situ llamados "estáticos" y "dinámicos". El método estático es conocido por los geólogos y geofísicos como el método volumétrico. El resultado del hidrocarburo en el lugar de su cálculo se compartirá con los ingenieros de yacimientos, ya que también determinarán el hidrocarburo en el lugar inicial a partir de los datos de producción a través de los métodos dinámicos, uno de ellos es el análisis de balance de materiales.

En este analisis, nos sentraremos en el metodo para calculo de OOIP por medio de calculos estáticos. ya que el  método volumétrico asume que el hidrocarburo original en el lugar es proporcional al volumen del yacimiento y que el yacimiento tiene una forma estructural. Este método se implementa antes de que comience la producción. Una vez que comenzó la producción y se registran los datos de producción, es importante verificar el hidrocarburo en el lugar del estudio volumétrico.
 
</p>

*Esta herramienta de analisis permite realizar una descripcion general del comportamiento de yacimientos de oil & gas para determinar de forma anticipada la volumetria esperada de gas o petrolio in situ ( originario antes de perforamiento del yacimiento), demo de analitica avanzada.

<h1 align="center"> Analitica de OOIP para Evaluaciòn de yacimientos- </h1>

<p align="center"><img src="https://1.bp.blogspot.com/-MKDWvZWzv1M/XnKAU_STkNI/AAAAAAAACa0/Nytz-8vhtB8DdUfV6FctV7-gV7YWd9RsgCLcBGAsYHQ/s320/map11_medium.jpg"/></p> 

# Tabla de contenidos:
---

- [Variables_de_estudio](#Variables_de_estudio)
- [Prerequisitos](#Prerequisitos)
- [Analisis_descriptivo](#Analisis_descriptivo)
- [Entrenamiento_modelo_ml_y_evaluacion](#Entrenamiento_modelo_ml_y_evaluacion)
- [Definiciones-interpretaciones](#Definiciones-interpretaciones)
- [Guía_de_usuario](#Guía_de_usuario)

--------------------------------------------------------------------------------------

## Variables_de_estudio

**conjunto de datos volumetric_data**

Se consideran mediciones registradas en diferentes puntos de  un yacimiento determinado para analisis antes del perforado, en las cuales se miden las sigueintes caracteristicas:

* Profundidad del pozo
* Porosidad de la roca
* Saturación de agua en el pozo
* Espesor de la roca

las cuales son utilizadas por medio de metodos de calculos volumetricos  tales como  piramidal, trapezoide  para determinar el gas&oil original en el lugar de analisi ( OOIP), este metodo realiza un mapeo interpolado de los puntos medibles al rededor del pozo, con el objetivo de estimar la cantidad de volumen de petroleo esperado, bajo las condiciones de la tierra por las caracteristicas mencionadas anteriormente.
 
**Conjunto de datos volve production data set**

se considera varaibalas de medicion por meido de procesos de litologia para determinar series temporales para observar la presencia de hidrocarburos por tipo de roca y su profundidad.

se  consideran las siguientes variables aleatorias

* 'DEPTH',
* 'ABDCQF01',
* 'ABDCQF02',
* 'ABDCQF03',
* 'ABDCQF04',
* 'BS',
* 'CALI',
* 'DRHO',
* 'DT',
* 'DTS',
* 'GR',
* 'NPHI',
* 'PEF',
* 'RACEHM',
* 'RACELM',
* 'RD',
* 'RHOB',
* 'RM',
* 'ROP',
* 'RPCEHM',
* 'RPCELM',
* 'RT'
-----------------------------------------------------------------------

## Prerequisitos

Para la ejecución de la herramienta de análisis se necesita installar las  siguientes  dependencias:

- ![python](https://img.shields.io/badge/python%20-3.9.7-green)
- ![numpy](https://img.shields.io/badge/numpy%20-1.23.1-green)
- ![scipy](https://img.shields.io/badge/scipy%20-1.9.0-green)
- ![matplotlib](https://img.shields.io/badge/matplotlib%20-3.5.2-green)
- ![pandas](https://img.shields.io/badge/pandas%20-1.4.3-green)
- ![seaborn](https://img.shields.io/badge/seaborn%20-0.11.2-green)


## Entrenamiento_modelo_ml_y_evaluacion

Se tiene dos archivos formato ipynb, en el primero se almacena la estimaciones de volumetrias utilizando los metodos estaticos Trapezoidal, Pyramidal y Simpson 1/3 para calcular la cantidad de hidrocarburo original en el yacimiento antes de su explotación. esta unidad de medida se expresa en **millones STB**

Por otro lado,  se muestran las series de las mediciones de litologia con referencia a la prfundidad del pozo ( yacimiento ) de las sigueintes variables  'NPHI', 'RHOB', 'GR', 'RT', 'PEF', 'CALI', 'DT' , con el objetivo de calcular  el triple combo de logs  para ver las condiciones pretrofisicas del yacimiento ( esto se encuentra en el notebook serie.ipynb)

## Definiciones-interpretaciones

### Grafico de combo triple de log

El gráfico de combo triple de log, también conocido como gráfico de registro triple, es un tipo de gráfico utilizado en la industria de petróleo y gas para visualizar datos recopilados durante la perforación de un pozo. El gráfico combina tres curvas de registro diferentes: registro de densidad (**RHOB**), registro de resistividad(**Resistivity**) y registro de porosidad (**NPHI**).

Cada curva del registro triple se representa en un eje vertical separado, con la profundidad del pozo en el eje horizontal. Los valores medidos en cada registro se muestran en diferentes escalas, por lo que cada curva puede tener una amplitud diferente.

El registro de densidad muestra la densidad de la formación geológica que rodea el pozo, lo que puede proporcionar información sobre la porosidad y el contenido de fluidos. El registro de resistividad mide la resistencia eléctrica de la formación, lo que puede ayudar a identificar la presencia de agua salada o hidrocarburos. El registro de porosidad mide la cantidad de espacio vacío en la roca, que es importante para determinar el potencial de producción de hidrocarburos.

Al combinar estas tres curvas en un solo gráfico, se puede obtener una imagen más completa de las características del yacimiento de hidrocarburos. Por ejemplo, si la curva de densidad muestra una formación menos densa y la curva de porosidad muestra una mayor porosidad, esto puede indicar la presencia de una formación geológica porosa que puede contener hidrocarburos. Si la curva de resistividad muestra un aumento en la resistencia eléctrica, esto puede indicar la presencia de agua salada.

En general, el gráfico de combo triple de log permite a los ingenieros de petróleo y gas evaluar y comprender las características del yacimiento de hidrocarburos para tomar decisiones informadas sobre la perforación, la producción y la exploración.

### Neutron density plot 

Un gráfico de densidad de neutrones, también conocido como registro de densidad de neutrones (ND), se utiliza en la industria de petróleo y gas para evaluar la densidad de la formación geológica que rodea un pozo de perforación. Este gráfico se genera midiendo la cantidad de neutrones emitidos por una fuente de neutrones hacia la formación y registrando la cantidad de neutrones que regresan al detector.

En el contexto de la evaluación del yacimiento de hidrocarburos, el gráfico de densidad de neutrones puede proporcionar información sobre la porosidad de la roca circundante, que es importante para determinar la cantidad de petróleo o gas que puede contener la formación. La porosidad se refiere a la cantidad de espacio vacío en la roca, que puede contener líquidos y gases.

El gráfico de densidad de neutrones muestra la densidad de la formación geológica en función de la profundidad del pozo. En el eje vertical se representa la profundidad, mientras que en el eje horizontal se muestra la densidad. La densidad se puede expresar en unidades de gramos por centímetro cúbico (g/cm³) o en unidades de porcentaje (%).

Los valores de densidad más altos en el gráfico indican formaciones geológicas más densas, mientras que los valores más bajos indican formaciones menos densas. La porosidad de la roca se puede calcular a partir del gráfico de densidad de neutrones utilizando la relación entre la densidad de la roca y la densidad de una roca completamente sólida.

En resumen, el gráfico de densidad de neutrones es una herramienta valiosa en la evaluación de yacimientos de hidrocarburos, ya que proporciona información sobre la porosidad y densidad de la formación geológica circundante.

## Guía_de_usuario
El repositorio contempla los siguientes folders y archivos 
*  **Data** : se almacena  los datos  que  se utilizan para el analisis,  inicialmente se carga el archivo llamado **volumetric_data** para realizar el calculo del **OOIP** de un yacimiento ,  en este archivero se puede encontrar una carpeta que se llama volve donde  se almacenan archivos .las de popsos  para analisis petrofisico y de litologia del yacimiento de hidrocarburos volvo.
* **volumetrics**: paquete que contiente  las funciones  de interes para utilizar en el calculo del **OOIP**
* **Estimacion_volumetria_OIP** : notebook de jupyter que contine el paso a paso para estimar la cantidad de petroleo (gas) en un yacimiento, considerando metodos de analisis estaticos 

<p align="center"><img src="https://cdn.slidesharecdn.com/ss_thumbnails/calculodelpoesyreservas-161007173038-thumbnail.jpg?width=600&height=600&fit=bounds"/></p> 

* **serie** : notebook donde se encuentra analisis base de litologia para determninar el comportamiento del subsuelo del yacimiento, permite identificar razgos fundamentales de la perforación durante la exploracion de los pozos.
