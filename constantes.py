import pygame

from pygame.locals import *

#CONSTANTES

pygame.display.init()

FPS = 60

RESOLUCION = [pygame.display.Info().current_w,  pygame.display.Info().current_h]

ANCHO_VENTANA = 500
ALTO_VENTANA = 500

ANCHO_PANTALLA_GL = 500
ALTO_PANTALLA_GL = 500

ANCHO_FASE = ANCHO_PANTALLA_GL * 4
ALTO_FASE = ALTO_PANTALLA_GL * 2

REL_CADROS_PANTALLA = 100

NUM_CADROS_ANCHO_FASE = int(REL_CADROS_PANTALLA * (ANCHO_VENTANA/float(ALTO_VENTANA)))
NUM_CADROS_ALTO_FASE = REL_CADROS_PANTALLA

ANCHO_CADRO = ANCHO_VENTANA / float(NUM_CADROS_ANCHO_FASE)
ALTO_CADRO = ALTO_VENTANA / float(NUM_CADROS_ALTO_FASE)

MARCO_LATERAL = 0
MARCO_VERTICAL = 0

COLOR_LIMPIADO = [1,1,1,1]

pos_camara = [0,0]
