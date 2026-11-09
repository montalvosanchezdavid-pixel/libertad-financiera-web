# Teoría moderna de carteras

La estructura de "tres cubos" de
[Política de inversión](01-politica-inversion.md) y el optimizador de
Supertrader no son arbitrarios: se apoyan en un marco teórico concreto,
desarrollado por Harry Markowitz en 1952 (Nobel de Economía en 1990).
Entenderlo te permite usar el optimizador con criterio, no como una caja
negra.

## La idea central

No basta con mirar el retorno esperado de cada activo por separado: lo
que importa es cómo se comportan **juntos** en una cartera. Combinar
activos que no se mueven exactamente igual (baja correlación) reduce el
riesgo total de la cartera sin sacrificar tanto retorno esperado como
parecería a simple vista — es la base matemática de "no pongas todos los
huevos en la misma cesta", cuantificada.

## Correlación: el ingrediente clave

La correlación mide entre -1 y +1 cuánto se mueven dos activos en la
misma dirección:
- **+1**: se mueven exactamente igual (diversificación nula entre
  ellos).
- **0**: no hay relación entre sus movimientos.
- **-1**: se mueven en direcciones exactamente opuestas (diversificación
  máxima, en la práctica casi inexistente entre activos financieros
  reales).

Acciones de un mismo sector suelen tener correlación alta entre sí;
acciones y bonos suelen tener correlación más baja (a veces negativa en
periodos concretos) — es el motivo por el que mezclar renta variable y
renta fija reduce la volatilidad total más de lo que reduciría solo
diversificar dentro de renta variable.

## Ejemplo numérico: por qué correlacionar poco reduce el riesgo

Dos activos con la misma volatilidad individual (20%), combinados al
50/50, dan volatilidad de cartera muy distinta según su correlación:

| Correlación entre los dos activos | Volatilidad resultante de la cartera 50/50 |
|---|---|
| +1 (se mueven idénticos) | 20% (ninguna reducción de riesgo) |
| +0,5 (parcialmente relacionados) | ~17,3% |
| 0 (sin relación) | ~14,1% |
| -0,5 (relación inversa parcial) | ~10% |

Con correlación 0, combinar dos activos igual de arriesgados por
separado reduce el riesgo total casi un 30% sin sacrificar el retorno
esperado (que sigue siendo el promedio de ambos) — esto es, literalmente,
la única forma conocida de "comer gratis" en inversión: reducir riesgo
sin reducir retorno esperado, solo por cómo se combinan los activos.

## La frontera eficiente

Para cada nivel de riesgo (volatilidad) asumido, existe una combinación
de activos que maximiza el retorno esperado — el conjunto de esas
combinaciones óptimas es la "frontera eficiente". Carteras por debajo de
la frontera son subóptimas (mismo riesgo, menos retorno posible);
carteras sobre la frontera son las candidatas razonables según cuánto
riesgo se quiera asumir.

## Cómo lo aplica el optimizador de Supertrader

`supertrader/optimizer.py` usa `PyPortfolioOpt` para:
1. Calcular retorno esperado y volatilidad histórica real de cada fondo
   (no supuestos fijos como en
   [Proyección numérica](02-proyeccion-numerica.md)).
2. Calcular la matriz de correlaciones entre todos los fondos
   introducidos.
3. Encontrar el reparto de pesos que maximiza el Sharpe ratio (retorno
   por unidad de riesgo) dentro de los límites `min_weight`/`max_weight`
   que definas en `config.yaml` — el mismo mecanismo que ya usas para
   implementar los límites de la política de tres cubos.

## Limitaciones que conviene conocer

- **Asume que las correlaciones son estables**: en crisis graves, la
  correlación entre activos "normalmente poco relacionados" tiende a
  subir hacia 1 (todo cae a la vez) — ver
  [Historia de crisis financieras](../01-fundamentos-economia/10-historia-de-crisis-financieras.md).
  La diversificación protege menos precisamente cuando más se necesita.
- **Se basa en datos históricos**: el retorno/volatilidad pasado no
  garantiza el futuro — es una estimación razonable, no una certeza.
- **Asume distribución normal de retornos**: la realidad tiene "colas
  gruesas" (eventos extremos más frecuentes de lo que una distribución
  normal predeciría) — motivo adicional para no apalancar el satélite ni
  concentrar en exceso.

## Enlaces para profundizar

- [Investopedia — Modern Portfolio Theory (MPT)](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- [Investopedia — Efficient Frontier](https://www.investopedia.com/terms/e/efficientfrontier.asp)
- [PyPortfolioOpt — documentación oficial](https://pyportfolioopt.readthedocs.io/)
