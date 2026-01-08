# Shared Models

There are multiple models that are shared between different components in the system. This document describes these shared models and their relations.

## Relations

### BandwidthModel

This model calculates the peak bandwidth of core-cache interconnects.

* **Model:** `BandwidthModel`
* **Formula:**
  $$
  BW = N_{\text{bus_width_bytes}} \cdot f_{bus}
  $$
  Where:
  * $BW$ = `bandwidth`
  * $N_{\text{bus_width_bytes}}$ = `bus-width`
  * $f_{bus}$ = `frequency`
  
* **Arguments:**
  * `bus-width` (@weight 1): Wider bus increases bandwidth.
  * `frequency` (@weight 1): Higher frequency increases bandwidth.

### AreaModel

This model calculates the physical die area occupied by the cache based on transistor count and process technology.

* **Model:** `AreaModel`
* **Formula:**
  $$
  A = N_{transistors} \cdot f(L_{gate})^2
  $$
  Where:
  * $A$ = `die-area`
  * $N_{transistors}$ = `transistors`
  * $L_{gate}$ = `process-node`

* **Arguments:**
  * `transistors` (@weight 1): More transistors require proportionally more area.
  * `process-node` (@weight 2): Area scales quadratically with feature size (2D scaling).

### FrequencyModel

This model determines the maximum operating frequency of the cache based on voltage, temperature, and process node.

* **Model:** `FrequencyModel`
* **Formula:**
  $$
  f = \alpha \cdot \frac{(V - V_{th})^\beta}{T} \cdot \frac{1}{L_{gate}}
  $$
  Where:
  * $f$ = `clock-frequency`
  * $V$ = `voltage`
  * $T$ = `temperature`
  * $L_{gate}$ = `process-node`

* **Arguments:**
  * `voltage` (@weight 1): Higher voltage enables faster switching.
  * `temperature` (@weight -0.5): Higher temperature reduces carrier mobility.
  * `process-node` (@weight -1): Smaller nodes enable higher frequencies.

---

### CurrentModel

This model calculates the current drawn by the cache during active switching operations.

* **Model:** `CurrentModel`
* **Formula:**
  $$
  I \approx k_1 \cdot N_{transistors} \cdot f \cdot V \cdot \frac{1}{\sqrt{L_{gate}}} \cdot e^{k_2 \cdot T}
  $$
  Where:
  * $I$ = `current`
  * $N_{transistors}$ = `transistors`
  * $f$ = `clock-frequency`
  * $V$ = `voltage`
  * $T$ = `temperature`
  * $L_{gate}$ = `process-node`

* **Arguments:**
  * `transistors` (@weight 1): More transistors increase switching current.
  * `process-node` (@weight -0.5): Smaller nodes reduce capacitance per transistor.
  * `temperature` (@weight 2): Temperature strongly affects leakage and mobility (exponential).
  * `voltage` (@weight 1): Current scales linearly with voltage.
  * `clock-frequency` (@weight 1): Higher frequency increases switching events per second.

---

### PowerModel

This model calculates the power consumption of the component.

* **Model:** `PowerModel`
* **Formula:**
  $$
  P = V \cdot I
  $$
  Where:
  * $P$ = `power`
  * $V$ = `voltage`
  * $I$ = `current`

* **Arguments:**
  * `voltage` (@weight 1): Power scales linearly with voltage (for a given current).
  * `dynamic-current` (@weight 1): Power scales linearly with current.

---

### TotalPowerModel

This model sums the powers to get total power consumption.

* **Model:** `TotalPowerModel`
* **Formula:**
  $$
  P_{total} = P_1 + P_2
  $$
  Where:
  * $P_{total}$ = `power-consumption`
  * $P_1$ = `power-1`
  * $P_2$ = `power-2`

* **Arguments:**
  * `power-1` (@weight 1): Power consumed during active operations.
  * `power-2` (@weight 1): Power consumed in standby/idle state.

---

### PowerThermalModel

This model converts electrical power consumption into thermal load for thermal management analysis.

* **Model:** `PowerThermalModel`
* **Formula:**
  $$
  Q_{thermal} = P_{electrical}
  $$
  Where:
  * $Q_{thermal}$ = `thermal-load`
  * $P_{electrical}$ = `power-consumption`

* **Arguments:**
  * `power-consumption` (@weight 1): All electrical power is converted to heat.

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
