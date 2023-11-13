from flask import *
import os

#instanciar servidor
app = Flask(__name__)

MY_EMAIL = os.environ['EMAIL_REMITENTE']
MY_PASSWORD = os.environ['EMAIL_PASSWORD']
CONFIG_DESTINATARIO = os.environ['CONFIG_DESTINATARIO']