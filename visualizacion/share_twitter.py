#-*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import webbrowser
import sqlite3




#Esta es una URL que permite compartir por twitter desde cualquier cuenta
#https://twitter.com/intent/tweet?text=


#Conexión con la base de datos de sqlite (donde estan los datos del calendario)
conn = sqlite3.connect('visualizacion.db')
c = conn.cursor()

aux= ''
for row in c.execute('SELECT * FROM PROGRAMA WHERE DIA="Monday"'):
        for row1 in c.execute('SELECT EVENTO FROM CHARLAS'):
                 lunes = row[1] + row[2] + "  "
                 aux += row[4]+" "+ row[5] +  ": " + row1[0] + "   \n "

lunes +=  aux
lunes += 'https://institucional.us.es/innosoft/ #isoftdays'
lunes.replace(" ", "",)

webbrowser.open("https://twitter.com/intent/tweet?text=" +lunes[0:289])
webbrowser.open("https://twitter.com/intent/tweet?text=" +lunes[289:575])
webbrowser.open("https://twitter.com/intent/tweet?text=" +lunes[576:864])
webbrowser.open("https://twitter.com/intent/tweet?text=" +lunes[864:1153])

print(lunes)




aux1= ''
for row in c.execute('SELECT * FROM PROGRAMA WHERE DIA="Tuesday"'):
        for row1 in c.execute('SELECT EVENTO FROM CHARLAS'):
            martes = row[1] + row[2] + "  "
            aux1 += row[4] + " " + row[5] + ": " + row1[0] + "   \n "

martes += aux1
martes += 'https://institucional.us.es/innosoft/ #isoftdays'
martes.replace(" ", "",)

#webbrowser.open("https://twitter.com/intent/tweet?text=" +martes[0:290])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +martes[291:575])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +martes[576:864])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +martes[864:1153])

#print(martes)


#print(aux1)

aux2= ''
for row in c.execute('SELECT * FROM PROGRAMA WHERE DIA="Wednesday"'):
    for row1 in c.execute('SELECT EVENTO FROM CHARLAS'):
        mierc = row[1] +"  "+ row[2] +"  "
        aux2 += row[4] + " " + row[5] + ": " + row1[0] + "   \n "

mierc += aux2
mierc += 'https://institucional.us.es/innosoft/ #isoftdays'
mierc.replace(" ", "",)

#webbrowser.open("https://twitter.com/intent/tweet?text=" +mierc[0:277])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +mierc[277:558])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +mierc[558:845])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +mierc[845:1153])

#print(mierc)

#print(mierc)

aux3= ''
for row in c.execute('SELECT * FROM PROGRAMA WHERE DIA="Thursday"'):
    for row1 in c.execute('SELECT EVENTO FROM CHARLAS'):
        jueves = row[1] + row[2] + "  "
        aux3 += row[4] + " " + row[5] + ": " + row1[0] + "   \n "

jueves += aux3
jueves += 'https://institucional.us.es/innosoft/ #isoftdays'
jueves.replace(" ", "",)

#webbrowser.open("https://twitter.com/intent/tweet?text=" +jueves[0:292])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +jueves[296:575])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +jueves[580:864])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +jueves[868:1153])

#print(jueves)

#print(jueves)

aux4= ''
for row in c.execute('SELECT * FROM PROGRAMA WHERE DIA="Friday"'):
    for row1 in c.execute('SELECT EVENTO FROM CHARLAS'):
        viernes = row[1] + row[2] + "  "
        aux4 += row[4] + " " + row[5] + ": " + row1[0] + "   \n "

viernes += aux4
viernes += 'https://institucional.us.es/innosoft/ #isoftdays'
viernes.replace(" ", "",)

#webbrowser.open("https://twitter.com/intent/tweet?text=" +viernes[0:289])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +viernes[294:575])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +viernes[576:864])
#webbrowser.open("https://twitter.com/intent/tweet?text=" +viernes[864:1153])



#print(viernes)