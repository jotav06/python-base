__version__ = "0.0.2"
__author__ = "Victor"
__license__ = "Unlicense"

import logging
import os
import sys

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("bruno", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s " "l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e),
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "de_DE": "Hallo, Welt!",
    "nl_NL": "Hallo, Wereld!",
    "sv_SE": "Hej, Världen!",
    "no_NO": "Hei, Verden!",
    "da_DK": "Hej, Verden!",
    "fi_FI": "Hei, Maailma!",
    "pl_PL": "Witaj, Świecie!",
    "ru_RU": "Привет, мир!",
    "ja_JP": "こんにちは、世界！",
    "zh_CN": "你好，世界！",
    "ko_KR": "안녕하세요, 세계!",
    "ar_SA": "مرحبا بالعالم!",
    "hi_IN": "नमस्ते दुनिया!",
    "tr_TR": "Merhaba, Dünya!",
    "el_GR": "Γειά σου, Κόσμε!",
    "he_IL": "שלום עולם!",
    "cs_CZ": "Ahoj, světe!",
    "hu_HU": "Helló, Világ!",
    "ro_RO": "Salut, Lume!",
    "uk_UA": "Привіт, світе!"
}


"""
# try com valor default
message = msg.get(current_language, msg["en_US"])
"""

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
