### CoolantFlowrateModel

This is the rate at which water or dielectric fluid is pumped through the cold plate or micro-channels.

* **Model:** `CoolantFlowrateModel`
* **Formula:**
  $$
  dm/dt = \frac{Q}{c_p*(T_o-T_i)}
  $$
  Where:
  * $dm/dt$ = `coolant flowrate`
  * $Q$ = `heat`
  * *$c_p$ = `heat capacity`
  * *$T_o$ = `temperature in`
  * *$T_i$ = `temperature out`
  
* **Arguments:**
  * `heat` (@weight 1): heat
  * `input-temperature` (@weight -1): coolant temperature in
  * `output-temperature` (@weight -1): coolant temperature out
  * `heat-capacity` (@weight -1): heat capacity of coolant

---
### AmbientInputTemperatureModel

This is the temperature of the air or fluid before it touches the chip. It sets the baseline.

* **Model:** `AmbientInputTemperatureModel`
* **Formula:**
  $$
  T_a = \frac{T_c}{P_{tot}*R_{tot}}
  $$
  Where:
  * $T_a$ = `ambient temperature`
  * $T_c$ = `core temperature`
  * *$P_{tot}$ = `power dissipated`
  * *$R_{tot}$ = `total thermal resistance`
  
* **Arguments:**
  * `core-temperature` (@weight 1): temperature of core
  * `power-dissipated` (@weight -1): power that dissipates
  * `thermal-resistance` (@weight -1): thermal resistance

---
### LateralThermalConductivityModel

How well heat spreads sideways.

* **Model:** `LateralThermalConductivityModel`
* **Formula:**
  $$
  k_{xy} = -\frac{q_x}{A*(dT/dx)}
  $$
  Where:
  * $k_{xy}$ = `lateral thermal conductivity`
  * $q_x$ = `heat flow`
  * *$A$ = `area`
  * *$dT/dx$ = `temperature gradient`
  
* **Arguments:**
  * `heat-flow` (@weight 1): flow of heat
  * `area` (@weight -1): area
  * `temperature-gradient` (@weight -1): change of temperature with distance

---
### ThermalInterfaceMaterialModel

The material between the dies. In 3D stacking, one might use "Hybrid Bonding" (Copper-to-Copper), which eliminates the TIM entirely, or micro-bumps with underfill.

* **Model:** `ThermalInterfaceMaterialModel`
* **Formula:**
  $$
  BLT = k_{TIM}*A*(R_{TIM}-R_{contact})
  $$
  Where:
  * $BLT$ = `bond line thickness`
  * $k_{TIM}$ = `thermal conductivity`
  * *$A$ = `area`
  * *$R_{TIM}$ = `TIM resistance`
  * *$R_{contact}$ = `conntact resistance`
  
* **Arguments:**
  * `tim-resistance` (@weight 1): thermal interface material resistance
  * `contact-resistance` (@weight 1): contact resistance
  * `area` (@weight 1): area of contact
  * `thermal-conductivity` (@weight 1): conductivity of interface material

---