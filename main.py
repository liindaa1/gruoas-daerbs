import math
cena = float(input("Cena ")) 
telpas_garums = float(input("garums "))
telpas_platums = float(input("platums "))
linoleja_platums = float(input("lplatums "))

telpa = telpas_garums * telpas_platums
izmaksas = telpa * linoleja_platums
cenas = izmaksas * cena
kopa = math.ceil(izmaksas)


print ("Cik daudz linoleja vajg ",kopa ,"m" " Cik daudz maksas",cenas, " EIRO")
