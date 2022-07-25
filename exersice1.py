# Напишите программу, удаляющую из текста все слова, содержащие ""абв"". Делали на семинаре 


word = 'абв Ура, питон круто, очеабвнь инетресные семинарабвы! абв'
listW = word.split()
print (word)
new_string = list(filter(lambda i: not 'абв' in i, listW))
new_new_string = ''
for i in range(len(new_string)):
    new_new_string+= new_string[i] + ' '
print(new_new_string)
