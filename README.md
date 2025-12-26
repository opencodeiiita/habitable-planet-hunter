# Habitable Planet Hunter 🪐

## Dataset Overview
This project utilizes the **PHL Exoplanet Catalog** to predict the potential habitability of exoplanets. The dataset contains various physical and orbital parameters for confirmed exoplanets and their host stars.

**Dataset Link:**
[https://www.kaggle.com/datasets/chandrimad31/phl-exoplanet-catalog](https://www.kaggle.com/datasets/chandrimad31/phl-exoplanet-catalog)

---

## Prediction Goal
The objective is to classify whether a planet is potentially habitable based on its physical properties and its host star's characteristics.

**Target Variable:** `P_HABITABLE`
* *Note: This column defines the habitability class (e.g., 0 for non-habitable, 1 for conservatively habitable, 2 for optimistically habitable). You may choose to convert this into a binary classification problem (Habitable vs. Non-Habitable).*

---

## Feature Selection Instructions

**⚠️ IMPORTANT: Restricted Feature Set**

To ensure the model learns robust physical relationships (e.g., the interaction between stellar luminosity and orbital distance) rather than relying on pre-calculated habitability scores, **you are restricted to the pool of 30 columns listed below.**

1.  **Do NOT use** obvious predictors or direct proxies for habitability such as:
    * `P_TEMP_EQUIL` (Equilibrium Temperature)
    * `P_ESI` (Earth Similarity Index)
    * `P_HABZONE_OPT` / `P_HABZONE_CON` (Habitable Zone flags)
    * `P_FLUX` (Insolation Flux - *removed to force learning from Luminosity/Distance*)
2.  **From the list of 30 below**, perform your own Feature Engineering and Selection to choose the most effective combination for your model.

### The Approved Pool of 30 Features

**Planet Physical Properties**
1.  `P_MASS` - Planet Mass (EU)
2.  `P_RADIUS` - Planet Radius (EU)
3.  `P_DENSITY` - Planet Density (EU)
4.  `P_GRAVITY` - Planet Surface Gravity (EU)
5.  `P_ESCAPE` - Planet Escape Velocity (EU)
6.  `P_TYPE` - Planet Type (e.g., Super Earth, Gas Giant)

**Planet Orbital Parameters**
7.  `P_PERIOD` - Orbital Period (days)
8.  `P_SEMI_MAJOR_AXIS` - Mean distance from the star (AU)
9.  `P_ECCENTRICITY` - Orbital Eccentricity
10. `P_INCLINATION` - Orbital Inclination (degrees)
11. `P_OMEGA` - Argument of Periastron
12. `P_PERIASTRON` - Periastron distance (AU)
13. `P_APASTRON` - Apastron distance (AU)
14. `P_IMPACT_PARAMETER` - Transit Impact Parameter
15. `P_HILL_SPHERE` - Radius of the Hill Sphere (AU)

**Stellar Properties (Host Star)**
16. `S_MASS` - Star Mass (SU)
17. `S_RADIUS` - Star Radius (SU)
18. `S_LUMINOSITY` - Star Luminosity (SU)
19. `S_TEMPERATURE` - Star Effective Temperature (K)
20. `S_AGE` - Star Age (Gyrs)
21. `S_METALLICITY` - Star Metallicity ([Fe/H])
22. `S_LOG_G` - Star Surface Gravity
23. `S_TYPE` - Star Spectral Type
24. `S_MAG` - Star Magnitude
25. `S_DISC` - Presence of a circumstellar disc
26. `S_MAGNETIC_FIELD` - Star Magnetic Field presence

**System & Meta Data**
27. `S_SNOW_LINE` - Snow Line Distance (AU)
28. `S_TIDAL_LOCK` - Tidal Lock Limit Distance (AU)
29. `P_DETECTION` - Method of Detection (e.g., Transit, Radial Velocity)
30. `P_DISTANCE` - Distance of the system from Earth (pc)

---

## ⚙️ Environment & Compatibility (Crucial)

To ensure that all code submissions work seamlessly on cloud platforms like **Kaggle** and **Google Colab**, you must follow these environment rules:

1.  **Python Version:** Use **Python 3.10** locally. This is the default version on Kaggle/Colab.
2.  **Library Versions:** When installing libraries (Pandas, Scikit-Learn, etc.), ensure you are using the **latest versions compatible with Python 3.10**.
3.  **Why?** If you use features from Python 3.12 that don't exist in 3.10, your code will fail during the evaluation phase.
