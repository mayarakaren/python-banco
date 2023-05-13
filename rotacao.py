import cv2
import numpy as np

#Função de rotação simples
def Simples(rotacao_image, angulo):
    #extração da largura e altura da imagem
    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]
    #calculo das coordenadas do ponto central
    y, x = altura / 2, largura / 2
    #Criação da matriz da rotação
    rotacao_matriz = cv2.getRotationMatrix2D((x,y), angulo, 1.0)
    #Aplicação da rotacao da imagem criado na linha na parte de cima
    rotacionando_image = cv2.warpAffine(rotacao_image, rotacao_matriz, (largura, altura))
    #Demonstração da imagem rotacionando
    return rotacionando_image

def complexo (rotacao_image, angulo):
    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]
    y, x = altura/2, largura/2
    rotacao_matriz = cv2.getRotationMatrix2D((y,x), angulo, 1.0)
    #Utilização seno e coseno
    cos = np.abs(rotacao_matriz[0][0])
    seno = np.abs(rotacao_matriz[0][1])
    #calculo nova altura
    nova_altura = int((altura * seno) + largura * cos)
    nova_largura = int((altura * cos) + largura * seno)
    #Criação da Matriz
    rotacao_matriz[0][2] += (nova_largura/2) - x
    rotacao_matriz[1][2] += (nova_altura/2) - y
    #rotacionamento  da imagem
    rotacionando_image = cv2.warpAffine(
        rotacao_image, rotacao_matriz, (nova_largura, nova_altura)
    )
    return rotacionando_image

#escolha da imagem
imagem = cv2.imread("img/noite.jfif", 1)
#definição do angulo a ser utilizado
Normal = Simples(imagem, 40)
Rotacao_Detalhada = complexo(imagem, 40)
cv2.imshow("Imagem normal", imagem)
cv2.imshow("Rotação Cálculo Simples", Normal)
cv2.imshow("Rotação Cálculo Complexo", Rotacao_Detalhada)

cv2.waitKey(0)
cv2.destroyAllWindows()