import MYTOOLS as mt

casas_pi = int(input("Quantas casas decimais de PI?"))
casas_e = int(input("Quantas casas decimais de E?"))

aprox_pi = mt.pi_real(casas_pi)
aprox_e = mt.e_real(casas_e)

print(f"""Pi = {aprox_pi}
E = {aprox_e}""")