import OpenGL.GL as gl
import glfw
import numpy as np
from Shader import *
from Modelo import *
from Triangulo import Triangulo
from Fondo import Fondo
from Boss import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

fondo = None
modelo = None
boss = None
window = None

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global window
    estado_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    if estado_arriba == glfw.PRESS:
        modelo.mover(modelo.ARRIBA)
    if estado_abajo == glfw.PRESS:
        modelo.mover(modelo.ABAJO)
    if estado_derecha == glfw.PRESS:
        modelo.mover(modelo.DERECHA)
    if estado_izquierda == glfw.PRESS:
        modelo.mover(modelo.IZQUIERDA)

    boss.actualizar()
    if modelo.colisionando(boss):
        glfw.set_window_should_close(window, 1)
        print("Game over: perdiste")


def colisionando():
    colisionando = False
    return colisionando
    
def dibujar():
    global modelo
    global fondo
    global boss
    boss.dibujar()
    fondo.dibujar()
    modelo.dibujar()

def main():
    global modelo
    global fondo
    global window
    global boss
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

    

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

