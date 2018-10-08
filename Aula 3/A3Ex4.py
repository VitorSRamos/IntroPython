def funcao_conv_mil_m(d_mil):
    d_m = d_mil*1610
    return d_m

def funcao_conv_m_mil(d_m):
    d_mil = d_m/1610
    return d_mil

def funcao_conv_h_s(h):
    s = h*3600
    return s

def funcao_conv_s_h(s):
    h = s/3600
    return h


#Exercício aula 1

d_km_1 = 10
d_m_1 = 1000*(d_km_1)
t_s_1 = 43.5*(60)

d_mil_1 = funcao_conv_m_mil(d_m_1)
t_h_1 = funcao_conv_s_h(t_s_1)

t_med_1 = (t_h_1)/(d_mil_1) #tempo médio por milha em horas
v_med_1 = 1/(t_med_1) #velocidade média em milhas por hora

print(t_med_1)
print(v_med_1)


#exercício aula 3

d_mil_2 = 4
t_h_2 = 0.5

d_m_2 = funcao_conv_mil_m(d_mil_2)
d_km_2 = d_m_2/1000

v_med_2 = (d_km_2)/(t_h_2) #velocidade média em quilômetros por hora
t_med_2 = 1/(v_med_2) #tempo médio por quilômetro em horas

print(v_med_2)
print(t_med_2)
