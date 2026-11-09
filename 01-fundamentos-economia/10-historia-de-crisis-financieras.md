# Historia de crisis financieras

Conocer el patrón de crisis pasadas no sirve para predecir la próxima
(cada una es distinta), pero sí para interiorizar algo muy concreto:
**las caídas fuertes ocurren con regularidad histórica**, y tu horizonte
de 4-5 años tiene una probabilidad no trivial de incluir una. Este
documento existe para que eso no te pille por sorpresa emocionalmente.

## Panorama rápido

| Crisis | Causa central | Caída aprox. bolsa EEUU | Duración hasta recuperar máximos |
|---|---|---|---|
| 1929 — Gran Depresión | Burbuja de crédito + pánico bancario | ~-86% | ~25 años (con inflación) |
| 1973-74 — Crisis del petróleo | Shock de oferta energética + inflación | ~-45% | ~7 años |
| 1987 — Lunes Negro | Pánico técnico/algorítmico, un solo día -22% | ~-33% (pico a valle) | ~2 años |
| 2000-02 — Puntocom | Burbuja de valoración en tecnológicas | ~-49% (Nasdaq ~-78%) | ~7 años |
| 2008-09 — Financiera global | Crisis de crédito hipotecario/bancario | ~-57% | ~5 años |
| 2010-12 — Deuda soberana europea | Riesgo de impago de países del euro | Variable por país | ~2-4 años según país |
| 2020 — COVID | Shock exógeno (pandemia, parón económico) | ~-34% | ~5 meses (recuperación histórica rápida) |
| 2022 — Inflación/subida de tipos | Fin de una década de tipos ultra bajos | ~-25% | ~2 años |

```chart
{
  "type": "bar",
  "title": "Caída aproximada de máximo a mínimo, bolsa EEUU",
  "unit": "%",
  "data": {
    "1929 - Gran Depresión": -86,
    "1973-74 - Petróleo": -45,
    "1987 - Lunes Negro": -33,
    "2000-02 - Puntocom": -49,
    "2008-09 - Financiera global": -57,
    "2020 - COVID": -34,
    "2022 - Inflación/tipos": -25
  }
}
```

*(Cifras aproximadas y con fines ilustrativos — cada crisis se mide de
forma algo distinta según el índice y el periodo exacto.)*

## Patrones que se repiten

- **El detonante siempre parece obvio en retrospectiva**, pero rara vez
  se ve venir con precisión de timing — motivo central por el que
  "salir del mercado antes de la caída" es casi imposible de ejecutar
  de forma sistemática y consistente.
- **La recuperación suele ser más rápida de lo que el pánico del momento
  hace pensar** — quien vende en el peor momento convierte una pérdida
  temporal (sobre el papel) en una pérdida permanente y real.
- **Cada crisis "parece distinta y peor"** en el momento — sensación
  normal, no información nueva sobre si debes cambiar de estrategia.
- **Las crisis de crédito/bancarias (1929, 2008) tardan más en
  recuperarse** que los shocks exógenos puros (2020) — la profundidad
  del daño estructural del sistema financiero importa más que la caída
  inicial.

## Por qué esto es más que historia académica para ti

Tu plan mezcla un horizonte largo (núcleo, 15-20 años — el tiempo
histórico suficiente para atravesar y recuperarse de cualquier crisis de
la tabla) con un horizonte corto y con fecha fija (reserva del negocio,
3-5 años — un plazo en el que, si coincide con algo como 2008 o 2000-02,
**no** habría dado tiempo a recuperarse antes de necesitar el dinero).
Es exactamente el razonamiento detrás de por qué esa reserva debe estar
en activos de bajo riesgo (ver
[Renta fija en profundidad](08-renta-fija-en-profundidad.md) y
[Política de inversión](../02-portfolio-inversion/01-politica-inversion.md)),
no en la misma cesta que el núcleo.

## Enlaces para profundizar

- [Federal Reserve History — panorama de crisis financieras en EEUU](https://www.federalreservehistory.org/)
- [Investopedia — 2008 Financial Crisis](https://www.investopedia.com/terms/f/financial-crisis.asp)
- [NBER — datador oficial de recesiones en EEUU](https://www.nber.org/research/business-cycle-dating)
