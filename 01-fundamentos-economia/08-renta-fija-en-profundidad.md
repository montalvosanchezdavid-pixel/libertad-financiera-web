# Renta fija en profundidad

En [mercados financieros](02-mercados-financieros.md) viste la
idea básica de un bono. Aquí se profundiza porque la renta fija es el
activo natural para el "cubo reserva" del negocio
([política de inversión](../02-portfolio-inversion/01-politica-inversion.md))
— y para usarla bien hay que entender más que "paga un interés fijo".

## Anatomía de un bono

- **Nominal**: lo que se devuelve al vencimiento.
- **Cupón**: el interés periódico (algunos bonos, "cupón cero", no pagan
  cupón y se compran con descuento sobre el nominal).
- **Vencimiento**: cuándo se devuelve el nominal.
- **Yield (rentabilidad)**: el retorno real para quien lo compra hoy,
  que no es lo mismo que el cupón si el bono cotiza por encima o por
  debajo de su nominal.

## La relación inversa precio-yield

Cuando suben los tipos de interés de mercado, el precio de los bonos ya
emitidos (con cupón fijo más bajo que el nuevo tipo) **baja** — nadie
pagaría el nominal completo por un cupón menos atractivo que el que se
puede conseguir ahora. Es la razón por la que en 2022, con la subida de
tipos más rápida en décadas, muchos fondos de renta fija "supuestamente
seguros" tuvieron pérdidas — algo contraintuitivo que conviene tener
interiorizado antes de meter ahí la reserva del negocio.

## Duración: el termómetro de sensibilidad

La duración mide cuánto se mueve el precio de un bono (o fondo de renta
fija) por cada punto porcentual que se mueven los tipos. A mayor
duración (bonos a más largo plazo), mayor sensibilidad — más ganancia si
bajan tipos, pero más pérdida si suben.

Para el cubo reserva del negocio, cuya prioridad es **no perder valor
justo cuando lo necesitas**, interesa duración **corta** (letras del
tesoro, fondos monetarios, depósitos) — sacrificas algo de rentabilidad
a cambio de mucha menos sensibilidad a movimientos de tipos.

## Ejemplo numérico: qué le pasa a un bono cuando suben los tipos

Un fondo de renta fija con duración 7 sufre, aproximadamente, una caída
de precio del 7% por cada punto porcentual que suben los tipos de
interés de mercado (la duración funciona como un multiplicador
aproximado). Es lo que pasó de forma real en 2022:

| Activo | Duración aprox. | Subida de tipos 2022 | Caída aprox. resultante |
|---|---|---|---|
| Fondo monetario / letras a corto plazo | ~0,2 | +4 puntos | Prácticamente sin impacto de precio |
| Bono corporativo a 5 años | ~4,5 | +4 puntos | ~-16% a -18% |
| Bono soberano a 20-30 años | ~17-19 | +4 puntos | ~-35% a -40% |

Es el motivo exacto por el que un fondo de renta fija "a largo plazo",
supuestamente conservador, tuvo en 2022 pérdidas comparables a las de
la bolsa — y por el que la reserva del negocio, con fecha de necesidad
conocida, debe ir en el extremo izquierdo de esta tabla (duración casi
cero), no en cualquier punto etiquetado como "renta fija".

## Riesgo de crédito y rating

Además del riesgo de tipos, existe el riesgo de que el emisor no pague
(default). Las agencias de rating (Moody's, S&P, Fitch) califican esa
probabilidad:
- **Investment grade** (BBB-/Baa3 o superior): riesgo de impago bajo
  (deuda pública de países solventes, grandes corporativos).
- **High yield / "bono basura"**: mayor cupón porque compensa mayor
  riesgo de impago — no es el tipo de activo adecuado para una reserva
  que debe estar disponible con certeza.

## La curva de tipos, revisitada

Ya viste en [macroeconomía básica](01-macroeconomia.md) que su inversión
(corto plazo pagando más que largo plazo) anticipa recesiones. Ahora con
más contexto: normalmente el mercado exige más rentabilidad por prestar
a más largo plazo (más incertidumbre) — cuando eso se invierte, es
porque el mercado espera que el banco central **baje** tipos en el
futuro (típicamente porque anticipa una desaceleración fuerte).

## Cómo aplicarlo de forma práctica

- Fondos monetarios (invierten en deuda a muy corto plazo) o cuentas
  remuneradas: el vehículo natural para la parte de la reserva más
  cercana a necesitarse.
- Letras del Tesoro español: bajo riesgo de crédito, fiscalidad como
  renta del ahorro, se pueden comprar directamente en el Tesoro Público.
- Fondos de renta fija a corto plazo: diversifican emisor sin asumir
  duración larga.
- Evitar fondos de renta fija a largo plazo o high yield para cualquier
  dinero con fecha de necesidad conocida (los 3-5 años del negocio).

## Enlaces para profundizar

- [Tesoro Público — Letras del Tesoro](https://www.tesoro.es/deuda-publica/letras-del-tesoro)
- [Investopedia — Bond Duration](https://www.investopedia.com/terms/d/duration.asp)
- [Investopedia — Credit Rating](https://www.investopedia.com/terms/c/creditrating.asp)
