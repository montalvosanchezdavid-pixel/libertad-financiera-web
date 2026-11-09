# Política de inversión

**Horizonte:** 4 años de aportación (ejemplo: 2.500€/mes = 30.000€/año, 120.000€ aportados en total sin contar crecimiento).
**Particularidad:** dentro de ese mismo periodo (3-5 años), una parte de
este dinero puede necesitarse como capital semilla para la clínica. Eso
significa que este NO es un plan de inversión de un solo horizonte
temporal — son dos objetivos con perfiles de riesgo distintos mezclados
en el mismo ahorro mensual, y hay que separarlos explícitamente o el
diseño de cartera será incoherente.

## Los tres cubos

### 1. Núcleo — crecimiento a largo plazo

Fondos indexados amplios (SP500 / MSCI World / All-World), el estilo que
ya calcula el optimizador de Supertrader por Sharpe ratio. Este dinero
**no** tiene fecha de salida fija: sigue invertido más allá de los 4
años, es la base de tu libertad financiera a 15-20 años vista, no del
negocio.

Volatilidad asumible alta porque el horizonte real es largo — una caída
del 30% en el año 3 no obliga a vender si no necesitas ese dinero hasta
dentro de 15 años.

### 2. Reserva — capital semilla del negocio

Esta es la parte que cambia todo el planteamiento: si sabes que en 3-5
años vas a necesitar sacar una cantidad concreta para abrir la clínica,
ese dinero **no puede estar sujeto al mismo riesgo que el núcleo**. Un
mal momento de mercado justo cuando necesitas retirarlo (ej. una caída
del 25% el año que decides abrir) sería el peor timing posible.

Recomendación de diseño (ajusta el importe a lo que estimes que cuesta
montar la clínica, ver
[Proyección financiera](../03-negocio-medicina-estetica/05-proyeccion-financiera.md)):
- Define primero cuánto capital necesitarás para el lanzamiento.
- Ese importe, según se acerque la fecha, va migrando de renta variable
  a activos de bajo riesgo y alta liquidez (cuentas remuneradas, fondos
  monetarios, renta fija a corto plazo) — cuanto más cerca el año 3-5,
  menos riesgo de mercado debe tener este cubo.
- El resto del ahorro mensual, una vez cubierto ese objetivo, va al
  núcleo de largo plazo.

### 3. Satélite — alto riesgo, tamaño limitado

Acciones individuales y criptomonedas. Aquí sí se acepta perder el 100%
de esta porción sin que afecte al plan: por eso su peso debe ser un
límite fijo y explícito, no algo que crece si "va bien".

Referencia de punto de partida (ajustable según tu tolerancia real, no
la que crees tener hasta la primera caída fuerte):
- Satélite total: 10-15% del ahorro destinado al núcleo (no de todo el ahorro mensual, solo de la porción de largo plazo).
- Dentro del satélite, cripto acotado aparte (ej. máximo 1/3 del
  satélite) por su volatilidad muy superior incluso a acciones
  individuales.

## Ejemplo numérico: 2.500€/mes repartidos

Con un reparto ilustrativo 60% núcleo / 25% reserva negocio / 15%
satélite (los porcentajes exactos son tu decisión, ver más abajo):

| Cubo | % | Importe mensual | Importe acumulado a 4 años (sin contar rentabilidad) |
|---|---|---|---|
| Núcleo | 60% | 1.500€ | 72.000€ |
| Reserva negocio | 25% | 625€ | 30.000€ |
| Satélite | 15% | 375€ | 18.000€ |
| **Total** | **100%** | **2.500€** | **120.000€** |

```chart
{
  "type": "stacked",
  "title": "Reparto ilustrativo de 2.500€/mes",
  "unit": "€",
  "data": {"Núcleo": 1500, "Reserva negocio": 625, "Satélite": 375}
}
```

Ver
[Proyección numérica](02-proyeccion-numerica.md)
para cómo crece cada cubo con rentabilidad real aplicada, no solo la
suma de aportaciones.

## Cómo se traduce esto en Supertrader

`config.yaml` de Supertrader ya soporta `min_weight`/`max_weight` por
fondo y categorías (`category`) libres. La forma de implementar esta
política ahí:
1. Añadir los tickers del satélite (acciones/cripto vía ETF, ya que
   Supertrader trabaja con yfinance) con `category: satelite` y un
   `max_weight` bajo por fondo.
2. Los fondos núcleo (SP500/World) con `category: nucleo`.
3. La reserva de negocio, al ser de bajo riesgo/corto plazo, no encaja
   bien en el optimizador de media-varianza (pensado para renta
   variable) — gestionarla aparte, fuera de Supertrader, en una cuenta
   remunerada o fondo monetario.

## Rebalanceo

Revisión trimestral: si el satélite ha crecido por encima de su límite
(porque ha subido mucho), vender el exceso y reforzar el núcleo — no al
revés. Es la disciplina que evita que "una posición que va bien" se
convierta sin darte cuenta en la mitad de la cartera.

## Lo que este documento no decide por ti

Los porcentajes exactos (cuánto núcleo vs. satélite, cuánto reservar
para el negocio) son una decisión personal que depende de tu tolerancia
real al riesgo y de la cifra concreta que necesites para la clínica.
Este documento da el marco; los números se revisan y ajustan según
avances en la parte 3.
