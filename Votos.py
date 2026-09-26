#Voto
i= int(input("Sua idade: "))
voto_o= (i== 16) or (i == 17) or (i> 68)

if voto_o==True:
  print("Voto não obrigatório")

elif i>17:
  print ("Voto obrigatório")

elif i >=0:
  print("Não pode votar")

else:
  print("ERRO")
