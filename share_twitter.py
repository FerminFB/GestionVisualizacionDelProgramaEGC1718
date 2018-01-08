from __future__ import absolute_import, print_function

import tweepy
import webbrowser
import sqlite3


#Esta es una URL que permite compartir por twitter desde cualquier cuenta
webbrowser.open("https://twitter.com/intent/tweet?text=Hello%20world")

#Conexión con la base de datos de sqlite (donde estan los datos del calendario)
conn = sqlite3.connect('programa.db')
c = conn.cursor()


for row in c.execute('SELECT * FROM PROGRAMA'):
        print (row)


for row in c.execute('SELECT * FROM CHARLAS'):
        print (row)

####### Con esto podemos twittear desde una cuenta fija el calendario
# Registrándose en esta página. nos creamos una app y miramos la siguiente información: http://apps.twitter.com
# The consumer key and secret will be generated for you after
#consumer_key="mTSMT3SgEJNQcWFCYCenWACqs"
#consumer_secret="2ssH7SErBEYW1F6Gc0ByvBD0AjGf2sYlRTJvNjMBRdCIrbz25T"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
#access_token="392627830-xuY08mATOmAotrjITfLxMX1J9FJjZ8Hd73kgy0LZ"
#access_token_secret="RZcootqGzwrcUEMJHn6eIPsnv8YvSOPpxAgEf9Q25GhAj"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#####Creación del tweet desde la cuenta que has seleccionado
#api.update_status('Hello world https://institucional.us.es/innosoft/ #isoftdays #test vía @InnoSoftDays')





