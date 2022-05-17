from OpenGL.GL import *
from Modelo import *
import glm

class Boss(Modelo):

    velocidad = 0.005
    direccion = 0

    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.12
        self.extremo_derecho = 0.12
        self.extremo_inferior = 0.12
        self.extremo_superior = 0.12
        self.posicion = glm.vec3(0.8,0.0,0.0)

        self.vertices = np.array(
            [
                -0.01*5,0.01*5,0,1.0,  0.0,0.0,0.1,1.0, 
                0.00*5,0.01*5,0,1.0,    0.0,0.0,0.1,1.0,  
                0.01*5,-0.00*5,0,1.0,    0.0,0.0,0.1,1.0,
                0.01*5,-0.01*5,0,1.0,     0.0,0.0,0.1,1.0,
                0.0,-0.02*5,0,1.0,  0.0,0.0,0.1,1.0, 
                -0.01*5,-0.02*5,0,1.0,    0.0,0.0,0.1,1.0,  
                -0.02*5,-0.01*5,0,1.0,    0.0,0.0,0.1,1.0,
                -0.02*5,-0.00,0,1.0,     0.0,0.0,0.1,1.0,
                -0.01*5,0.01*5,0,1.0,  0.0,0.0,0.1,1.0,

                -0.01*4,0.01*4,0,1.0,  0.0,0.0,0.1,1.0, 
                0.00*4,0.01*4,0,1.0,    0.0,0.0,0.1,1.0,  
                0.01*4,-0.00*4,0,1.0,    0.0,0.0,0.1,1.0,
                0.01*4,-0.01*4,0,1.0,     0.0,0.0,0.1,1.0,
                0.0,-0.02*4,0,1.0,  0.0,0.0,0.1,1.0, 
                -0.01*4,-0.02*4,0,1.0,    0.0,0.0,0.1,1.0,  
                -0.02*4,-0.01*4,0,1.0,    0.0,0.0,0.1,1.0,
                -0.02*4,-0.00,0,1.0,     0.0,0.0,0.1,1.0,
                -0.01*4,0.01*4,0,1.0,  0.0,0.0,0.1,1.0 
            ], dtype="float32"
        )

        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, transformaciones_id, color_id)

    def actualizar(self):
        cantidad_movimiento = self.velocidad * 0.5
        if self.direccion == 0:
            self.posicion.x = self.posicion.x - cantidad_movimiento
        elif self.direccion == 1:
            self.posicion.x = self.posicion.x + cantidad_movimiento
        if self.posicion.x <= -0.8 and self.direccion == 0:
            self.direccion = 1
        if self.posicion.x >= 0.8 and self.direccion == 1:
            self.direccion = 0
    
    def dibujar(self):

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 18)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()
