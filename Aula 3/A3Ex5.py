def funcao_imc(a, m):
    imc = m/(a**2)
    return imc

def funcao_vol_esf(r):
    import math
    v_esf = (4/3)*(math.pi)*(r**3)
    return v_esf

def funcao_d_max(wl, d_anteparo, d_fenda):
    d_y = (wl)*(d_anteparo)/(d_fenda)
    return d_y

#argumentos
a = 1.72
m = 71.1
r = 5
wl = 632.8
d_anteparo = 1.98
d_fenda = 0.25

imc = funcao_imc(a, m)
v_esf = funcao_vol_esf(r)
d_max = funcao_d_max(wl, d_anteparo, d_fenda)

print(imc)
print(v_esf)
print(d_max)
