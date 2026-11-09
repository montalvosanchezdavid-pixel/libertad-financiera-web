# Ciclo económico e indicadores líderes

En [macroeconomía básica](01-macroeconomia.md) viste la idea de ciclo
económico (expansión-pico-contracción-suelo). Aquí se profundiza en
**cómo se mide dónde estamos en ese ciclo** — sin caer en la trampa de
usarlo para intentar predecir el mercado a corto plazo, algo que ni los
profesionales consiguen de forma consistente.

## Tres tipos de indicadores

- **Adelantados (leading)**: cambian antes que la economía en conjunto.
  Sirven para anticipar, no para confirmar lo que ya pasó.
- **Coincidentes (coincident)**: se mueven a la vez que la economía —
  confirman el estado actual.
- **Rezagados (lagging)**: cambian después — confirman una tendencia ya
  instalada, útiles para validar en retrospectiva, no para actuar sobre
  ellos.

## Ejemplos concretos

| Tipo | Indicador | Qué mide |
|---|---|---|
| Adelantado | Curva de tipos (`T10Y2Y`) | Expectativas del mercado sobre tipos futuros |
| Adelantado | PMI (índice de gestores de compras) | Actividad manufacturera/servicios, encuesta mensual |
| Adelantado | Permisos de construcción | Inversión futura del sector inmobiliario |
| Adelantado | Confianza del consumidor | Predisposición futura a gastar |
| Coincidente | Producción industrial (`INDPRO`) | Actividad económica real, en tiempo casi real |
| Coincidente | Ventas minoristas | Consumo actual |
| Rezagado | Tasa de desempleo | Las empresas despiden/contratan después de que cambia la actividad |
| Rezagado | IPC / inflación | Los precios tardan en reflejar cambios de demanda/oferta |

Varios de estos (`T10Y2Y`, `INDPRO`, `CPIAUCSL`) ya son los que usa el
módulo Macro de Supertrader — este documento es el porqué detrás de esos
indicadores concretos, no una lista nueva.

## Por qué no usar esto para "hacer market timing"

Aunque los indicadores adelantados anticipan tendencia, no dan una señal
de compra/venta precisa: la bolsa suele moverse **antes** de que el
indicador confirme el giro (el mercado es en sí mismo un indicador
adelantado de la economía). Históricamente, intentar entrar y salir del
mercado según estas señales genera peor resultado que quedarse invertido
de forma sistemática — es el argumento de fondo, junto con
[Historia de crisis financieras](10-historia-de-crisis-financieras.md),
de por qué tu política de inversión no incluye "vender si la macro se ve
mal".

## Ejemplo práctico: leer un "panel" de indicadores

Imagina que en un momento dado observas esta combinación de señales:

| Indicador | Lectura | Lo que sugiere |
|---|---|---|
| Curva de tipos (`T10Y2Y`) | Invertida desde hace 6 meses | Los mercados esperan que el banco central baje tipos — señal clásica de alerta |
| PMI manufacturero | Por debajo de 50 y bajando | Contracción de actividad industrial |
| Desempleo | Estable, todavía bajo | La economía real aún no lo refleja (es rezagado) |
| Confianza del consumidor | Cayendo tres meses seguidos | El gasto discrecional podría enfriarse pronto |

Lectura conjunta razonable: hay señales adelantadas de posible
desaceleración, aunque los datos "duros" (desempleo) todavía no lo
confirman — es exactamente el patrón que precede a muchas de las
recesiones de
[Historia de crisis financieras](10-historia-de-crisis-financieras.md).
**Lo que esto no te dice** es cuándo exactamente, ni cuánto va a caer el
mercado, ni si ya está descontado en los precios actuales — de ahí que
la conclusión práctica sea "mantener el rumbo con más atención al
contexto", no "vender y esperar".

## Uso correcto: contexto, no gatillo

El valor real de estos indicadores es cualitativo:
- Entender **por qué** se mueve el mercado, no predecir el siguiente
  movimiento.
- Detectar si el contexto macro apoya o dificulta el momento de abrir el
  negocio (ej. desempleo subiendo → gasto discrecional más débil →
  peor momento para lanzar un negocio que depende de gasto no esencial,
  ver [el apartado de desempleo](01-macroeconomia.md#desempleo) de macroeconomía básica).
- Dar marco a conversaciones informadas, no señales automáticas de
  trading.

## Enlaces para profundizar

- [FRED — series de indicadores líderes](https://fred.stlouisfed.org/release?rid=12)
- [The Conference Board — Leading Economic Index](https://www.conference-board.org/topics/us-leading-indicators)
- [Investopedia — Leading vs Lagging Indicators](https://www.investopedia.com/terms/l/leadingindicator.asp)
