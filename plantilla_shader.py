import OpenGL.GL as gl
import glfw
import numpy as np
from Shader import *
from Modelo import *
from Triangulo import Triangulo
from Fondo import Fondo
from Boss import *
from Bicho import *
from Bicho2 import *
from Bicho3 import *
from Bicho4 import *
from Bicho5 import *
from Bicho6 import *
from PowerUp import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

bicho = None 
bicho2 = None 
bicho3 = None
bicho4 = None
bicho5 = None
bicho6 = None
fondo = None
modelo = None
boss = None
window = None
powerUp=  None

tiempo_anterior = 0.0

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global tiempo_anterior
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    global window
    estado_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    if estado_arriba == glfw.PRESS:
        modelo.mover(modelo.ARRIBA, tiempo_delta)
    if estado_abajo == glfw.PRESS:
        modelo.mover(modelo.ABAJO, tiempo_delta)
    if estado_derecha == glfw.PRESS:
        modelo.mover(modelo.DERECHA, tiempo_delta)
    if estado_izquierda == glfw.PRESS:
        modelo.mover(modelo.IZQUIERDA, tiempo_delta)

    boss.actualizar(tiempo_delta)
    if modelo.colisionando(boss):
        glfw.set_window_should_close(window, 1)
        print("Game over: perdiste")

    if bicho.colisionando(modelo):
            bicho.vivo = False
    if bicho2.colisionando(modelo):
            bicho2.vivo = False
    if bicho3.colisionando(modelo):
            bicho3.vivo = False
    if bicho4.colisionando(modelo):
            bicho4.vivo = False
    if bicho5.colisionando(modelo):
            bicho5.vivo = False
    if bicho6.colisionando(modelo):
            bicho6.vivo = False

    if ((bicho.vivo == False) & (bicho2.vivo == False) & (bicho3.vivo == False) & (bicho4.vivo == False) & (bicho5.vivo == False) & (bicho6.vivo == False)):
        glfw.set_window_should_close(window, 1)
        print("Game over: ganaste")
       
    if modelo.colisionando(powerUp):
        modelo.velocidad = modelo.velocidad = 1.6
        powerUp.vivo = False

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    return colisionando
    
def dibujar():
    global modelo
    global fondo
    global boss
    global bicho
    global powerUp
    fondo.dibujar()
    bicho.dibujar()
    bicho2.dibujar()
    bicho3.dibujar()
    bicho4.dibujar()
    bicho5.dibujar()
    bicho6.dibujar()
    powerUp.dibujar()
    boss.dibujar()
    modelo.dibujar()

def main():
    global modelo
    global fondo
    global window
    global boss
    global bicho, bicho2, bicho3 ,bicho4 ,bicho5 ,bicho6
    global powerUp   
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")

    fondo = Fondo(shader,
            posicion_id, color_id, transformaciones_id)

    modelo = Triangulo(shader, 
            posicion_id, color_id, transformaciones_id)

    boss = Boss(shader, posicion_id, color_id, transformaciones_id)

    bicho = Bicho(shader, posicion_id, color_id, transformaciones_id)
    bicho2 = Bicho2(shader, posicion_id, color_id, transformaciones_id)
    bicho3 = Bicho3(shader, posicion_id, color_id, transformaciones_id)
    bicho4 = Bicho4(shader, posicion_id, color_id, transformaciones_id)
    bicho5 = Bicho5(shader, posicion_id, color_id, transformaciones_id)
    bicho6 = Bicho6(shader, posicion_id, color_id, transformaciones_id)

    powerUp = PowerUp(shader, posicion_id, color_id, transformaciones_id)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.22,0.58,0.2,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    fondo.borrar()
    boss.borrar()
    shader.borrar()
    bicho.borrar()

    

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

