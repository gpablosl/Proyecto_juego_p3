from OpenGL.GL import *

import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.vertices = np.array(
            [
                -1,1,0,1.0,    0.4,0.65,0.15,1.0,
                -0.9,1,0,1.0,     0.4,0.65,0.15,1.0,
                -1,-1,0,1.0,  0.4,0.65,0.15,1.0, 
                -0.9, -1,0.0,1.0,    0.4,0.65,0.15,1.0
                
            ], dtype="float32"
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -1,1,0,1.0,  0.28,0.7,0.17,1.0,  
                    -1,0.9,0,1.0,    0.28,0.7,0.17,1.0, 
                    1.0,1,0.0,1.0,    0.28,0.7,0.17,1.0, 
                    1,0.9,0,1.0,     0.28,0.7,0.17,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    1,-1,0,1.0,  0.28,0.7,0.17,1.0, 
                    0.9, -1,0.0,1.0,    0.28,0.7,0.17,1.0,
                    1,1,0,1.0,    0.28,0.7,0.17,1.0,
                    0.9,1,0,1.0,     0.28,0.7,0.17,1.0                   
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    1.0,-1,0.0,1.0,    0.4,0.65,0.15,1.0, 
                    1,-0.9,0,1.0,      0.4,0.65,0.15,1.0,
                    -1,-1,0,1.0,   0.4,0.65,0.15,1.0,  
                    -1,-0.9,0,1.0,     0.4,0.65,0.15,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
 
                    -1.0,0.5,0.0,1.0,      0.20,0.53,0,1.0,
                    -1,1,0.0,1.0,    0.20,0.53,0,1.0, 
                    -0.5, 0.5,0,1.0,       0.20,0.53,0,1.0, 
                    -0.5, 1,0.0,1.0,     0.20,0.53,0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    1.0,-0.5,0,1.0,    0.33,0.6,0.2,1.0,  
                    1,-1.0,0,1.0,     0.33,0.6,0.2,1.0,
                    0.5, -0.5,.0,1.0,       0.33,0.6,0.2,1.0, 
                    0.5,-1,0,1.0,     0.33,0.6,0.2,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.4,-0.5,0,1.0,    0.3,0.45,0.1,1.0,  
                    0.4,-0.2,0,1.0,     0.3,0.45,0.1,1.0,
                    0.5, -0.3,.0,1.0,       0.3,0.45,0.1,1.0, 
                    0.7,-0.4,0,1.0,     0.3,0.45,0.1,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.2,0.2,0,1.0,     0.3,0.45,0.1,1.0,
                    0.2,0.4,0,1.0,    0.3,0.45,0.1,1.0,  
                    -0.2,0.2,.0,1.0,       0.3,0.45,0.1,1.0, 
                    -0.2, 0.4,0,1.0,     0.3,0.45,0.1,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                   0.1,0.9,0,1.0,    0.3,0.7,0.2,1.0,  
                    -0.1,0.9,0,1.0,     0.3,0.7,0.2,1.0,
                   0.1, 0.7,.0,1.0,       0.3,0.7,0.2,1.0, 
                    -0.1,0.7,0,1.0,     0.3,0.7,0.2,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                   -0.4,0.5,0,1.0,    0.2,0.55,0.15,1.0,  
                    -0.45,0.2,0,1.0,     0.2,0.55,0.15,1.0,
                   -0.6,0.4,.0,1.0,       0.2,0.55,0.15,1.0, 
                    -0.5, 0.3,0,1.0,     0.2,0.55,0.15,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.56,0.21,0,1.0,     0.34,0.7,0.342,1.0,
                   0.56,0.56,0,1.0,    0.34,0.7,0.342, 1.0,
                   0.21, 0.21,.0,1.0,       0.34,0.7,0.342,1.0,
                    0.21,0.56,0,1.0,     0.34,0.7,0.342,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                   -0.36,-.11,0,1.0,    0.25,0.5,0.22, 1.0,
                    -0.36,-0.36,0,1.0,     0.25,0.5,0.22,1.0,
                   -0.11, -0.11,.0,1.0,       0.25,0.5,0.22,1.0,
                    -0.11,-0.36,0,1.0,     0.25,0.5,0.22,1.0
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                   -0.85, -0.74,0,1.0,    0.27,0.68,0.22, 1.0,
                    -0.66,-.80,0,1.0,     0.27,0.68,0.22,1.0,
                   -0.76,-0.87,.0,1.0,       0.27,0.68,0.22,1.0,
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.0, 0.1,0,1.0,    0.2,0.4,0.22, 1.0,
                    0.05*3,-0.06*3+0.1,0,1.0,     0.2,0.4,0.22,1.0,
                    -0.02*3, -0.05*3+0.1,.0,1.0,       0.2,0.4,0.22,1.0,
                    0.0,-0.1*3+0.1,.0,1.0,       0.2,0.4,0.22,1.0,
                    -0.05*3,-0.06*3+0.1,.0,1.0,       0.2,0.4,0.22,1.0,

                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.1,-0.9,0,1.0,     0.6,0.7,0.6,1.0,
                   -0.1,-0.9,0,1.0,    0.6,0.7,0.6, 1.0,
                   0.1, -0.7,.0,1.0,       0.6,0.7,0.6,1.0,
                    -0.1,-0.7,0,1.0,     0.6,0.7,0.6,1.0
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.00,0.075,0,1.0,       0.5,0.18,0.6,1.0,
                    0.025,0.00,0.0,1.0,     0.5,0.18,0.6,1.0,
                    0.05,-0.025,0,1.0,      0.5,0.18,0.6,1.0,
                    -0.0,-0.075,0,1.0,      0.5,0.18,0.6,1.0,
                    -0.05,-0.025,0,1.0,     0.5,0.18,0.6,1.0,
                    -0.025,0.0,0,1.0,       0.5,0.18,0.6,1.0,
                    -0.05,0.025,0,1.0,      0.5,0.18,0.6,1.0,

                ], dtype="float32"
            )
        )

        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)

        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)
    

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 51, 5)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLES, 60, 8)



        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def borrar(self):
        #gl.glDeleteVertexArrays(1, self.VAO)
        #gl.glDeleteBuffers(1, self.VBO)

        print("borrando")

