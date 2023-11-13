import smtplib

#globales
PROVIDER = "smtp.gmail.com"
PUERTO = 587
MY_EMAIL = "javier.mtgt@gmail.com"
MY_PASSWORD = "chjo iolj nqgm yjcl"

def enviarCorreo(asunto:str, cuerpo:str, correoDestinatario:str)->str:
    try:
        with smtplib.SMTP(PROVIDER, PUERTO) as connection:  # envia el correo utilizando los datos en el diccionario
            connection.starttls()       # inicia coneccion
            connection.login(MY_EMAIL, MY_PASSWORD) # envia usuario y contraseña
            connection.sendmail(                    # envia correo
                from_addr=MY_EMAIL,                 # remitente
                to_addrs=correoDestinatario,        # destinatario
                msg=f"Subject:{asunto}\n\n{cuerpo}".encode('utf-8')  # contenido
            )
            connection.close()
        return ""
    except Exception as e:
        return str(e)