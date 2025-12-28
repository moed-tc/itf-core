"""
itf_tc.py - Módulo do Tensor de Compressão do Espaço-Tempo (TC)
"""

import sympy as sp

# Fibrado interno 4D
T1, T2, T3, T4 = sp.symbols('T_1 T_2 T_3 T_4', real=True)
T_vec = sp.Matrix([T1, T2, T3, T4])

# Tensor de Compressão TC (protótipo diagonal)
f1 = sp.Function('f_1')(T1, T2, T3, T4)
f2 = sp.Function('f_2')(T1, T2, T3, T4)
f3 = sp.Function('f_3')(T1, T2, T3, T4)
f4 = sp.Function('f_4')(T1, T2, T3, T4)

TC = sp.diag(f1, f2, f3, f4)

# Quantidades derivadas
TC_trace_squared = sp.trace(TC**2)
TC_det = TC.det()

# Inércia do Tempo (IT) acoplada
kappa_0, kappa_1, kappa_2 = sp.symbols('kappa_0 kappa_1 kappa_2', real=True, positive=True)
misalignment = sum((T_vec[i] - T_vec[j])**2 for i in range(4) for j in range(i+1, 4))
magnitude = T_vec.dot(T_vec)
IT = kappa_0 + kappa_1 * misalignment + kappa_2 * magnitude**2

# Projeção efetiva simplificada para 4D
alpha = sp.symbols('alpha', real=True)
TC_4D_eff = alpha * (sp.trace(TC)/4) * sp.eye(4)

__all__ = ["T_vec", "TC", "f1", "f2", "f3", "f4", "TC_trace_squared", "TC_det", "IT", "TC_4D_eff"]
