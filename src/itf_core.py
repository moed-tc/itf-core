import sympy as sp

# ---- Parâmetros simbólicos ----
kappa_0, kappa_1, kappa_2 = sp.symbols('kappa_0 kappa_1 kappa_2', real=True, positive=True)
m = sp.symbols('m', real=True, positive=True)  # massa efetiva (para termo cinético)

# ---- Função Inércia do Tempo (IT) ----
def It(tau1, tau2, tau3, k0=kappa_0, k1=kappa_1, k2=kappa_2):
    """
    Potencial de Inércia do Tempo (IT)
    Resiste a desalinhamento e alta magnitude das componentes temporais internas.
    """
    desalinhamento = (tau1 - tau2)**2 + (tau1 - tau3)**2 + (tau2 - tau3)**2
    magnitude = tau1**2 + tau2**2 + tau3**2
    return k0 + k1 * desalinhamento + k2 * magnitude**2

# ---- Lagrangiana efetiva (versão toy-model para PINN) ----
def L_itf(tau1, tau2, tau3, f1=1, f2=1, f3=1, mass=m):
    """
    Lagrangiana simplificada do Inertia of Time Framework (ITF)
    Termo cinético anisotrópico nas dimensões internas de tempo
    menos o potencial IT.
    """
    kinetic = mass * (f1 * tau1**2 + f2 * tau2**2 + f3 * tau3**2)
    potential = It(tau1, tau2, tau3)
    return kinetic - potential

__all__ = ["It", "L_itf"]
