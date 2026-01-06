# Core Cache Interconnect System

## Relations

### ThermalCoolingCapabilityModel

This is how much heat the coolant can carry away.

* **Model:** `ThermalCoolingCapabilityModel`
* **Formula:**
  $$
  Q = (dm/dt)*c_p*(T_o-T_i)
  $$  $$
  Where:
  * $Q$ = `cooling-capability`
  * $dm/dt$ = `coolant-flowrate`
  * *$c_p$ = `heat-capacity`
  * *$T_o$ = `input-temperature`
  * *$T_i$ = `output-temperature`
  
* **Arguments:**
  * `coolant-flowrate` (@weight 1): coolant flowrate
  * `input-temperature` (@weight 1): coolant temperature in
  * `output-temperature` (@weight 1): coolant temperature out
  * `heat-capacity` (@weight 1): heat capacity of coolant

---

### ThermalTimResistanceModel

The resistance to heat flow through the Thermal Interface Material (TIM) between the die and the heat spreader or heat sink.

* **Model:** `ThermalTimResistanceModel`
* **Formula:**
  $$
  R_{TIM} = \frac{d_{TIM}}{k_{TIM}*A} + R_{contact}
  $$
  Where:
  * $d_{TIM}$ = `tim-thickness`
  * $k_{TIM}$ = `tim-conductivity`
  * $A$ = `total-die-area`
  * $R_{TIM}$ = `tim-resistance`
  * $R_{contact}$ = `contact-resistance`

* **Arguments:**
  * `total-die-area` (@weight 1): total die area
  * `tim-thickness` (@weight 1): thickness of TIM
  * `tim-conductivity` (@weight 1): conductivity of TIM

---

### ThermalResistanceModel

The total thermal resistance to the cooler through the thermal TSVs and TIM.

* **Model:** `ThermalResistanceModel`
* **Formula:**
  $$
  R = \frac{1}{D*\pi*(d/2)^2*k} + R_{TIM} + R_{contact}
  $$
  Where:
  * $R$ = `thermal-resistance`
  * $D$ = `thermal-tsv-density`
  * $d$ = `thermal-tsv-diameter`
  * $k$ = `thermal-tsv-conductivity`
  * $R_{TIM}$ = `tim-resistance`

* **Arguments:**
  * `die-area` (@weight 1): die area
  * `tsv-density` (@weight 1): TSV density
  * `tsv-diameter` (@weight 1): TSV diameter
  * `tsv-thermal-conductivity` (@weight 1): TSV thermal conductivity
  * `tim-resistance` (@weight 1): TIM resistance

---

### ThermalCapabilityModel

This is the thermal capability of the core or cache given its thermal resistance and the cooling capability of the cooling system.

* **Model:** `ThermalCapabilityModel`
* **Formula:**
  $$
  Q_{capability} = \frac{Q_{cooling}}{R_{thermal}}
  $$
  Where:
  * $Q_{capability}$ = `core-cooling-capability` or `cache-cooling-capability`
  * $Q_{cooling}$ = `cooling-capability`
  * $R_{thermal}$ = `core-resistance` or `cache-resistance`

* **Arguments:**
  * `cooling-capability` (@weight 1): cooling capability
  * `core-resistance` (@weight 1): core thermal resistance to cooler
  * `cache-resistance` (@weight 1): cache thermal resistance to cooler
