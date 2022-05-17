from OpenGL.GL import *
from Modelo import *

class Bicho(Modelo):

    vivo = True
    def __init__(self, x, y):
        super().__init__(x,y)
        self.extremo_izquierdo = 0.07
        self.extremo_derecho = 0.07
        self.extremo_inferior = 0.07
        self.extremo_superior = 0.07
        
    def actualizar (self):
        if self.vivo:
            if self.posicion.x > 1.05: 
                self.posicion_id[0] = -1.0
            if self.posicion_id[0] < -1.05: 
                self.posicion_id[0] = 1.0
                
            if self.posicion_id[1] > 1.05: 
                self.posicion_id[1] = -1.0   
            if self.posicion_id[1] < -1.05: 
                self.posicion_id[1] = 1.0  


        self.vertices = np.array(
                [
                   -0.02*2.5,0.01*2.5,0,1.0,    0.5,0.18,0.6, 1.0,
                    -0.01*2.5,0.0,0,1.0,     0.5,0.18,0.6,1.0,
                   -0.02*2.5,-0.01*2.5,0,1.0,       0.5,0.18,0.6,1.0,
                    -0.0,-0.03*2.5,0,1.0,     0.5,0.18,0.6,1.0
                   0.02*2.5,-0.01*2.5,0,1.0,    0.5,0.18,0.6, 1.0,
                    0.01*2.5,0.00,1.0,     0.5,0.18,0.6,1.0,
                   0.02*2.5,0.01*2.5,.0,1.0,       0.5,0.18,0.6,1.0,
                    0.00,0.03*2.5,0,1.0,     0.5,0.18,0.6,1.0
                ], dtype="float32"
            )
        
            
def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)

