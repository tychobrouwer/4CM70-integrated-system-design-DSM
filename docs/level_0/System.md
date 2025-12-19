# System

## Relations

### TotalPowerModel

This model calculates the total power consumption of the system by summing the power consumption of its main components.

* **Model:** `TotalPowerModel`
* **Formula:**
  $$
  P_{total} = P_{core} + P_{cache}
  $$
  Where:
  * $P_{total}$ = `total-power-consumption`
  * $P_{core}$ = `core-power-consumption`
  * $P_{cache}$ = `cache-power-consumption`

* **Arguments:**
  * `core-power-consumption` (@weight 1): Power consumed by the processing core.
  * `cache-power-consumption` (@weight 1): Power consumed by the cache.

### EfficiencyModel

This model calculates the efficiency of the system based on its computational performance and power consumption.

* **Model:** `EfficiencyModel`
* **Formula:**
  $$
  E = \frac{P_{comp}}{P_{total}}
  $$
  Where:
  * $E$ = `efficiency`
  * $P_{comp}$ = `core-computational-performance`
  * $P_{total}$ = `total-power-consumption`

* **Arguments:**
  * `total-power-consumption` (@weight -1): Total power consumed by the system.
  * `core-computational-performance` (@weight 1): Computational performance of the core

### TotalDieAreaModel

This model calculates the total die area of the system by summing the die areas of its main components.

* **Model:** `TotalDieAreaModel`
* **Formula:**
  $$
  A_{total} = A_{core} + A_{cache}
  $$
  Where:
  * $A_{total}$ = `total-die-area`
  * $A_{core}$ = `core-die-area`
  * $A_{cache}$ = `cache-die-area`

* **Arguments:**
  * `core-die-area` (@weight 1): Die area occupied by the processing core.
  * `cache-die-area` (@weight 1): Die area occupied by the cache.
