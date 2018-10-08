qtd_liv = 60

p_liv = (24.95)*(0.6)*(qtd_liv)

p_frete = 3 + (0.75)*(qtd_liv - 1)

p_tot = p_liv + p_frete

print(p_tot)
