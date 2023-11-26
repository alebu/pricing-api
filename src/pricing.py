import numpy as np
import scipy.stats as sp

def d_denominator(sigma, time_to_expiry):
    return sigma*np.sqrt(time_to_expiry)

def d_1(S, K, time_to_expiry, r, variance):
    d_1 = (
        np.log(S/K) + (
            time_to_expiry*(r + 0.5*variance)
        )
    )/d_denominator(np.sqrt(variance), time_to_expiry)
    return d_1

def d_2(S, K, time_to_expiry, r, variance):
    d_2 = (
        np.log(S/K) + (
            time_to_expiry*(r - 0.5*variance)
        )
    )/d_denominator(np.sqrt(variance), time_to_expiry)
    return d_2

def N(x):
    return sp.norm.cdf(x)

def call_option_bsm_formula(S, K, T, t, r, sigma):
    tau = T - t
    return S*N(d_1(S, K, tau, r, sigma**2)) - K*np.exp(-r*(tau))*N(d_2(S, K, tau, r, sigma**2))