import pygame
import random
from pynput.mouse import Button, Controller
# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pygame.init()

   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("This is my very first thing")

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
 
mouse = Controller()
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
  
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    
    pantalla.fill(BLANCO)
    pantalla.fill(NEGRO)
    R=random.randrange(10, 255,1)
    G=random.randrange(0, 255,1)
    B=random.randrange(0, 255,1)
    RANDOM = (R,G,B)
    x,y=mouse.position
    mousex=int(x)
    mousey=int(y)
    pygame.draw.circle(pantalla,RANDOM, (mousex,mousey), 10, 9)
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()