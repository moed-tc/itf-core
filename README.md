# MOED-TC | Modified Einstein Dynamics via Contraction Tensor

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moed-tc/itf-core/blob/main/notebooks/itf_simulator.ipynb)

> A theoretical framework proposing **local compressibility of space-time**, regulated by a Contraction Tensor (TC) and Inertia of Time (IT).  
> Designed as a fully relativistic extension inspired by the spirit of MOND, but applied directly to Einstein's equations.

## Overview

MOED-TC models space-time as locally elastic. Local compression is governed by:

- **Contraction Tensor (TC)** – a mixed (1,1) tensor in a 4D internal gauge fiber, describing elastic deformation.
- **Inertia of Time (IT)** – a potential that resists extreme compression and misalignment of internal time coordinates.

### Key Features
- Avoids singularities (black holes and Big Bang) via a natural bounce mechanism
- Generates particle masses and quantum-like behavior from small space-time oscillations
- Produces dark matter-like effects from anisotropic residuals of TC
- Produces dark energy-like effects from isotropic residuals of TC/IT
┌─────────────────────┐
              │   4D Space-Time     │
              │   (base manifold)   │
              └────────┬────────────┘
                       │
           Local elastic compression
                       │
              ┌────────▼────────────┐
              │ Contraction Tensor   │
              │ TC + Inertia of Time │
              └────────┬────────────┘
                       │
     Oscillations ◄───┘   Anisotropies → Dark matter effect
     Harmonic                Isotropies   → Dark energy effect
           ↓
      Particle properties (mass, spin, charge)

## Relation to MOND

MOED-TC can be viewed as a **relativistic analog of Modified Newtonian Dynamics (MOND)**.

- MOND modifies Newtonian gravity in low-acceleration regimes to explain galaxy rotation curves without dark matter.
- MOED-TC introduces similar effective modifications directly in General Relativity through local space-time compressibility.
- Fully covariant, addresses cosmology, gravitational lensing, and singularities.

## Contraction Tensor (TC)

The TC is a mixed tensor \( T^i_j \) in the 4D internal gauge fiber (diagonal prototype):

$$
T^i_j = \begin{pmatrix}
f_1(T_1, T_2, T_3, T_4) & 0 & 0 & 0 \\
0 & f_2(T_1, T_2, T_3, T_4) & 0 & 0 \\
0 & 0 & f_3(T_1, T_2, T_3, T_4) & 0 \\
0 & 0 & 0 & f_4(T_1, T_2, T_3, T_4)
\end{pmatrix}
$$

Physical quantities:

$$
\mathrm{Tr}(T^2) = f_1^2 + f_2^2 + f_3^2 + f_4^2
$$

$$
\det(T) = f_1 f_2 f_3 f_4
$$

## Inertia of Time (IT)

The potential resisting extreme compression:

$$
\mathrm{IT}(T_1,T_2,T_3,T_4) = \kappa_0 + \kappa_1 \sum_{1 \leq i < j \leq 4} (T_i - T_j)^2 + \kappa_2 (T_1^2 + T_2^2 + T_3^2 + T_4^2)^2
$$

Strong growth at high compression prevents singularities and enforces a bounce.

## Effective 4D Projection

The internal compression projects onto the base space-time as an effective stress-energy contribution (simplified isotropic part in the current prototype):

$$
T^{\rm TC}_{\mu\nu} = \alpha \cdot \frac{1}{4} (f_1 + f_2 + f_3 + f_4) \, g_{\mu\nu}
$$

## Repository Contents

itf-core/
├── src/
│   ├── itf_core.py      # Core Inertia of Time (IT) functions
│   └── itf_tc.py        # Full Contraction Tensor (TC) in 4D fiber
├── notebooks/
│   └── itf_simulator.ipynb  # Interactive simulator with eigenvalue evolution plots
├── requirements.txt     # Python dependencies
└── README.md            # This file

## Try It in Google Colab

Click the badge above to open the interactive simulator.

**Tip:** Run the first cell to automatically set up the environment. Then execute the remaining cells to see symbolic expressions and eigenvalue plots demonstrating emergent dark matter, dark energy, and bounce behavior.

## Current Status

This is an **early-stage theoretical exploration**.  
The goal is to share the core ideas, gather feedback, and iteratively develop the formalism and numerical tests.

Comments, questions, criticisms, and suggestions are very welcome — please open an issue or submit a pull request!

⭐ If the approach interests you, feel free to star the repository to follow future developments.
