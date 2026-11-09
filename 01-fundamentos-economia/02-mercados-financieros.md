# Mercados financieros

## Acciones

Una parte de la propiedad de una empresa. Ganas dinero de dos formas:
subida del precio (revalorización) y dividendos (reparto de beneficios).
Acción individual = riesgo concentrado en una empresa: puede irte muy
bien o muy mal.

## Fondos indexados y ETFs

En vez de comprar una acción, compras "un trozo de todas": un ETF que
replica el S&P 500 te da exposición a las 500 mayores empresas de EEUU
en un solo producto. Menor riesgo que una acción suelta porque
diversificas automáticamente. Es la base de la parte "núcleo" de tu plan
de inversión (ver [02-portfolio-inversion](../02-portfolio-inversion/01-politica-inversion.md)).

## Índices bursátiles

Un índice (S&P 500, Nasdaq, IBEX 35...) es una cesta representativa de
empresas que sirve de termómetro del mercado. No se puede invertir
directamente en un índice, pero sí en productos (ETFs, fondos) que lo
replican. La pestaña Mercados de Supertrader te da el pulso de los
principales índices en tiempo real.

## Renta fija (bonos)

Prestas dinero (a un estado o empresa) a cambio de un interés fijo
durante un plazo. Menor riesgo y menor potencial de subida que la renta
variable; sirve para amortiguar la volatilidad de una cartera.

## Criptomonedas

Activos digitales sin respaldo de ningún banco central, con volatilidad
muy superior a acciones o bonos. No generan dividendos ni flujo de caja
— su valor depende enteramente de la demanda futura. Encajan como
posición satélite pequeña, nunca como núcleo de una cartera con un
horizonte de 4 años como el tuyo.

## Volatilidad

Cuánto se mueve el precio de un activo. Más volatilidad = más riesgo de
pérdida a corto plazo, pero también más potencial de ganancia. El
optimizador de Supertrader usa la volatilidad histórica (junto al
retorno esperado) para calcular el reparto entre fondos.

## Ejemplo real: concentración vs. diversificación

En 2022, con la subida de tipos golpeando a las tecnológicas, algunas
acciones individuales muy conocidas cayeron mucho más que el mercado en
conjunto:

| Activo | Caída aprox. en 2022 |
|---|---|
| Meta (Facebook) | ~-64% |
| Netflix | ~-51% |
| S&P 500 (índice completo, 500 empresas) | ~-19% |
| MSCI World (índice global) | ~-18% |

```chart
{
  "type": "bar",
  "title": "Caída aproximada en 2022",
  "unit": "%",
  "data": {"Meta (Facebook)": -64, "Netflix": -51, "S&P 500 (500 empresas)": -19, "MSCI World (global)": -18}
}
```

Quien tuviera solo Meta como posición principal sufrió más de tres veces
la caída de quien estaba en un fondo indexado amplio — no porque Meta
sea "mala", sino porque una sola empresa concentra todo el riesgo
específico de esa empresa (directivos, competencia, un producto que no
funciona), mientras que el índice diluye ese riesgo entre 500 empresas
distintas. Es el ejemplo numérico detrás de por qué tu núcleo va en
fondos indexados y una acción suelta como Meta, si la quieres, es
satélite de tamaño limitado.

## Cómo se relaciona esto con la macro

Los mercados anticipan la economía: bajan cuando se espera una
recesión, suben cuando se espera expansión — a veces antes de que el
dato macro oficial lo confirme. Por eso Supertrader cruza mercados y
macro en pestañas separadas pero pensadas para leerse juntas.

## Enlaces para profundizar

- [Investopedia — Stock Market Basics](https://www.investopedia.com/terms/s/stockmarket.asp)
- [CNMV — Guía del inversor](https://www.cnmv.es/portal/Inversor/Guia-Inversor.aspx) (regulador
  español de mercados)
- [Bogleheads — filosofía de inversión indexada](https://www.bogleheads.org/wiki/Bogleheads%C2%AE_investment_philosophy)
