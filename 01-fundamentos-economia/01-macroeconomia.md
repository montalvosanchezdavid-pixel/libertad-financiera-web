# Macroeconomía básica

## PIB (Producto Interior Bruto)

El valor total de todo lo que un país produce en un periodo. Cuando sube,
la economía crece; dos trimestres seguidos cayendo = recesión técnica.
No mide bienestar ni desigualdad, solo actividad económica.

- Se usa como referencia constante en la pestaña Macro de Supertrader
  (indicador `INDPRO`, producción industrial, como proxy mensual de
  actividad).

## Inflación

La subida general de precios. Se mide con índices como el IPC (España) o
el CPI (`CPIAUCSL` en EEUU, el que usa Supertrader). Inflación moderada
(~2%) se considera sana; alta inflación erosiona el valor del ahorro en
efectivo — es el argumento central de por qué "ahorrar" sin invertir
pierde poder adquisitivo con el tiempo.

## Tipos de interés

El precio del dinero. Los fija principalmente el banco central (BCE en
Europa, Fed en EEUU) para controlar la inflación: suben tipos para
enfriar la economía, los bajan para estimularla.

Efecto directo sobre ti:
- Tipos altos → hipotecas y crédito más caros, pero mejor remuneración de
  depósitos/renta fija.
- Tipos bajos → dinero barato, favorece inversión en renta variable e
  inmobiliario.

## Ciclos económicos

La economía no crece en línea recta: expansión → pico → contracción →
suelo, y vuelta a empezar. Un indicador clásico de "algo se está
enfriando" es la inversión de la curva de tipos (cuando la deuda a corto
plazo paga más que la de largo plazo) — es el indicador `T10Y2Y` que ya
usa el módulo Macro de Supertrader.

## Ejemplo numérico: el coste real de no invertir

Supón que guardas 30.000€ (un año de tu ahorro) en una cuenta corriente
al 0% durante 4 años, con una inflación media del 2,5% anual. El dinero
sigue siendo "30.000€" en el banco, pero su poder de compra real es:

| Año | Valor nominal | Poder de compra real (ajustado por inflación) |
|---|---|---|
| 0 | 30.000€ | 30.000€ |
| 1 | 30.000€ | ~29.270€ |
| 2 | 30.000€ | ~28.560€ |
| 3 | 30.000€ | ~27.870€ |
| 4 | 30.000€ | ~27.190€ |

Has "perdido" cerca de 2.800€ de poder adquisitivo sin que aparezca
ningún número en rojo en tu cuenta — la inflación no se siente como una
pérdida, pero lo es. Es la razón numérica, no solo teórica, de por qué
el ahorro sin invertir no es una opción neutra: es una decisión con
coste, aunque no lo parezca.

```chart
{
  "type": "line",
  "title": "30.000€ guardados en efectivo: nominal vs. poder de compra real",
  "unit": "€",
  "labels": ["Año 0", "Año 1", "Año 2", "Año 3", "Año 4"],
  "series": {
    "Valor nominal": [30000, 30000, 30000, 30000, 30000],
    "Poder de compra real": [30000, 29270, 28560, 27870, 27190]
  }
}
```

## Desempleo

Además del nivel, importa la tendencia. Desempleo subiendo suele
anticipar menor consumo, lo que afecta a sectores discrecionales
(negocios como una clínica estética, que depende de gasto no esencial)
antes que a sectores defensivos (salud, alimentación).

## Enlaces para profundizar

- [Investopedia — Macroeconomics](https://www.investopedia.com/terms/m/macroeconomics.asp)
- [Banco Central Europeo — explicación de política monetaria](https://www.ecb.europa.eu/ecb/educational/explainers/tell-me/html/index.en.html)
- [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/) — la
  misma fuente de datos que usa Supertrader para el módulo Macro.
- [Banco de España — Educación financiera](https://www.bde.es/wbe/es/areas-actuacion/educacion-financiera/)
