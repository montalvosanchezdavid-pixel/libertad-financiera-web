# Rebalanceo: estrategias avanzadas

[Política de inversión](01-politica-inversion.md) ya establece
revisión trimestral. Aquí se detallan las opciones reales para ejecutar
ese rebalanceo de la forma más eficiente (fiscal y operativamente).

## Rebalanceo por calendario vs. por banda

- **Por calendario**: revisar y ajustar en fechas fijas (ej. cada
  trimestre), independientemente de cuánto se haya desviado la cartera.
  Simple y predecible.
- **Por banda (threshold)**: rebalancear solo cuando un cubo se desvía
  más de un umbral definido (ej. ±5 puntos porcentuales de su peso
  objetivo), sin importar cuándo ocurra. Más eficiente (evita
  operaciones innecesarias cuando todo sigue cerca del objetivo), pero
  requiere vigilar la cartera con más frecuencia que solo una vez al
  trimestre.
- Enfoque híbrido, razonable para tu caso: revisar trimestralmente
  (calendario) y solo actuar si algún cubo supera su banda de desviación
  — combina la simplicidad de una rutina fija con no operar sin
  necesidad.

## Ejemplo numérico: una cartera que se desvía

Empiezas con núcleo 60% (60.000€) y satélite 15% (15.000€) sobre una
cartera de 100.000€ (el resto en reserva). El satélite tiene un año
excelente (+60%) mientras el núcleo sube lo normal (+8%):

| Cubo | Valor inicial | Tras un año | Peso resultante |
|---|---|---|---|
| Núcleo | 60.000€ | 64.800€ | ~55,6% (antes 60%) |
| Satélite | 15.000€ | 24.000€ | ~20,6% (antes 15%, por encima del límite del 15%) |

Sin rebalancear, el satélite ha pasado de ser una posición limitada a
representar más peso relativo del que tu política permite — exactamente
el escenario que el rebalanceo trimestral está diseñado para corregir,
antes de que "una posición que ha ido muy bien" se convierta, sin que lo
decidas activamente, en la parte más grande y arriesgada de tu cartera.

## El coste fiscal del rebalanceo importa

Ver
[Fiscalidad de la inversión en España](../01-fundamentos-economia/03-fiscalidad-inversion-espana.md):
- **Fondos de inversión**: traspasar entre fondos (vender uno, comprar
  otro) no tributa hasta el reembolso final — puedes rebalancear entre
  fondos indexados sin coste fiscal inmediato.
- **ETFs**: vender un ETF con ganancia sí genera una plusvalía sujeta a
  IRPF en ese momento, aunque el dinero se reinvierta enseguida en otro
  ETF — un rebalanceo "gratis" en fondos puede tener coste fiscal real
  en ETFs.
- Esto es un argumento adicional (más allá del ya mencionado) a favor de
  usar fondos de inversión, no ETFs, para el núcleo si vas a rebalancear
  con cierta frecuencia.

## Rebalancear con nuevas aportaciones antes que vendiendo

La forma más eficiente de rebalancear una cartera que sigue recibiendo
aportaciones mensuales (tu caso) es dirigir las **nuevas** aportaciones
hacia el cubo que se ha quedado por debajo de su peso objetivo, en vez
de vender el que ha subido. Ventajas:
- Ningún coste fiscal (no hay venta).
- Ninguna orden de venta que ejecutar activamente.
- Solo cuando la desviación es demasiado grande para corregirla con
  aportaciones nuevas en un plazo razonable, tiene sentido vender del
  cubo sobreponderado.

## Ejemplo aplicado a tus tres cubos

Si el satélite ha subido mucho y supera su límite del 10-15% (ver
[Política de inversión](01-politica-inversion.md)):
1. Primera opción: dirigir las próximas aportaciones mensuales solo al
   núcleo hasta que el peso del satélite vuelva a su rango — sin vender
   nada del satélite.
2. Si el desvío es demasiado grande para corregirlo así en 1-2
   trimestres: vender el exceso del satélite y reforzar el núcleo,
   asumiendo el coste fiscal de esa venta si es en acciones/ETFs
   individuales.

## Frecuencia y disciplina

El error más común no es rebalancear "mal" técnicamente, sino no
rebalancear en absoluto porque "el que sube parece que va a seguir
subiendo" — es exactamente el sesgo de recencia descrito en
[Psicología y sesgos del inversor](../01-fundamentos-economia/12-psicologia-y-sesgos-del-inversor.md).
Tener la regla escrita (banda + calendario) y seguirla mecánicamente
es más importante que la sofisticación de la regla en sí.

## Enlaces para profundizar

- [Vanguard — Rebalancing a portfolio](https://investor.vanguard.com/investor-resources-education/portfolio-management/rebalancing-your-portfolio)
- [Bogleheads wiki — Rebalancing](https://www.bogleheads.org/wiki/Rebalancing)
