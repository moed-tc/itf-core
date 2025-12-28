"""
itf_tc.py - Space-Time Contraction Tensor (TC) Full Module
MOED-TC Framework - 4D internal gauge fiber
"""

import sympy as sp

# 4D internal time coordinates (gauge fiber compatible with SU(2)_L × U(1)_Y)
T1, T2, T3, T4 = sp.symbols('T_1 T_2 T_3 T_4', real=True)
T_vec = sp.Matrix([T1, T2, T3, T4])

# Functional components of the Contraction Tensor (to be parametrized or learned by PINN)
f1 = sp.Function('f_1')(T1, T2, T3, T4)
f2 = sp.Function('f_2')(T1, T2, T3, T4)
f3 = sp.Function('f_3')(T1, T2, T3, T4)
f4 = sp.Function('f_4')(T1, T2, T3, T4)

# Contraction Tensor TC - diagonal prototype (easily extendable to full matrix)
TC = sp.diag(f1, f2, f3, f4)

# Derived physical quantities
TC_trace_squared = sp.trace(TC**2)    # Tr(TC²) – quadratic compression strength
TC_det = TC.det()                     # det(TC) – compression volume factor

# Inertia of Time (IT) fully coupled to the 4D fiber
kappa_0, kappa_1, kappa_2 = sp.symbols('kappa_0 kappa_1 kappa_2', real=True, positive=True)

# Full pairwise misalignment among all four components
misalignment = sum((T_vec[i] - T_vec[j])**2 for i in range(4) for j in range(i+1, 4))
magnitude = T_vec.dot(T_vec)

IT = kappa_0 + kappa_1 * misalignment + kappa_2 * magnitude**2

# Simplified effective projection to 4D space-time (isotropic part)
alpha = sp.symbols('alpha', real=True)
TC_4D_eff = alpha * (sp.trace(TC) / 4) * sp.eye(4)

# Export symbols for easy import
__all__ = [
    "T_vec", "TC", "f1", "f2", "f3", "f4",
    "TC_trace_squared", "TC_det",
    "IT", "TC_4D_eff"
]

# Demo when run directly
if __name__ == "__main__":
    print("=== MOED-TC: Contraction Tensor (TC) Module ===\n")
    print("Internal time vector (4D fiber):")
    sp.pprint(T_vec)
    print("\nContraction Tensor TC:")
    sp.pprint(TC)
    print("\nTr(TC²):")
    sp.pprint(TC_trace_squared)
    print("\ndet(TC):")
    sp.pprint(TC_det)
    print("\nInertia of Time (IT):")
    sp.pprint(IT)
    print("\nEffective 4D projection TC_4D_eff:")
    sp.pprint(TC_4D_eff)
