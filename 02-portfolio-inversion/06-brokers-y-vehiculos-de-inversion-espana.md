# Brokers y vehículos de inversión en España

Un plan de inversión perfecto sobre el papel no sirve de nada si el
vehículo elegido tiene comisiones altas o el bróker no es fiable. Este
documento es la guía práctica de "dónde" ejecutar la política de
[Política de inversión](01-politica-inversion.md).

## Fondos indexados vs. ETFs: la decisión más importante

Ya se mencionó la diferencia fiscal en
[Fiscalidad de la inversión en España](../01-fundamentos-economia/03-fiscalidad-inversion-espana.md):
los fondos permiten traspasos entre sí sin tributar, los ETFs no. Para
el núcleo de largo plazo, donde es probable que rebalancees o ajustes el
vehículo con los años, esa ventaja fiscal suele pesar más que las
comisiones ligeramente más bajas de muchos ETFs. Para el satélite
(operaciones puntuales, menos traspasos), la diferencia importa menos.

## Roboadvisors españoles (gestión delegada low-cost)

- **Indexa Capital**: carteras de fondos indexados (Vanguard, Amundi...)
  con rebalanceo automático y gestión del traspaso fiscal, comisión de
  gestión reducida sobre lo gestionado.
- **MyInvestor**: roboadvisor y también broker directo (fondos y
  acciones/ETFs), respaldado por banco con ficha bancaria propia (Andbank
  España).
- **Finizens**: modelo similar a Indexa, carteras indexadas con
  rebalanceo automático.

Ventaja de un roboadvisor: cero fricción operativa (tú decides el perfil
de riesgo, ellos ejecutan y rebalancean). Desventaja: menos control
granular que gestionarlo tú mismo fondo a fondo con el optimizador de
Supertrader.

## Brokers para autogestión (ETFs y acciones)

- **Interactive Brokers (IBKR)**: comisiones muy bajas, acceso a
  mercados globales, interfaz menos amigable para principiantes.
- **DeGiro**: comisiones bajas, muy usado en Europa, buena opción para
  ETFs y acciones individuales del satélite.
- **MyInvestor**: para quien prefiera fondos indexados directamente sin
  pasar por un roboadvisor, con comisión de custodia competitiva.

## Qué mirar al comparar (más allá de "quién es más barato")

- **TER (Total Expense Ratio)**: comisión anual del propio fondo/ETF,
  independiente del bróker — impacta más a largo plazo que la comisión
  de compra-venta puntual.
- **Comisión de custodia**: algunos brokers la cobran, otros no —
  revisar la letra pequeña, no solo la comisión de operación.
- **Fondo de Garantía de Inversiones (FOGAIN) o equivalente**: cobertura
  en caso de quiebra del bróker (no del mercado) hasta un límite —
  verificar que el bróker elegido esté cubierto por un sistema de
  garantía reconocido en la UE/EEE.
- **Domicilio fiscal del bróker**: brokers no españoles pueden implicar
  gestión adicional en la declaración de la renta (modelo 720 si superan
  ciertos umbrales de activos en el extranjero) — a valorar con tu
  gestor fiscal.

## Ejemplo numérico: por qué 0,15% de diferencia en TER importa

Sobre 100.000€ invertidos durante 20 años a un retorno bruto del 7%
anual, la diferencia entre un fondo con TER 0,10% y uno con TER 0,25%
(ambos indexando lo mismo, ej. el mismo índice global):

| Fondo | TER | Retorno neto aprox. | Valor a los 20 años |
|---|---|---|---|
| Fondo A | 0,10% | 6,90% | ~386.000€ |
| Fondo B | 0,25% | 6,75% | ~373.000€ |

```chart
{
  "type": "bar",
  "title": "Valor a los 20 años sobre 100.000€ segun el TER",
  "unit": "€",
  "data": {"Fondo A (TER 0.10%)": 386000, "Fondo B (TER 0.25%)": 373000}
}
```

Una diferencia de comisión que parece insignificante (0,15 puntos)
se traduce en unos 13.000€ menos al final, solo por el efecto compuesto
de pagar un poco más cada año durante dos décadas — el motivo por el
que comparar el TER, no solo la comisión de compra-venta, es una de las
decisiones de mayor impacto a largo plazo de todo el plan.

## Recomendación de estructura, no de producto concreto

Este documento no sustituye comparar condiciones actuales (cambian con
frecuencia) antes de decidir. El criterio de decisión sí es estable:
núcleo en fondos indexados (por la ventaja fiscal de traspasos) en un
bróker/roboadvisor con comisión de gestión baja y buena cobertura de
garantía; satélite en un bróker de bajo coste por operación si vas a
gestionar acciones/ETFs individuales tú mismo.

## Enlaces para profundizar

- [CNMV — Registro oficial de entidades](https://www.cnmv.es/portal/consultas/EntidadesRegistrales.aspx)
- [FOGAIN — Fondo de Garantía de Inversiones](https://www.fogain.com/)
- [Bogleheads wiki — European investing](https://www.bogleheads.org/wiki/European_investing)
