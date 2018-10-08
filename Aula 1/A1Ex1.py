#Exercício 1

d_km = 10

d_mil = d_km/1.61

t_min = 43.5

t_hor = t_min/60

v_mph = d_mil/t_hor 

t_med_hor = 1/v_mph 

t_med_min = t_med_hor*60

print ('A velocidade média é de ' , v_mph, 'milhas por hora. O tempo medio por milha é de ' , t_med_min , 'minutos')
