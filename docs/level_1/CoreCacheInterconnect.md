# Core Cache Interconnect System

## Relations

### InterconnectBandwidthModel

This model calculates the peak bandwidth of core-cache interconnects.

* **Model:** `InterconnectBandwidthModel`
* **Formula:**
  $$
  BW = N_{\text{bus_width_bytes}} \cdot f_{bus}
  $$
  Where:
  * $BW$ = `Bandwidth of the interconnect`
  * $N_{\text{bus_width_bytes}}$ = `bus-width`
  * $f_{bus}$ = `frequency`
  
* **Arguments:**
  * `bus-width` (@weight 1): Data bus width in bytes per cycle
  * `frequency` (@weight 1): Core frequency

---

### InterconnectLatencyModel

This very simplified model gives an indication of the latency of an interconnect.

* **Model:** `InterconnectLatencyModel`
* **Formula:**
  $$
  t = \frac{L}{v} + \frac{S}{N_{bus_width_bytes}*f_{bus}}
  $$
  Where:
  * $t$ = `Latency of the interconnect`
  * $S$ = 'Size of file transfer' (architecture-independent, unimportant for DSM)
  * *v* = 'Signal velocity' (architecture-independent, unimportant for DSM)
  * $L$ = 'length'
  * $N_{\text{bus_width_bytes}}$ = `bus-width`
  * $f_{bus}$ = `frequency`
  
* **Arguments:**
  * `length` (@weight 1): physical length of the interconnect
  * `bus-width` (@weight -1): Data bus width in bytes per cycle
  * `frequency` (@weight -1): Core frequency

---