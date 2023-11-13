from flask import *
import os

#instanciar servidor
app = Flask(__name__)

MY_EMAIL = os.environ.get('EMAIL_REMITENTE')
MY_PASSWORD = os.environ.get('EMAIL_PASSWORD')
CONFIG_DESTINATARIO = os.environ.get('CONFIG_DESTINATARIO')