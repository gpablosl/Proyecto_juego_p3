from OpenGL.GL import *
from Modelo import *
import glm

class Bicho2(Modelo):
    vivo = True

    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.0
        self.extremo_derecho = 0.12
        self.extremo_inferior = 0.03
        self.extremo_superior = 0.12
        self.posicion = glm.vec3(-0.55, -0.55,0.0)


        self.vertices = np.array(
            [
                0.00*12,0.00*12,0,1.0,  0.8,0.0,0.7,1.0, 
                0.01*12,0.00*12,0,1.0,    0.8,0.0,0.7,1.0,  
                0.00*12,0.01*12,0,1.0,    0.8,0.0,0.7,1.0,
                0.01*12,0.01*12,0,1.0,     0.8,0.0,0.7,1.0,
            ], dtype="float32"
        )

        super().__init__(shader, posicion_id, transformaciones_id, color_id)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
    
        if self.vivo:
            self.shader.usar_programa()
            gl.glBindVertexArray(self.VAO)

            gl.glUniformMatrix4fv(self.transformaciones_id,
                    1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


            gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

            gl.glBindVertexArray(0)
            self.shader.liberar_programa()
