# DCA vs. pago único (lump sum)

Ya conoces el concepto de DCA
([el glosario](../01-fundamentos-economia/05-glosario.md)).
Este documento existe para que sepas que, aunque en tu caso no hay
elección real, sí hay evidencia relevante detrás de la que otros sí
tienen.

## La evidencia: lump sum gana en promedio

Estudios históricos (el más citado es de Vanguard) muestran que invertir
una cantidad grande de golpe (lump sum) supera a repartirla en
aportaciones periódicas (DCA) en aproximadamente **dos de cada tres
periodos históricos** analizados. La razón es simple: el mercado sube
con más frecuencia de la que baja a largo plazo, así que cuanto antes
esté el dinero invertido, más tiempo tiene para crecer.

## Entonces, ¿por qué existe DCA como estrategia?

- **Reduce la varianza de resultados**, no solo el resultado esperado:
  con lump sum, el resultado depende mucho de si el momento de entrada
  fue bueno o malo; con DCA, se promedia el precio de entrada a lo largo
  del periodo, suavizando tanto los mejores como los peores escenarios.
- **Reduce el "arrepentimiento"**: psicológicamente, invertir una suma
  grande justo antes de una caída fuerte es mucho más difícil de asumir
  emocionalmente que ver caer una pequeña aportación mensual — conecta
  con
  [Psicología y sesgos del inversor](../01-fundamentos-economia/12-psicologia-y-sesgos-del-inversor.md).
- **Es la única opción realista** cuando el dinero no existe todavía de
  golpe, sino que llega como ahorro mensual del sueldo — la situación típica de quien ahorra de forma periódica.

## Ejemplo numérico: cómo promedia el precio el DCA

Aportando 500€/mes durante 6 meses a un fondo cuyo precio por
participación varía:

| Mes | Precio por participación | Participaciones compradas con 500€ |
|---|---|---|
| 1 | 100€ | 5,00 |
| 2 | 90€ | 5,56 |
| 3 | 80€ | 6,25 |
| 4 | 85€ | 5,88 |
| 5 | 95€ | 5,26 |
| 6 | 110€ | 4,55 |

```chart
{
  "type": "line",
  "title": "Precio por participacion durante los 6 meses",
  "unit": "€",
  "labels": ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6"],
  "series": {"Precio": [100, 90, 80, 85, 95, 110]}
}
```

Total invertido: 3.000€. Total participaciones: 32,5. Precio medio de
compra real: 3.000€ / 32,5 ≈ **92,3€** — por debajo de la media simple
de los seis precios (93,3€), porque compraste automáticamente más
participaciones cuando el precio estaba bajo (meses 2 y 3) y menos
cuando estaba alto (mes 6). Este efecto (comprar más barato cuando cae,
sin decidirlo activamente) es la ventaja mecánica del DCA, indepen-
diente de cualquier habilidad para predecir el mercado.

## Tu caso: DCA "forzoso" y por qué no es una desventaja

No estás "eligiendo" DCA frente a lump sum por estrategia de timing: es
la única forma en que existe tu capital de inversión (una parte del sueldo mensual). Esto es en realidad una ventaja estructural: al no
tener una suma grande esperando el "momento perfecto" para entrar,
eliminas por completo la tentación de intentar predecir el mercado antes
de invertir (market timing) — cada mes, la decisión es automática, no
una decisión activa.

## Variante: Value Averaging

Una variante más sofisticada de DCA: en vez de aportar siempre la misma
cantidad, se ajusta la aportación para que el valor total de la cartera
crezca según un objetivo predefinido — aportando más los meses que el
mercado ha bajado (compras "más barato") y menos (o vendiendo) los meses
que ha subido mucho. Requiere más disciplina y cálculo que el DCA
simple, y su ventaja sobre DCA clásico es modesta y debatida — no es
necesario para tu plan, pero vale la pena saber que existe.

## Enlaces para profundizar

- [Vanguard — Cost averaging: invest now or temporarily hold your cash?](https://investor.vanguard.com/investor-resources-education/article/cost-averaging-invest-now-or-temporarily-hold-your-cash)
- [Bogleheads wiki — Dollar cost averaging](https://www.bogleheads.org/wiki/Dollar_cost_averaging)
