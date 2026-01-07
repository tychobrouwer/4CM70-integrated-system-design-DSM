# Core Cache Interconnect System

## Relations

### ThermalCoolingCapabilityModel

This model calculates the heat removal capacity of the cooling system based on coolant properties and flow characteristics.

* **Model:** `ThermalCoolingCapabilityModel`
* **Formula:**
  $$
  Q_{cool} = \dot{m} \cdot c_p \cdot (T_{out} - T_{in})
  $$
  Where:
  * $Q_{cool}$ = `cooling-capability` (heat removal capacity)
  * $\dot{m}$ = `coolant-flowrate` (mass flow rate of coolant)
  * $c_p$ = `coolant-specific-heat` (specific heat capacity of coolant)
  * $T_{out}$ = `coolant-outlet-temperature` (temperature leaving heat exchanger)
  * $T_{in}$ = `coolant-inlet-temperature` (temperature entering heat exchanger)

* **Arguments:**
  * `coolant-flowrate` (@weight 1): Higher flow rate increases heat removal capacity linearly.
  * `coolant-inlet-temperature` (@weight -1): Lower inlet temperature increases cooling effectiveness.
  * `coolant-outlet-temperature` (@weight 1): Higher outlet temperature indicates more heat absorbed.
  * `coolant-specific-heat` (@weight 1): Higher specific heat allows more energy absorption per unit mass.

---

### ThermalCapabilityModel

This model distributes the total cooling capability between the core and cache components based on their respective thermal resistances to the cooler.

* **Model:** `ThermalCapabilityModel`
* **Formula:**
  $$
  Q_{core} = \frac{Q_{cool}}{R_{core}} \quad , \quad Q_{cache} = \frac{Q_{cool}}{R_{cache}}
  $$
  Where:
  * $Q_{core}$ = `core-capability` (maximum heat dissipation capability for core)
  * $Q_{cache}$ = `cache-capability` (maximum heat dissipation capability for cache)
  * $Q_{cool}$ = `cooling-capability` (total cooling system capacity)
  * $R_{core}$ = `core-resistance` (thermal resistance from core to cooler)
  * $R_{cache}$ = `cache-resistance` (thermal resistance from cache to cooler)

* **Arguments:**
  * `cooling-capability` (@weight 1): Total heat removal capacity available.
  * `core-resistance` (@weight -1): Lower resistance enables higher heat dissipation from core.
  * `cache-resistance` (@weight -1): Lower resistance enables higher heat dissipation from cache.

---

### ThermalResistanceModel

This model calculates the total thermal resistance from a die (core or cache) to the cooler through thermal TSVs and thermal interface material.

* **Model:** `ThermalResistanceModel`
* **Formula:**
  $$
  R_{total} = R_{TSV} + R_{TIM}
  $$
  $$
  R_{TSV} = \frac{1}{N_{TSV} \cdot k_{TSV} \cdot A_{TSV}}
  $$
  Where:
  * $R_{total}$ = `thermal-resistance` (total thermal resistance to cooler)
  * $R_{TSV}$ = Thermal resistance through TSV array
  * $R_{TIM}$ = `tim-resistance` (thermal interface material resistance)
  * $N_{TSV}$ = Number of thermal TSVs (from `tsv-density` × `die-area`)
  * $k_{TSV}$ = `tsv-thermal-conductivity`
  * $A_{TSV}$ = Cross-sectional area of TSVs (function of `tsv-diameter`)

* **Arguments:**
  * `die-area` (@weight -1): Larger die area allows more TSVs, reducing resistance.
  * `tsv-density` (@weight -1): Higher TSV density provides more parallel thermal paths.
  * `tsv-diameter` (@weight -1): Larger diameter TSVs have lower thermal resistance.
  * `tsv-thermal-conductivity` (@weight -1): Higher conductivity reduces thermal resistance.
  * `tim-resistance` (@weight 1): TIM resistance adds to total thermal path.

---

### ThermalTimResistanceModel

This model calculates the thermal resistance of the Thermal Interface Material (TIM) layer between the die and the heat spreader or heat sink.

* **Model:** `ThermalTimResistanceModel`
* **Formula:**
  $$
  R_{TIM} = \frac{d_{TIM}}{k_{TIM} \cdot A_{die}} + R_{contact}
  $$
  Where:
  * $R_{TIM}$ = `tim-resistance` (total TIM thermal resistance)
  * $d_{TIM}$ = `tim-thickness` (thickness of TIM layer)
  * $k_{TIM}$ = `tim-conductivity` (thermal conductivity of TIM material)
  * $A_{die}$ = `die-area` (total die area for heat transfer)
  * $R_{contact}$ = `contact-resistance` (interfacial thermal resistance)

* **Arguments:**
  * `die-area` (@weight -1): Larger area reduces thermal resistance (inverse relationship).
  * `tim-thickness` (@weight 1): Thicker TIM increases thermal resistance.
  * `tim-conductivity` (@weight -1): Higher conductivity TIM reduces resistance.
  * `contact-resistance` (@weight 1): Imperfect surface contact adds resistance.

---
