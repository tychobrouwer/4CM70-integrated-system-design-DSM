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

### InterconnectLengthModel2D

This very simplified model gives an indication of the length an interconnect has to be in a 2D architecture. It does not have a specific formula, but we know that the interconnect length scales with the square root of die area. We also know that the process node has influence on the mean interconnect length, as the smaller features are, the shorter interconnects will be.

* **Model:** `InterconnectLatencyModel`
* **Formula:**
  $$
  L = \sqrt{A_{die}} * \sqrt{N_{process_node}}
  $$
  Where:
  * $L$ = `Length of the interconnect`
  * $A_{die}$ = `Die area of cpu`
  * *$N_{process_node}$ = `Factor for influence of the process node
  
* **Arguments:**
  * `die-area` (@weight 0.5): area of the die
  * `process-node` (@weight 0.5): Process node that is used in manufacturing

---


### InterconnectLengthModel3D

This very simplified model gives an indication of the length an interconnect has to be in a 3D architecture. It does not have a specific formula, but we know that the interconnect length scales with the square root of die area. We also know that the process node has influence on the mean interconnect length, as the smaller features are, the shorter interconnects will be. Because core and cache are stacked on top of each other in a 3D architecture, this has a smaller influence than in a 2D situation.

* **Model:** `InterconnectLatencyModel`
* **Formula:**
  $$
  L = \sqrt{A_{die}} * N_{process_node}^{/frac{1}{4}}
  $$
  Where:
  * $L$ = `Length of the interconnect`
  * $A_{die}$ = `Die area of cpu`
  * *$N_{process_node}$ = `Factor for influence of the process node
  
* **Arguments:**
  * `die-area` (@weight 0.5): area of the die
  * `process-node` (@weight 0.25): Process node that is used in manufacturing

---
