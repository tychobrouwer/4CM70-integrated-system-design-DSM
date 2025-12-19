# Power Distribution System

## Relations

### Total Power Relation

This model aggregates the power requirements of the individual chip components to determine the total system load.

* **Model:** `TotalPowerModel`
* **Formula:**
  $$
  P_{\text{total}} = P_{\text{core}} + P_{\text{cache}}
  $$
  Where:
  * $P_{\text{total}}$ = `power-capability`
  * $P_{\text{core}}$ = `core-capability`
  * $P_{\text{cache}}$ = `cache-capability`

* **Arguments:**
  * `core-capability` (@weight 1): Power demand from the processing cores.
  * `cache-capability` (@weight 1): Power demand from the memory cache.

---

### Cache TSV Electrical Model

Determines the maximum safe current for the cache layer based on thermal and material constraints.

* **Model:** `TSVElectricalModel`
* **Physics Basis:** Thermal-limit current capacity balancing Joule heating against the thermal budget.
* **Formula:**
  $$
  I_{\max,\text{cache}} =
  K \cdot
  N_{\text{cache}}
  \cdot
  d_{\text{cache}}^{2}
  \cdot
  L_{\text{cache}}^{-1}
  \cdot
  \sqrt{
    \frac{
      \Delta T_{\text{cache}}
      \cdot
      k_{\text{tsv}}
    }{
      \rho_{\text{tsv}}
      \cdot
      R_{\text{tim}}
      \cdot
      R_{\text{contact}}
    }
  }
  $$

  Where:
  * $I_{\max,\text{cache}}$ = `cache-max-current-capacity`
  * $N_{\text{cache}}$ = `cache-tsv-count`
  * $d_{\text{cache}}$ = `cache-tsv-diameter`
  * $L_{\text{cache}}$ = `cache-tsv-length`
  * $\Delta T_{\text{cache}}$ = `cache-max-temp-budget`
  * $k_{\text{tsv}}$ = `tsv-thermal-conductivity`
  * $\rho_{\text{tsv}}$ = `tsv-resistivity`
  * $R_{\text{tim}}$ = `tim-resistance`
  * $R_{\text{contact}}$ = `contact-resistance`
  * $K$ = model constant (captures geometry/unit normalization)

* **Key Arguments & Weights:**
  * `cache-tsv-count` (@weight 1): Linear scaling of current paths.
  * `cache-tsv-diameter` (@weight 2): Quadratic scaling due to cross-section effects.
  * `cache-tsv-length` (@weight -1): Inverse scaling; longer paths reduce safe current.
  * `cache-max-temp-budget` (@weight 0.5): Square-root scaling of allowable temperature rise.
  * `tsv-thermal-conductivity` (@weight 0.5): Better heat removal increases capacity.
  * `tsv-resistivity` (@weight -0.5): Higher resistivity reduces capacity.
  * `tim-resistance` (@weight -0.5): Higher thermal resistance reduces capacity.
  * `contact-resistance` (@weight -0.5): Higher localized thermal resistance reduces capacity.

---

### Core TSV Electrical Model

Determines the maximum safe current for the compute core layer. While it uses the same physical model as the cache, the arguments are specific to the core's unique geometry and thermal limits.

* **Model:** `TSVElectricalModel`
* **Physics Basis:** Identical to the cache model, adapted for core-specific TSV dimensions and temperature tolerances.
* **Formula:**
  $$
  I_{\max,\text{core}} =
  K \cdot
  N_{\text{core}}
  \cdot
  d_{\text{core}}^{2}
  \cdot
  L_{\text{core}}^{-1}
  \cdot
  \sqrt{
    \frac{
      \Delta T_{\text{core}}
      \cdot
      k_{\text{tsv}}
    }{
      \rho_{\text{tsv}}
      \cdot
      R_{\text{tim}}
      \cdot
      R_{\text{contact}}
    }
  }
  $$

  Where:
  * $I_{\max,\text{core}}$ = `core-max-current-capacity`
  * $N_{\text{core}}$ = `core-tsv-count`
  * $d_{\text{core}}$ = `core-tsv-diameter`
  * $L_{\text{core}}$ = `core-tsv-length`
  * $\Delta T_{\text{core}}$ = `core-max-temp-budget`
  * $k_{\text{tsv}}$ = `tsv-thermal-conductivity`
  * $\rho_{\text{tsv}}$ = `tsv-resistivity`
  * $R_{\text{tim}}$ = `tim-resistance`
  * $R_{\text{contact}}$ = `contact-resistance`
  * $K$ = model constant (captures geometry/unit normalization)

* **Key Arguments & Weights:**
  * `core-tsv-count` (@weight 1)
  * `core-tsv-diameter` (@weight 2)
  * `core-tsv-length` (@weight -1)
  * `core-max-temp-budget` (@weight 0.5)
  * `tsv-thermal-conductivity` (@weight 0.5)
  * `tsv-resistivity` (@weight -0.5)
  * `tim-resistance` (@weight -0.5)
  * `contact-resistance` (@weight -0.5)
