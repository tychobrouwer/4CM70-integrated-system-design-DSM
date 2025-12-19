# SRAM Cache

## Relations

### CacheOrganizationModel

This model determines the internal structure of the cache (number of sets) based on its total capacity and configuration.

* **Model:** `CacheOrganizationModel`
* **Formula:**
  $$
  N_{sets} = \frac{C}{B \cdot A}
  $$
  Where:
  * $N_{sets}$ = `number-of-sets`
  * $C$ = `capacity`
  * $B$ = `block-size`
  * $A$ = `associativity`

* **Arguments:**
  * `capacity` (@weight 1): Total cache capacity.
  * `block-size` (@weight -1): Size of a single cache block (line).
  * `associativity` (@weight -1): Number of ways (blocks per set).

---

### CacheAccessTimeModel

This model estimates the time required to access data in the cache, influenced by its size, complexity, and operating conditions.

* **Model:** `CacheAccessTimeModel`
* **Formula:**
  $$
  t_{access} \approx k \cdot \sqrt{C} \cdot (1 + \alpha \cdot A) \cdot f(V, T, L_{gate})
  $$
  Where:
  * $t_{access}$ = `access-time`
  * $C$ = `capacity`
  * $A$ = `associativity`
  * $V, T, L_{gate}$ Represent voltage, temperature, and process node factors.

* **Arguments:**
  * `capacity` (@weight 0.5): Larger caches generally have longer wire delays.
  * `associativity` (@weight 0.5): Higher associativity adds logic depth (muxing delay).
  * `process-node` (@weight -1): Smaller nodes reduce intrinsic gate delay.
  * `voltage` (@weight -1): Higher voltage generally reduces delay.
  * `temperature` (@weight 1): Higher temperature increases resistance and delay.

---

### CapacityModel

This model relates the physical transistor count to the effective storage capacity of the SRAM.

* **Model:** `CapacityModel`
* **Formula:**
  $$
  C \approx \frac{N_{transistors}}{N_{per\_bit} + N_{overhead}}
  $$
  Where:
  * $C$ = `capacity`
  * $N_{transistors}$ = `transistors`
  * $N_{per\_bit}$ $\approx$ 6 (for 6T SRAM)

* **Arguments:**
  * `transistors` (@weight 1): Total number of transistors available for the array and control logic.

---

### CacheBandwidthModel

This model calculates the theoretical maximum data throughput of the cache interface.

* **Model:** `CacheBandwidthModel`
* **Formula:**
  $$
  BW = W_{bus} \cdot f_{clock}
  $$
  Where:
  * $BW$ = `bandwidth`
  * $W_{bus}$ = `bus-width`
  * $f_{clock}$ = `clock-frequency`

* **Arguments:**
  * `bus-width` (@weight 1): Width of the data interface in bits/bytes.
  * `clock-frequency` (@weight 1): Rate at which data is transferred.
  * `process-node` (@weight -0.5): Indirectly affects achievable frequency and signal integrity.

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

### CacheHitRateModel

This model estimates the cache hit probability based on its size and organization parameters.

* **Model:** `CacheHitRateModel`
* **Formula:**
  $$
  H \approx 1 - \frac{k}{C^\alpha \cdot A^\beta}
  $$
  Where:
  * $H$ = `hit-rate`
  * $C$ = `capacity`
  * $A$ = `associativity`

* **Arguments:**
  * `capacity` (@weight 1): Larger capacity significantly reduces capacity misses.
  * `associativity` (@weight 0.5): Higher associativity reduces conflict misses.
  * `block-size` (@weight 0.2): Larger blocks exploit spatial locality but may increase conflict misses if too large.
