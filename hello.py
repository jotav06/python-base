__version__ = "0.0.1"
__author__ = "Victor"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá,Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola,mundo!"


print(msg)
