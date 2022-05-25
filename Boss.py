from OpenGL.GL import *
from Modelo import *
import glm

class Boss(Modelo):

    velocidad = 4.2
    direccion = 0

    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.0
        self.extremo_derecho = 0.17
        self.extremo_inferior = 0.3
        self.extremo_superior = 0.07
        self.posicion = glm.vec3(0.8,0.2,0.0)

        #self.vertices = np.array(
        #    [
        #        0.00*18,0.00*18,0,1.0,  0.5,0.0,0.1,1.0, 
        #        0.01*18,0.00*18,0,1.0,    0.5,0.0,0.1,1.0,  
        #        0.00*18,0.01*18,0,1.0,    0.5,0.0,0.1,1.0,
          #      0.01*18,0.01*18,0,1.0,     0.5,0.0,0.1,1.0,
         #   ], dtype="float32"
        #)

        self.vertices = np.array(
            [
                0.00*5,0.00*5,0,1.0,  0.5,0.0,0.1,1.0, 
                -0.01*5,-0.01*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.03*5,-0.05*5,0,1.0,    0.5,0.0,0.1,1.0,
            ], dtype="float32"
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                0.00*5,0.00*5,0,1.0,  0.5,0.0,0.1,1.0, 
                0.04*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.03*5,-0.05*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                0.03*5,0.00*5,0,1.0,  0.5,0.0,0.1,1.0, 
                0.04*5,-0.01*5,0,1.0,    0.5,0.0,0.1,1.0,  
                -0.01*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                0.04*5,-0.01*5,0,1.0,  0.5,0.0,0.1,1.0, 
                -0.01*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.00*5,-0.05*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                0.03*5,-0.00*5,0,1.0,  0.5,0.0,0.1,1.0, 
                -0.00*5,-0.00*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.04*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )  
        self.vertices = np.append(self.vertices, np.array(
                [
                -0.01*5,-0.01*5,0,1.0,  0.5,0.0,0.1,1.0, 
                -0.01*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.04*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                0.04*5,-0.01*5,0,1.0,  0.5,0.0,0.1,1.0, 
                0.04*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.00*5,-0.04*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )  
        self.vertices = np.append(self.vertices, np.array(
                [
                -0.00*5,-0.05*5,0,1.0,  0.5,0.0,0.1,1.0, 
                0.03*5,-0.05*5,0,1.0,    0.5,0.0,0.1,1.0,  
                0.01*5,-0.00*5,0,1.0,    0.5,0.0,0.1,1.0,                         
                ], dtype="float32"
            )
        )                    
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, transformaciones_id, color_id)

    def actualizar(self,tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 0:
            self.posicion.x = self.posicion.x - cantidad_movimiento
        elif self.direccion == 1:
            self.posicion.x = self.posicion.x + cantidad_movimiento
        if self.posicion.x <= -1 and self.direccion == 0:
            self.direccion = 1
        if self.posicion.x >= 0.85 and self.direccion == 1:
            self.direccion = 0
    
    def dibujar(self):

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 3, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 6, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 9, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 15, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 18, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 21, 3)        
        gl.glBindVertexArray(0)
        self.shader.liberar_programa()
