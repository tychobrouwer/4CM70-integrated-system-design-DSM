# Core

## Relations

### PerformanceModel

This model estimates the computational performance and required bandwidth of a processing core based on its clock frequency, voltage, process node, transistor count, and latencies.

* **Model:** `PerformanceModel`
* **Formula:**
  $$
  CPP = f_{core} \cdot IPC
  $$
  $$
  RBW = \frac{CPP \cdot D_{inst}}{L_{cache} + L_{interconnect}}
  $$
  $$
  IPC = \alpha \cdot \frac{(V - V_{th})^\beta}{L_{gate}} \cdot \log(N_{transistors})
  $$
  Where:
  * $CPP$ = `core-computational-performance`
  * $f_{core}$ = `core-clock-frequency`
  * $IPC$ = Instructions per cycle
  * $RBW$ = `core-required-bandwidth`
  * $D_{inst}$ = Average data per instruction (architecture-independent, unimportant for DSM)
  * $L_{cache}$ = `cache-latency`
  * $L_{interconnect}$ = `interconnect-latency`
  * $V$ = `core-voltage`
  * $L_{gate}$ = `core-process-node-factor`
  * $N_{transistors}$ = `core-transistors`

* **Arguments:**
  * `core-clock-frequency` (@weight 0.4): Higher clock frequency increases computational performance.
  * `core-voltage` (@weight 0.3): Higher voltage improves switching speed, enhancing performance.
  * `core-process-node-factor` (@weight -0.2): Smaller process nodes enable higher performance due to reduced gate delays.
  * `core-transistors` (@weight 0.1): More transistors can improve performance through increased parallelism.
  * `cache-latency` (@weight -0.3): Lower cache latency reduces data access time, improving required bandwidth.
  * `interconnect-latency` (@weight -0.2): Lower interconnect latency enhances data transfer speed, reducing required bandwidth.
