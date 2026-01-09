# SRAM Cache

## Relations

### CacheTransistorModel

This model estimates the number of transistors required to implement the cache based on its capacity, associativity, and block size.

* **Model:** `CacheTransistorModel`
* **Formula:**
  $$
  N_{transistors} = \frac{C \cdot 8}{N_{bits\_per\_cell}} \cdot (A + 1) + f(B)
  $$
  Where:
  * $N_{transistors}$ = `transistors`
  * $C$ = `capacity` (in bytes)
  * $A$ = `associativity`
  * $B$ = `block-size`
  * $N_{bits\_per\_cell}$ ≈ 6 for 6T SRAM cells

* **Arguments:**
  * `capacity` (@weight 1): Primary driver of transistor count - larger caches need more cells.
  * `associativity` (@weight 0.1): Additional tag storage and comparison logic for each way.
  * `block-size` (@weight 0): Minimal impact - affects organization but not total cell count significantly.

---

### CacheWireLengthModel

This model estimates the average wire length within the cache, which affects access time and power.

* **Model:** `CacheWireLengthModel`
* **Formula:**
  $$
  L_{wire} \approx \sqrt{A_{die}} \cdot \frac{1}{\sqrt{N_{banks}}} \cdot f(L_{gate})
  $$
  Where:
  * $L_{wire}$ = `internal-wire-length`
  * $A_{die}$ = `die-area`
  * $N_{banks}$ = `number-of-banks`
  * $L_{gate}$ = `process-node-factor`

* **Arguments:**
  * `die-area` (@weight 0.5): Wire length scales with square root of area.
  * `number-of-banks` (@weight -0.5): More banks reduce average wire length per access.
  * `process-node-factor` (@weight 0.5): Smaller nodes have proportionally shorter wires.

---

### CacheAccessTimeModel

This model estimates the time required to access data in the cache, influenced by its size, complexity, and operating conditions.

* **Model:** `CacheAccessTimeModel`
* **Formula:**
  $$
  t_{access} \approx k \cdot C^{0.3} \cdot (1 + \alpha \cdot A^{0.5}) \cdot \frac{L_{wire}^{0.5}}{V} \cdot (1 + \beta \cdot T) \cdot L_{gate}
  $$
  Where:
  * $t_{access}$ = `access-time`
  * $C$ = `capacity`
  * $A$ = `associativity`
  * $L_{wire}$ = `internal-wire-length`
  * $V$ = `voltage`
  * $T$ = `temperature`
  * $L_{gate}$ = `process-node-factor`

* **Arguments:**
  * `capacity` (@weight 0.3): Larger caches have longer wire delays.
  * `associativity` (@weight 0.5): Higher associativity adds multiplexing delay.
  * `process-node-factor` (@weight -1): Smaller nodes reduce intrinsic gate delay.
  * `voltage` (@weight -1): Higher voltage reduces delay.
  * `temperature` (@weight 0.3): Higher temperature increases resistance and delay.
  * `internal-wire-length` (@weight 0.5): Longer wires increase RC delay.

---

### CacheHitRateModel

This model estimates the cache hit probability based on its size and organization parameters.

* **Model:** `CacheHitRateModel`
* **Formula:**
  $$
  H \approx 1 - \frac{k}{C^{0.7} \cdot A^{0.3} \cdot B^{0.15}}
  $$
  Where:
  * $H$ = `hit-rate`
  * $C$ = `capacity`
  * $A$ = `associativity`
  * $B$ = `block-size`

* **Arguments:**
  * `capacity` (@weight 0.7): Larger capacity significantly reduces capacity misses.
  * `associativity` (@weight 0.3): Higher associativity reduces conflict misses.
  * `block-size` (@weight 0.15): Larger blocks exploit spatial locality.

---

### CacheAMATModel

This model calculates the Average Memory Access Time (AMAT), which is the effective latency seen by the processor.

* **Model:** `CacheAMATModel`
* **Formula:**
  $$
  t_{avg} = t_{hit} + (1 - H) \cdot t_{miss}
  $$
  Where:
  * $t_{avg}$ = `latency`
  * $t_{hit}$ = `access-time`
  * $H$ = `hit-rate`
  * $t_{miss}$ = `miss-penalty`

* **Arguments:**
  * `access-time` (@weight 1): Time to access the cache on a hit.
  * `hit-rate` (@weight -1): Probability of finding data in the cache (highly sensitive).
  * `miss-penalty` (@weight 1): Time required to fetch data from the next level of memory.

---
