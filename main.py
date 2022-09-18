#Variable asignada para separar lineas y dar orden
sep='\n'
#Immportando libreria tiempo
import time
#importando libreria random
import random
#variable de intentos
intentos=1
#Variable de color amarillo
amarillo='\033[33m'
#Variable de color rojo
rojo='\033[31m'
#Variable de color azul
azul='\033[34m'
#Variable de color verde
verde='\033[32m'
#Reset del color en general
colorset='\033[39m'

#inicio
iniciar_trivia=True
#Determinamos el color del texto
print(amarillo+'Bienvenido')
#Variable para asignar nombre del usuario
nombre = input('Indiquenos su nommbre por favor:'+sep)
#Ejecutanto la linea de separacion
print(sep)
#Indicaciones del cuestionario
print('Hola,',nombre)
print('Este es un cuestionario para saber que tanto conoce sobre soporte tecnico basico')
print('A continuacion se te realizaran 10 preguntas, cada respuesta valida equivale a 2 puntos.')
#Delimitamos el final de color insertado
print('En base al puntaje final que saques el programa evaluara que tanto conoces sobre el soporte tecnico en equipos informaticos. Mucha suerte'+colorset)
print(sep)

#bucle de intentos trivia
while iniciar_trivia==True:
  
  #Variable del puntaje final
  puntaje=0
  #Mostramos la cantidad de intentos
  print('Intento n: ',intentos,sep)
  
  #Mostrando contador antes de iniciar preguntas
  for timer in range(5,0,-1):
    print(timer)
    time.sleep(1)
  print(sep)
  
  #Inicio de las preguntas
  print(azul+'PREGUNTA 1')
  print('Que es lo primero que debes hacer al momento de recepcionar un ordenador?')
  print('a) Limpiarlo.')
  print('b) Preguntarle para que lo usa')
  print('c) Prender/tratar de prender la maquina frente a el/ella')
  print('d) Ofrecerle una mejora de rendimiento.'+colorset)
  #Creamos una variable para guardar la respuesta y analizamos si es correcta
  respuesta_01 = input('Su respuesta:'+sep)
  #Insertamos un bucle que solo permita ingresar una de las alternativas
  while respuesta_01 not in('a','b','c','d','abcd'):
    respuesta_01=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_01 == 'c':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje +=2
  elif respuesta_01 == 'abcd':
    print('Eres hacker, dedicate a la programacion estimado. No necesitas este test.')
    puntaje-=1010
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset)  
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 2
  print(azul+'PREGUNTA 2')
  print('Cada cuanto tiempo es recomendable en promedio darle mantenimiento a una maquina?')
  print('a) Cada semana.')
  print('b) Cada 6 meses.')
  print('c) Cada 2 años.')
  print('d) Cuando presente lentitud.'+colorset)
  respuesta_02 = input('Su respuesta: '+sep)
  
  while respuesta_02 not in('a','b','c','d'):
    respuesta_02=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_02 == 'b':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 3
  print(azul+'PREGUNTA 3')
  print('Por que debes cuidar tu magnetización al manipular internamente un ordenador?')
  print('a) Porque te puede pasar corriente.')
  print('b) Porque la pasta térmica es sensible.')
  print('c) Porque se puede llegar a estropear la placa.')
  print('d) Se puede prender la maquina sin necesidad de estar conectada'+colorset)
  respuesta_03 = input('Su respuesta:'+sep)
  
  while respuesta_03 not in('a','b','c','d'):
    respuesta_03=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_03 == 'c':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 4
  print(azul+'PREGUNTA 4')
  print('Que liquido es fundamental a la hora de limpiar una placa?')
  print('a) Alcohol isopropilico.')
  print('b) Agua.')
  print('c) Limpiatodo.')
  print('d) Aceite siliconado.'+colorset)
  respuesta_04 = input('Su respuesta:'+sep)
  
  while respuesta_04 not in('a','b','c','d'):
    respuesta_04=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_04 == 'a':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 5
  print(azul+'PREGUNTA 5')
  print('Como puedes desmagnetizarte?')
  print('a) Usando una pulsera antiestatica')
  print('b) Con guantes quirúrgicos.')
  print('c) Apoyando tus manos en un lado del case.')
  print('d) Todas las anteriores.'+colorset)
  respuesta_05 = input('Su respuesta:'+sep)
  
  while respuesta_05 not in('a','b','c','d'):
    respuesta_05=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_05 == 'd':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 6
  print(azul+'PREGUNTA 6')
  print('6. Cual de todos los componentes es el que con mayor frecuencia se deteriora?')
  print('a) HDD/SSD')
  print('b) Placa base')
  print('c) Fuente de alimentación')
  print('d) Ventiladores'+colorset)
  respuesta_06 = input('Su respuesta:'+sep)
  
  while respuesta_06 not in('a','b','c','d'):
    respuesta_06=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_06 == 'b':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 7
  print(azul+'PREGUNTA 7')
  print('Cual de todos los componentes es el que con menor frecuencia se deteriora?')
  print('a) Memoria ram')
  print('b) Procesador')
  print('c) Tarjeta de video')
  print('d) Ventiladores'+colorset)
  respuesta_07 = input('Su respuesta:'+sep)
  
  while respuesta_07 not in('a','b','c','d'):
    respuesta_07=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_07 == 'b':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 8
  print(azul+'PREGUNTA 8')
  print('Que ver primero si se piensa darle un upgrade a un ordenador?')
  print('a) Buscar lo ultimo en tecnologia.')
  print('b) Revisar si los nuevos componentes son compatibles.')
  print('c) Revisar que el nuevo componente sea del mismo modelo/marca.')
  print('d) Comprarse un nuevo ordenador.'+colorset)
  respuesta_08 = input('Su respuesta:'+sep)
  
  while respuesta_08 not in('a','b','c','d'):
    respuesta_08=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_08 == 'b':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 9
  print(azul+'PREGUNTA 9')
  print('Que herramienta es básica para revisar un ordenador?')
  print('a) Destornilladores.')
  print('b) Software de análisis.')
  print('c) Dispositivo de almacenamiento.')
  print('d) Todas las anteriores.'+colorset)
  respuesta_09 = input('Su respuesta:'+sep)
  
  while respuesta_09 not in('a','b','c','d'):
    respuesta_09=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_09 == 'd':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep,'Tu puntaje hasta ahora:',puntaje,' / 20',sep)
  time.sleep(3)
  
  #Pregunta 10
  print(azul+'PREGUNTA 10')
  print('Como se entrega el ordenador ya reparado/con mantenimiento?')
  print('a) Prender la maquina en frente del cliente.')
  print('b) Entregarlo con un buen aroma.')
  print('c) Comparar su ordenador con otro parecido.')
  print('d) Dejándolo para que lo recoja y pague.'+colorset)
  respuesta_10 = input('Su respuesta:'+sep)
  
  while respuesta_10 not in('a','b','c','d'):
    respuesta_10=input('Por favor, responde correctamente.'+sep+ 'Su respuesta: ')
  if respuesta_10 == 'a':
    print(verde+'-Respuesta correcta, '+nombre+'!-'+colorset)
    puntaje+=2
  else:
    print(rojo+'-Respuesta incorrecta-'+colorset) 
  print(sep)
  time.sleep(5)
  
  #Aplicando puntaje random
  puntaje -=random.randint(5,10)
  print('Tu puntaje final es de: ')
  print(puntaje,' / 20')

  #consulta de continuacion de la trivia
  print(sep,amarillo+'Desea realizar otro intento?')
  repetir_trivia=input('Ingresa "si" para continuar, presione cualquier otra para finalizar: '+colorset).lower()
  print(sep)
  #condicional en caso finaliza la trivia
  if repetir_trivia!='si':
    print(sep,amarillo+'Gracias por participar, ',nombre,'. Buen dia'+colorset)
    iniciar_trivia=False
  #Aumentan los intentos
  intentos+=1