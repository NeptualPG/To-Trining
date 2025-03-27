def reduction(posi,sw):
    posi = posi-((9-sw)*6)
    return posi

posi = 45*6
casend = posi
caseout = 0
sw = 0
ln = []  

text = input("Type the numbers to delete in the probability: ")

for i in range(len(text)):  #OBTENGO LA LOGITUD DEL TEXTO PARA PODER SABER CUALES SON NÚMEROS
    
    if text[i].isdigit():   #FUNTION TO KNOW IF THE CHARACTER IS A DIGIT
        if not (int(text[i]) in ln):
            ln.append(int(text[i])) #ADD TO THE LIST THE DIGIT TO NO CAN BE THE SAME DIGIT
            casend = reduction(casend,sw)   #REDUCE LOS CASOS
            sw += 1 

caseout = posi - casend

print(f"De {posi} posibilidades")
print(f"Las posibilidades validas son: {casend}")
print(f"Las posibilidades invalidas son: {caseout}")




