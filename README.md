# pyping

Controla tus dispositivos haciendo "Ping" a tus dispositivos con python y además con aviso a Telegram de los cambios que tengan.


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

Espero que guste.

Un saludo.
