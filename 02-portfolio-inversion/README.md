# 02 — Portfolio y plan de inversión

Plan de inversión para un ahorro mensual constante (ejemplo: 2.500€/mes) durante los
próximos 4 años, con un objetivo adicional que lo diferencia de un plan
de inversión genérico: parte de ese dinero necesita estar disponible en
3-5 años para financiar el lanzamiento de la clínica ([ver parte 3](../03-negocio-medicina-estetica/README.md)).

![Analizando el crecimiento de una cartera](../assets/img/analisis-monedas.jpg)
*Revisar la cartera es un hábito de baja frecuencia, no un pasatiempo diario — trimestral basta.*

1. [Política de inversión](01-politica-inversion.md) — la estrategia:
   núcleo, satélite, y el cubo reservado para el negocio.
2. [Proyección numérica](02-proyeccion-numerica.md) — cuánto podría
   crecer el ahorro en distintos escenarios, con cálculos explícitos.

La fiscalidad de plusvalías y Patrimonio ya está cubierta en
[Fiscalidad de la inversión en España](../01-fundamentos-economia/03-fiscalidad-inversion-espana.md),
no se repite aquí.

## Para profundizar durante el año

3. [Teoría moderna de carteras](03-teoria-moderna-de-carteras.md) —
   Markowitz, correlación y cómo funciona el optimizador de Supertrader.
4. [Rebalanceo: estrategias avanzadas](04-rebalanceo-estrategias-avanzadas.md) —
   por calendario vs. por banda, y el coste fiscal de rebalancear.
5. [DCA vs. pago único](05-dca-vs-pago-unico.md) — qué dice la evidencia
   y por qué tu caso es DCA "forzoso".
6. [Brokers y vehículos de inversión en España](06-brokers-y-vehiculos-de-inversion-espana.md) —
   roboadvisors, brokers de autogestión y qué mirar de verdad.
7. [Comportamiento del inversor en crisis](07-comportamiento-del-inversor-en-crisis.md) —
   checklist de reacción para el día que el mercado caiga con fuerza.
8. [Independencia financiera y FIRE](08-independencia-financiera-y-fire.md) —
   la regla del 4% y cómo se conecta (o no) con tu plan de negocio.
9. [Plan de contingencia y gestión de riesgo](09-plan-de-contingencia-y-gestion-de-riesgo.md) —
   fondo de emergencia, seguros de persona clave y escenarios alternativos.

## Relación con Supertrader

Este es el documento de **estrategia** (el qué y el por qué). La
**ejecución** — calcular el reparto exacto cada mes según precios reales,
registrar cada aportación, ver el valor actual de la cartera y probar
simulacros — se hace con la herramienta
Supertrader, un proyecto de software aparte. Antes
de aportar cada mes, la política de aquí define *qué* fondos y *qué*
porcentaje máximo de satélite configurar en `config.yaml` de Supertrader;
Supertrader calcula el resto.
