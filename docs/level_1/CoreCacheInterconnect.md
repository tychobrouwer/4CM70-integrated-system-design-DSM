# Core Cache Interconnect System

## Relations

### InterconnectLatencyModel

This very simplified model gives an indication of the latency of an interconnect.

* **Model:** `InterconnectLatencyModel`
* **Formula:**
  $$
  t = \frac{L}{v} + \frac{S}{N_{bus_width}*f_{bus}}
  $$
  Where:
  * $t$ = Latency of the interconnect
  * $S$ = 'Size of file transfer' (architecture-independent, unimportant for DSM)
  * *v* = 'Signal velocity' (architecture-independent, unimportant for DSM)
  * $L$ = Physical length of the interconnect
  * $N_{bus_width}$ = Bus width
  * $f_{bus}$ = Interconnect frequency

* **Arguments:**
  * `length` (@weight 1)
  * `bus-width` (@weight -1)
  * `frequency` (@weight -1)

---

### InterconnectLengthModel2D

This very simplified model gives an indication of the length an interconnect has to be in a 2D architecture. It does not have a specific formula, but we know that the interconnect length scales with the square root of die area. We also know that the process node has influence on the mean interconnect length, as the smaller features are, the shorter interconnects will be.

* **Model:** `InterconnectLengthModel2D`
* **Formula:**
  $$
  l = \sqrt{A_{die}} * \sqrt{N_{process_node}}
  $$
  Where:
  * $l$ = Length of the interconnect
  * $A_{die}$ = Die area of CPU
  * *$N_{process_node}$ = Factor for influence of the process node
  
* **Arguments:**
  * `die-area` (@weight 0.5)
  * `process-node-factor` (@weight 0.5)

---

### InterconnectLengthModel3D

This very simplified model gives an indication of the length an interconnect has to be in a 3D architecture. It does not have a specific formula, but we know that the interconnect length scales with the square root of die area. We also know that the process node has influence on the mean interconnect length, as the smaller features are, the shorter interconnects will be. Because core and cache are stacked on top of each other in a 3D architecture, this has a smaller influence than in a 2D situation.

* **Model:** `InterconnectLengthModel3D`
* **Formula:**
  $$
  l = \sqrt{A_{die}} * N_{process_node}^{/frac{1}{4}}
  $$
  Where:
  * $l$ = `length`
  * $A_{die}$ = `die-area`
  * *$N_{process_node}$ = `process-node-factor`
  
* **Arguments:**
  * `die-area` (@weight 0.5): Higher die area increases interconnect length.
  * `process-node-factor` (@weight 0.25): Smaller process nodes reduce interconnect length.

---

### InterconnectLengthConnector

Connects the length parameter on an architecture basis

* **Model** `InterconnectLengthConnector`
* **Formula**
  $$
  l = l_{2D} \vee l_{3D}
  $$
  Where:
  * $l$ = `length` (Architecture independent length of the interconnect)
  * $l_{2D}$ = `length-2D`
  * $l_{3D}$ = `length-3D`

* **Arguments**
  * `length-2D` (@weight 1)
  * `length-3D` (@weight 1)

---

### InterconnectAreaModel

Calculates the interconnect area

* **Model**
* **Formula**
  $$
  A = f(l, N_bus_width, N_process_node)
  $$
  Where
  * $A$ = Interconnect area
  * $l$ = Interconnect length
  * $N_{bus_width}$ = Bus width
  * $N_{process_node}$ = Factor for influence of the process node

* **Arguments**
  * `length` (@weight 1): Increased length increases area.
  * `N_{bus_width}` (@weight 1): Wider buses require more area.
  * `N_{process_node}` (@weight -2): Smaller process nodes reduce area requirements.

---
