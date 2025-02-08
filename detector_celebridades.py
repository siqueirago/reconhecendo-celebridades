import face_recognition
import cv2
from PIL import Image



imagem_referencia = face_recognition.load_image_file("imagens/cristiano_ronaldo.jpg")
rosto_referencia = face_recognition.face_encodings(imagem_referencia)[0]

# Carregar a imagem com os outros rostos
imagem_comparacao = cv2.imread("images/bbc.jpg")

# Converter a imagem para o formato RGB (face_recognition precisa deste formato)
imagem_rgb = cv2.cvtColor(imagem_comparacao, cv2.COLOR_BGR2RGB)

# Encontrar os rostos na imagem de compara��o
localizacoes_rostos = face_recognition.face_locations(imagem_rgb)
codificacoes_rostos = face_recognition.face_encodings(imagem_rgb, localizacoes_rostos)

# Comparar o rosto de refer�ncia com os outros rostos
for (topo, direita, embaixo, esquerda), codificacao_rosto in zip(localizacoes_rostos, codificacoes_rostos):
    resultados = face_recognition.compare_faces([rosto_referencia], codificacao_rosto)

    if resultados[0]:
        # Desenhar um ret�ngulo verde ao redor do rosto correspondente
        cv2.rectangle(imagem_comparacao, (esquerda, topo), (direita, embaixo), (0, 255, 0), 2)
    else:
        # Desenhar um ret�ngulo vermelho ao redor dos rostos n�o correspondentes
        cv2.rectangle(imagem_comparacao, (esquerda, topo), (direita, embaixo), (0, 0, 255), 2)

# Exibir a imagem com os resultados
cv2.imshow("Comparacao de Rostos", imagem_comparacao)
cv2.waitKey(0)
cv2.destroyAllWindows()