# Shared Models

There are multiple models that are shared between different components in the system. This document describes these shared models and their relations.

## Relations

### AreaModel

This model calculates the area of the cache based the number of transistors and the process node.

* **Model:** `AreaModel`
* **Formula:**
  $$
  A = N_{\text{transistors}} \cdot f(L_{gate})
  $$
  Where:
  * $A$ = `area`
  * $N_{\text{transistors}}$ = `number-of-transistors`
  * $L_{gate}$ = `process-node`
  
* **Arguments:**
  * `number-of-transistors` (@weight 1): Total number of transistors.
  * `process-node` (@weight 1): Represents the process node factor.

---

### FrequencyModel

This model determines the operational clock frequency as a function of voltage, temperature, and the manufacturing process node.

* **Model:** `FrequencyModel`
* **Formula:**
  $$
  f = \alpha \cdot \frac{(V - V_{th})^\beta}{T} \cdot \frac{1}{f(L_{gate})}
  $$
  Where:
  * $f$ = `clock-frequency`
  * $V$ = `voltage`
  * $T$ = `temperature`
  * $L_{gate}$ = `process-node`

* **Arguments:**
  * `voltage` (@weight 1): Operating voltage.
  * `temperature` (@weight 1): Operating temperature.
  * `process-node` (@weight -1): Represents the process node factor.

---

### CurrentModel

This model calculates the total electrical current drawn by the component, accounting for both dynamic switching and static leakage.

* **Model:** `CurrentModel`
* **Formula:**
  $$
  I = I_{dynamic} + I_{static} \approx (k_1 \cdot N \cdot f \cdot V) + (k_2 \cdot N \cdot e^{k_3 \cdot T})
  $$
  Where:
  * $I$ = `current`
  * $N$ = `transistors`
  * $f$ = `clock-frequency`
  * $V$ = `voltage`
  * $T$ = `temperature`

* **Arguments**
  * `transistors` (@weight 1): Total number of transistors.
  * `process-node` (@weight -0.5): Manufacturing process node.
  * `temperature` (@weight 2): Operating temperature.
  * `clock-frequency` (@weight 1): Operating clock frequency.
  * `voltage` (@weight 1): Operating voltage.
  
---

### PowerModel

This model calculates the power consumption based on voltage and current.

* **Model:** `PowerModel`
* **Formula:**
  $$
  P = V \cdot I
  $$
  Where:
  * $P$ = `power-consumption`
  * $V$ = `voltage`
  * $I$ = `current`

* **Arguments:**
  * `voltage` (@weight 1): Operating voltage.
  * `current` (@weight 1): Operating current.

---

### PowerThermalModel

This model transforms the electrical power consumption of the cache into a thermal load based (power -> thermal power).

* **Model:** `PowerThermalModel`
* **Formula:**
  $$
  P_{\text{cons}} = Q_{\text{load}}
  $$
  Where:
  * $P_{\text{cons}}$ = `power-consumption`
  * $Q_{\text{load}}$ = `thermal-load`

* **Arguments:**
  * `power-consumption` (@weight 1): Power consumption.
  * `thermal-load` (@weight 1): Thermal load.

---

### PowerConsumptionRelation

This relation connects max power consumption to the thermal cooling capacity and electrical power capacity.

* **Relation:** `PowerConsumptionRelation`
* **Formula:**
  $$
  P_{max} \leq Q_{cooling} \text{ and } P_{max} \leq Q_{thermal}
  $$
  Where:
  * $P_{max}$ = `max-power-consumption`
  * $Q_{cooling}$ = `cooling-capacity`
  * $P_{capacity}$ = `power-capacity`

* **Arguments:**
  * `cooling-capacity` (@weight 1): Cooling system capacity.
  * `power-capacity` (@weight 1): Power supply capacity.

---

### TemperatureModel

This model estimates the operating temperature of the cache based on thermal load, resistance to cooler, and ambient conditions.

* **Model:** `TemperatureModel`
* **Formula:**
  $$
  T = T_{ambient} + Q_{load} \cdot R_{th}
  $$
  Where:
  * $T$ = `temperature`
  * $T_{ambient}$ = `ambient-temperature`
  * $Q_{load}$ = `thermal-load`
  * $R_{th}$ = `thermal-resistance`

* **Arguments:**
  * `thermal-load` (@weight 1): Thermal load.
  * `thermal-resistance` (@weight 1): Thermal resistance.
  * `ambient-temperature` (@weight 1): Ambient temperature.

---

