saldo = 1000
saque = 500
limite = 200 
conta_especial = True

# AND = Para ser true tudo tem que ser true 

# OR = Para ser true basta um ser true

# print (True and True)
# print (True and False)
# print (False and True)
# print (True or False)
# print (True or False)

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
print(exp)

exp_2 =  (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2) 

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente 
print(exp_3)