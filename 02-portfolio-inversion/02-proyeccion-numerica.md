# Proyección numérica

**Esto es matemática de interés compuesto sobre supuestos, no una
predicción.** Los mercados no dan un retorno constante año a año; esto
sirve para tener una intuición de magnitudes, no una cifra que "vas a
tener".

## Supuesto base

- Aportación (ejemplo): 2.500€/mes, constante, durante 48 meses (4 años).
- Total aportado sin crecimiento: **120.000€**.
- Aportación mensual, crecimiento compuesto mensual.

## Escenarios a 4 años (100% del ahorro, para ver el rango)

| Escenario | Retorno anual asumido | Valor estimado a los 4 años | Ganancia sobre lo aportado |
|---|---|---|---|
| Conservador | 4% | ~129.900€ | ~9.900€ |
| Base | 7% | ~138.000€ | ~18.000€ |
| Optimista | 10% | ~146.800€ | ~26.800€ |

```chart
{
  "type": "bar",
  "title": "Valor estimado a los 4 años (120.000€ aportados)",
  "unit": "€",
  "data": {"Conservador (4%)": 129900, "Base (7%)": 138000, "Optimista (10%)": 146800}
}
```

El 7% "base" es aproximadamente la media histórica real (ajustada a
inflación) de largo plazo de la bolsa estadounidense — no un mínimo
garantizado; hay periodos de 4 años históricos con rentabilidad negativa.

## Por qué el retorno real de tu cartera será menor que el 100% en núcleo

Con la política de tres cubos de
[Política de inversión](01-politica-inversion.md), no todo tu ahorro
está en el escenario de mayor retorno esperado: la reserva para el
negocio está deliberadamente en activos de bajo riesgo (retorno esperado
más bajo, ~1-3%) para protegerla de una caída justo cuando la necesites.

Ejemplo ilustrativo de cartera mixta (ajusta los pesos a tu decisión
real):

| Cubo | Peso | Retorno anual asumido |
|---|---|---|
| Núcleo (SP500/World) | 60% | 7% |
| Reserva negocio (bajo riesgo) | 25% | 2% |
| Satélite (acciones + cripto) | 15% | 10%* |

*Retorno esperado del satélite es la media asumida — la varianza real
individual es mucho mayor (puede ser fuertemente negativo o muy
positivo en 4 años; no tratar como un número fiable a nivel individual).

Retorno blended aproximado de esta mezcla: ~6.2% anual — más cerca del
escenario "conservador-base" que del "optimista", que es exactamente el
efecto esperado de proteger la reserva del negocio.

## Cómo usar esto en la práctica

1. Decide el importe objetivo de la reserva de negocio (parte 3).
2. Ajusta los pesos de la tabla anterior a tu situación real.
3. Recalcula con una hoja de cálculo o el propio código de Supertrader
   (`supertrader/optimizer.py` calcula retorno esperado/volatilidad
   reales por fondo con `PyPortfolioOpt`, más preciso que estos supuestos
   fijos).
4. Revisa la proyección cada 6-12 meses con datos reales, no la dejes
   fija cuatro años.
