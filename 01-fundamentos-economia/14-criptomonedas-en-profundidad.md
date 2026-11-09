# Criptomonedas en profundidad

En [mercados financieros](02-mercados-financieros.md) quedó claro
que cripto es satélite, nunca núcleo, por su volatilidad y falta de
flujo de caja. Aquí se profundiza porque "satélite" no significa
"informal" — merece el mismo rigor que cualquier otra posición.

## Qué es blockchain, en una frase

Un libro de contabilidad distribuido entre muchos ordenadores, donde
añadir una entrada nueva requiere el acuerdo de la red según unas reglas
(consenso), sin que una autoridad central lo controle. Bitcoin fue la
primera aplicación (moneda); Ethereum añadió "contratos inteligentes"
(programas que se ejecutan en la propia red).

## Por qué no genera flujo de caja

A diferencia de una acción (beneficios de una empresa) o un bono (cupón
de un emisor), la mayoría de criptomonedas no representan un derecho
sobre flujos futuros de nada — su valor depende enteramente de que
alguien más esté dispuesto a pagar más por ella en el futuro (teoría del
"mayor tonto", cuando es puramente especulativo) o de la utilidad real
de la red subyacente (cuando hay un caso de uso genuino). Esto no
significa que no tenga valor, pero sí que no se puede valorar con los
mismos modelos que una empresa (ver
[Análisis fundamental básico](09-analisis-fundamental-basico.md)).

## Bitcoin vs. altcoins

- **Bitcoin**: el más establecido, con la tesis más simple ("oro
  digital", reserva de valor descentralizada con oferta limitada a 21
  millones).
- **Altcoins** (Ethereum y miles más): mayor riesgo y mayor dispersión
  de resultados — desde proyectos con adopción real hasta esquemas sin
  ningún valor subyacente. Cuanto más se aleja del proyecto establecido,
  mayor debe ser el escrutinio antes de destinarle una sola parte, por
  pequeña, del satélite.

## Custodia: el riesgo que no es de mercado

- **Exchange (Binance, Coinbase...)**: cómodo, pero no posees las claves
  privadas — si el exchange quiebra o sufre un hackeo, puedes perderlo
  todo (ha pasado repetidamente en la historia del sector).
- **Wallet propia (hardware o software)**: tú controlas las claves
  privadas — mayor seguridad frente al exchange, pero la responsabilidad
  de no perderlas (o que te las roben) es enteramente tuya, sin ningún
  fondo de garantía detrás.
- Para importes pequeños de satélite, un exchange regulado en la UE
  puede ser proporcional; para importes mayores, moverlo a wallet propia
  reduce el riesgo de contraparte.

## Ejemplo real: la volatilidad de Bitcoin en números

| Fecha | Precio aprox. Bitcoin | Variación |
|---|---|---|
| Noviembre 2021 (máximo del ciclo) | ~69.000$ | — |
| Noviembre 2022 (mínimo del ciclo) | ~15.500$ | ~-78% desde el máximo |
| Marzo 2024 (nuevo máximo) | ~73.000$ | ~+370% desde el mínimo de 2022 |

```chart
{
  "type": "bar",
  "title": "Precio de Bitcoin: pico, valle y recuperación ($)",
  "unit": "$",
  "data": {"Nov. 2021 (máximo)": 69000, "Nov. 2022 (mínimo)": 15500, "Marzo 2024 (nuevo máximo)": 73000}
}
```

Una caída del 78% significa que, para volver al punto de partida, hace
falta una subida posterior de más del 350% — la asimetría matemática
entre pérdidas y ganancias necesarias para recuperarlas es más brutal
cuanto mayor es la caída. Compárese con el S&P 500, cuya peor caída
histórica reciente (2008) fue de ~-57%, ya de por sí severa: la
volatilidad de cripto es de otro orden de magnitud, y es exactamente
la razón numérica (no solo la opinión) detrás de mantenerlo como
satélite de peso limitado.

## Regulación: MiCA

La Unión Europea aprobó el reglamento MiCA (Markets in Crypto-Assets),
en vigor progresivamente desde 2024, que obliga a los exchanges a
operar bajo licencia y supervisión — reduce (no elimina) el riesgo de
fraude/quiebra desordenada frente a la era casi sin regulación de años
anteriores.

## Fiscalidad: matiz importante

Ya viste en
[Fiscalidad de la inversión en España](03-fiscalidad-inversion-espana.md)
que las plusvalías tributan en la base del ahorro. Con cripto hay un
matiz: **una permuta cripto-cripto (cambiar Bitcoin por Ethereum, sin
pasar por euros) también es una operación sujeta a tributación** en
España — a diferencia de lo que mucha gente asume. Llevar registro de
cada operación (fecha, precio de compra/venta en euros) es necesario
para declarar correctamente.

## Enlaces para profundizar

- [CNMV y Banco de España — advertencia conjunta sobre criptoactivos](https://www.cnmv.es/)
- [Investopedia — What Is Blockchain?](https://www.investopedia.com/terms/b/blockchain.asp)
- [Unión Europea — Reglamento MiCA](https://finance.ec.europa.eu/digital-finance/markets-crypto-assets-regulation-mica_en)
