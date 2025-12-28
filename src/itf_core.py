import sympy as sp

# ---- Variáveis simbólicas ----
t, x, y = sp.symbols('t x y', real=True)

# ---- Função It (inércia temporal) ----
def It(tau1, tau2, tau3, k0=1.0, k1=1.0, k2=1.0):
    """
    Inércia Temporal efetiva (prototipo simplificado)
    tau1,tau2,tau3 = componentes do vetor temporal
    """
    desalinhamento = (tau1-tau2)**2 + (tau1-tau3)**2 + (tau2-tau3)**2
    magnitude = (tau1**2 + tau2**2 + tau3**2)
    return k0 + k1 * desalinhamento + k2 * (magnitude**2)

# ---- Lagrangiana efetiva simplificada ----
def L_itf(t, tau1, tau2, tau3):
    """
    Protótipo da Lagrangiana do ITF (versão 0.1)
    sem termos gravitacionais explícitos
    """
    IT = It(tau1, tau2, tau3)
    return 0.5 * IT * t**2  # termo cinematico mínimo

__all__ = ["It", "L_itf"]
