import  re
from telefone import Telefone

#padrao_molde = "[(xx)aaaa-wwww]"
#padrao = "([^0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"

#texto = "Eu gosto do numero 21999999999"
telefone = '5521999999999'
#resultado = re.findall(padrao, telefone)
resultado = Telefone(telefone)
print(resultado)







