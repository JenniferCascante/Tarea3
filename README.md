# Universidad de Costa Rica
# Tarea 3  
# Jennifer María Cascante Peraza  
# B51626
# Profesor: Fabián Abarca

Punto 1: A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.
La función de densidad marginal se calcula por medio de la integral a la distribución conjunta de X o Y, o en este caso al ser valores discretos por medio de la
sumatoria de estos, es por esto que en el código después de exportar y procesar a la interfaz los datos ya dados, se crea un vector con el tamaño correspodiente de
las filas y columnas, con el comando linspace para calcular el valor de la densidad marginal sumando los datos de interés, se utilizó el comando sum. Luego de esto    
se graficaron las curvas de dichos datos para poder indetificar el modelo de distribución usual estudiado: rayleigh, exponencial, uniforme o normal (campana gaussiana),
tanto para las filas como para las columnas las gráficas se asemejaron a la gaussiana, por lo tanto esta fue la función que se definió, para poder calcular la mejor curva de ajusta al usar el comando curve_fit.

![Y](1.png)
![Y](2.png)

Ajuste para filas X = [9.90484381 3.29944288]

Ajusute para columnas Y = [15.0794609   6.02693775]


Punto 2: Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
Si las variables son independientes pues la función de probabilidad  de densidadd conjunta es el producto de las marginales. La expresión de la función de densidad conjunta que modela los datos es:

FX,Y(x, y) = FX(x) * FY (y) para todo x, y ∈ R

Punto 3: Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

- Correlación: Permite conocer si existe una relación funcional entre las variables X, Y. Es decir, poder calcular los valores de Y a partir de los de X, con una función.
La correlación es: 149.54281000000012
Como el número obtenido fue positivo se puede afirmar Positivo que las variables son directamente proporcionales entre sí,  y que la media varía en la misma dirección con el factor del valor del coeficiente de correlación.

- Covarianza: La covarianza indica si ambas variables varían en la misma dirección (covarianza positiva) o en dirección opuesta (covarianza negativa). No tiene importancia en el valor numérico de covarianza, solo el signo es útil.
La covarianza es: 0.183105046498099
En este caso la covarianza es positiva por lo tanto las variables varían en la misma dirección.

- Coeficiente de correlación:  Es el parámetro que nos va a decir si la correlación es débil o fuerte. Para calcularlo, necesitamos conocer el valor de las desviaciones típicas marginales de cada variable σx y σy. Su valor siempre estará entre -1 y 1. Su expresión es la siguiente: r= (σxy)/(σx*σy)
El coeficiente de covarianza es: 0.0023019877198043152
En este caso como el coeficiente dio un valor muy cercano a cero, se puede afirmar que la correlación es muy débil.


Punto 4: Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).

Gráficas 2D:
![Y](1.png)
![Y](2.png)
Estas imágenes corresponde a las curvas después de realizarse el ajuste.
![Y](3.png)
![Y](4.png)

Gráficas 3D:
Imagen de la densidad conjunta en 3D:
![Y](5.png)


