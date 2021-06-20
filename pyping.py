
'''
Como hacer Ping a nuestros dispositivos:
El programa nos avisará del cambio que tengan los dispositivos de nuestra red. 
La primera vez que lo ejecutemos los añadirá y nos dirá si están conectado o 
desconectados. Nosostros personalizaremos los mensajes de telegram.

¿Qué necesitamos para empezar?
*Crear un bot en telegram. Tienes ejemplos en la web.
*Conocer la ip de los dispositivos que queremos chequear y anotarlos en el txt.
    Añadir ip "," (coma) y el nombre del dispositivo..
    *Si quieres chequear las ip de tu red, puedes hacerlo con la app "Fing" para Android y iOS.
*Rellenar token del bot de telegram.
*Rellenar chatid para el envio de los avisos.

*Ajustes de la configuración en la parte de "Configuración de Scrip Ping":
 - Tiempo_Espera: Los segundos, minutos, horas o dias de tiempo de espera en volver a hacer ping a
                     la lista de dispositivos, ¿que debo elegir?, por defecto lo dejo en 5 minutos, 
                     para no utilizar ese tiempo, dejarlo en 0 (cero).
 - Cantidad de Ping: Nº de veces que hace Ping a cada dispositivo, por defecto 2.
 - ruta_archivo: ruta del archivo txt con la lista de dispositivos.
 - nombre_archivo: nombre del archivo txt de las lista de dispositovs, por defecto ping.
 - mostrar_terminal: En caso de que quieras ver que es lo que ejecuta el script, puedes poner
                     True y verás en la terminal el proceso, por defecto False.
 - archivo_log: Crea archivo log para hacer un seguimiento, por defecto False.
 - token: token del bot de telegram.
 - chatid: ID del chat de telegram que enviaremos los mensajes.
 - mensaje_conexion: mensaje que se enviará por telegram en caso de conexión.
 - mensaje_desconexion: mensaje que se enviará por telegram en caso de desconexión.
'''

################################
## CONFIGURACIÓN SCRIPT PING:
Tiempo_Espera_Segundos = 0
Tiempo_Espera_Minutos = 5 
Tiempo_Espera_Horas = 0
Tiempo_Espera_Dias = 0
Cantidad_Ping = 2
ruta_archivos = 'Ruta/De/La/Carpeta'
nombre_archivo = 'ping'
mostrar_terminal = False
archivo_log = False

## TELEGRAM
token = 'TOKEN DEL BOT DE TELEGRAM'
chatid = 'CHATID DE TELEGRAM'
mensaje_conectado = ' --> Conectado'
mensaje_desconectado = ' !!> Desconectado'
################################


import time, platform, subprocess, requests, logging
from datetime import datetime

## FUNCIÓN PING
def ping(host,info):
    plataforma = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', plataforma, '{}'.format(Cantidad_Ping), host]
    if mostrar_terminal == False:
        ping = subprocess.call(comando, stderr=subprocess.STDOUT, shell=False, stdout=subprocess.DEVNULL)
    else:
        ping = subprocess.call(comando, stderr=subprocess.STDOUT, shell=False)
    if ping == 0:
        if estado[info] != True:
            estado[info] = True
            mensajeTelegram(info,mensaje_conectado)
            if mostrar_terminal:
                print(str(info) + '{}\n'.format(mensaje_conectado))
            if archivo_log:
                logging.info(str(info) + mensaje_conectado,)

        else:
            pass
    
    else:
        if estado[info] != False:
            estado[info] = False
            mensajeTelegram(info,mensaje_desconectado)
            if mostrar_terminal:
                print(str(info) + '{}\n'.format(mensaje_desconectado))
            if archivo_log:
                logging.info(str(info) + mensaje_desconectado)

        else:
            pass

## AÑADIR DISPOSITIVOS AL estado POR PRIMERA VEZ  
def add_estado():
    with open('{}{}.txt'.format(ruta_archivos,nombre_archivo), "r") as f:
            lee = f.readlines()
            for x in lee:
                if '#' in x:
                    pass
                elif x == '\n':
                    pass
                else:
                    x = x.split(',')
                    info = x[1].replace('\n','')
                    estado[info] = ''
            if archivo_log:
                logging.info('estado inicial creado.')

## MENASJES DE TELEGRAM
def mensajeTelegram(dispositivo,message):
    base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text="{}{}"'.format(token,chatid,dispositivo,message)
    requests.get(base_url)

## ARCHIVO LOG
if archivo_log:
    logging.basicConfig(filename='{}LOG_{}.log'.format(ruta_archivos,nombre_archivo), filemode='w', level=logging.INFO)

## FECHA
fecha_actual = datetime.utcnow()
if archivo_log:
    logging.info('Primera ejecución: ' + str(fecha_actual))

## TIEMPO DE ESPERA
Tiempo_Espera_Minutos =  Tiempo_Espera_Minutos * 60
Tiempo_Espera_Horas = (Tiempo_Espera_Horas * 60) * 60
Tiempo_Espera_Dias = ((Tiempo_Espera_Dias * 24) * 60 ) * 60
Tiempo_Espera = Tiempo_Espera_Segundos + Tiempo_Espera_Minutos + Tiempo_Espera_Horas + Tiempo_Espera_Dias

## SCRIPT
estado = {}
add_estado()
while True:
    try:
        with open('{}{}.txt'.format(ruta_archivos,nombre_archivo), "r") as k:
            lee = k.readlines()
            for x in lee:
                if '#' in x:
                    pass
                elif x == '\n':
                    pass
                else:
                    x = x.split(',')
                    host = x[0]
                    info = x[1].replace('\n','')    
                    ping(host,info)
        if mostrar_terminal:
            print('\nTiempo_Espera para volver a revisar la lista de dispositivos.\n')
        if archivo_log:
            logging.info('Tiempo_Espera para volver a revisar la lista de dispositivos.')
        time.sleep(Tiempo_Espera)

    except Exception as e:
        #En caso de algún error, para 40 segundos y vuelve a intentarlo.
        if archivo_log:
            logging.error('Ha ocurrido un error:\n' + str(e))
        time.sleep(40)

