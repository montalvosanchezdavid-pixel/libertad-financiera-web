# Interés compuesto y matemática financiera

Todo el resto del repositorio asume que entiendes esto — merece su
propio documento porque es, con diferencia, el concepto individual más
importante de todo el plan.

## La fórmula

Valor futuro de una cantidad invertida hoy:

```
VF = VP × (1 + r)^n
```

Donde VP = valor presente, r = tipo de retorno por periodo, n = número
de periodos. La diferencia con el interés **simple** (que solo calcula
interés sobre el capital inicial) es que aquí cada periodo genera
interés también sobre los intereses ya acumulados — el crecimiento no es
lineal, es exponencial.

## Por qué empezar antes importa más que aportar más tarde

Ejemplo con un único pago de 10.000€ al 7% anual:
- Invertido a los 25 años → a los 65 años (40 años de crecimiento): unos
  ~150.000€.
- El mismo pago de 10.000€ invertido a los 35 años → a los 65 (30 años):
  unos ~76.000€.

Diez años de diferencia en el punto de partida, con la misma cantidad,
casi duplican el resultado final — no porque el importe cambie, sino
porque el tiempo es el exponente de la fórmula, no un factor lineal más.
Es el argumento matemático detrás de "empieza cuanto antes", más allá de
cualquier consejo genérico.

## Calculadora: prueba con tus propios números

```calc
{"title": "Interes compuesto con aportacion mensual", "principal": 0, "monthly": 2500, "rate": 7, "years": 4}
```

## La regla del 72

Atajo mental: dividiendo 72 entre el tipo de retorno anual, obtienes
(aproximadamente) los años que tarda una inversión en duplicarse.

- Al 4% anual → ~18 años para duplicar.
- Al 7% anual → ~10 años para duplicar.
- Al 10% anual → ~7 años para duplicar.

Útil para tener intuición rápida sin calculadora, no para cálculos de
precisión (para eso, ver
[Proyección numérica](../02-portfolio-inversion/02-proyeccion-numerica.md)).

## Valor futuro de aportaciones periódicas (anualidades)

Un caso habitual no es un único pago, sino aportaciones mensuales constantes (por ejemplo, 2.500€/mes) — una
"anualidad". La fórmula es más compleja que el interés compuesto simple,
pero la lógica es la misma: cada aportación empieza a generar
rendimiento desde el momento en que se hace, así que las aportaciones
más tempranas del periodo pesan más en el resultado final que las
últimas. Es la base de cómo se calculan los escenarios de
[Proyección numérica](../02-portfolio-inversion/02-proyeccion-numerica.md).

## TAE vs. TIN: la letra pequeña que cambia el resultado

- **TIN (Tipo de Interés Nominal)**: el tipo "de etiqueta", sin
  contar el efecto de la frecuencia de capitalización.
- **TAE (Tasa Anual Equivalente)**: incluye el efecto de cómo de a
  menudo se capitaliza el interés (mensual, trimestral...) y las
  comisiones — es la cifra comparable entre productos distintos
  (depósitos, préstamos, hipotecas).

Dos productos con el mismo TIN pero distinta frecuencia de
capitalización no dan el mismo resultado real — comparar siempre por
TAE, nunca por TIN, tanto al invertir como al pedir financiación para la
clínica.

## Enlaces para profundizar

- [Investopedia — Compound Interest](https://www.investopedia.com/terms/c/compoundinterest.asp)
- [Banco de España — Calculadora y educación financiera](https://www.bde.es/wbe/es/areas-actuacion/educacion-financiera/)
- [Investopedia — Rule of 72](https://www.investopedia.com/terms/r/ruleof72.asp)
