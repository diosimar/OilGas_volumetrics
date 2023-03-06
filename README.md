![analytics](https://img.shields.io/badge/Machine%20Learning-Medicina%20predictiva-green)

# Oil & Gas volumetrias ( OIP)

# Introducción 👇


<p style='text-align: justify;'>

El sector upstream de la industria del petróleo y el gas, a veces denominado exploración y producción (o E&P), se ocupa de localizar yacimientos para la extracción de petróleo y gas y la posterior perforación, recuperación y producción de crudo y gas natural. La producción de petróleo y gas es una industria increíblemente intensiva en capital, que requiere el uso de costosos equipos de maquinaria, así como trabajadores altamente cualificados. El sector upstream es muy amplio y abarca operaciones de perforación tanto en tierra como en alta mar.

¿Cómo sabe cuánto petróleo original en el lugar (OOIP) o gas original en el lugar (OGIP) está presente en nuestro yacimiento? Existen dos métodos de cálculo de hidrocarburos in situ llamados "estáticos" y "dinámicos". El método estático es conocido por los geólogos y geofísicos como el método volumétrico. El resultado del hidrocarburo en el lugar de su cálculo se compartirá con los ingenieros de yacimientos, ya que también determinarán el hidrocarburo en el lugar inicial a partir de los datos de producción a través de los métodos dinámicos, uno de ellos es el análisis de balance de materiales.

En este analisis, nos sentraremos en el metodo para calculo de OOIP por medio de calculos estáticos. ya que el  método volumétrico asume que el hidrocarburo original en el lugar es proporcional al volumen del yacimiento y que el yacimiento tiene una forma estructural. Este método se implementa antes de que comience la producción. Una vez que comenzó la producción y se registran los datos de producción, es importante verificar el hidrocarburo en el lugar del estudio volumétrico.
 
</p>

*Esta herramienta de analisis permite realizar una descripcion general del comportamiento de yacimientos de oil & gas para determinar de forma anticipada la volumetria esperada de gas o petrolio in situ ( originario antes de perforamiento del yacimiento), demo de analitica avanzada.

<h1 align="center"> Analitica de OOIP para Evaluaciòn de yacimientos- </h1>

<p align="center"><img src="https://www.drillingformulas.com/wp-content/uploads/2016/04/Volumetric-Estimation-of-Fluid-Reserves.jpg"/></p> 

# Tabla de contenidos:
---

- [Variables_de_estudio](#Variables_de_estudio)
- [Prerequisitos](#Prerequisitos)
- [Analisis_descriptivo](#Analisis_descriptivo)
- [Entrenamiento_modelo_ml_y_evaluacion](#Entrenamiento_modelo_ml_y_evaluacion)
- [Guía_de_usuario](#Guía_de_usuario)

--------------------------------------------------------------------------------------

## Variables_de_estudio

Se consideran mediciones registradas en diferentes puntos de  un yacimiento determinado para analisis antes del perforado, en las cuales se miden las sigueintes caracteristicas:

* Profundidad del pozo
* Porosidad de la roca
* Saturación de agua en el pozo
* Espesor de la roca

las cuales son utilizadas por medio de metodos de calculos volumetricos  tales como  piramidal, trapezoide  para determinar el gas&oil original en el lugar de analisi ( OOIP), este metodo realiza un mapeo interpolado de los puntos medibles al rededor del pozo, con el objetivo de estimar la cantidad de volumen de petroleo esperado, bajo las condiciones de la tierra por las caracteristicas mencionadas anteriormente.
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



## Guía_de_usuario
