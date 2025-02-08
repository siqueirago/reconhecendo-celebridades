# Nexa - Análise Avançada de Imagens e Texto com IA na AWS
## AWS Rekognition - Detectando Celebridades em Imagens
O Amazon Rekognition é um serviço da AWS que facilita a adição de análise de imagens e vídeos aos seus aplicativos. Com ele, é possível detectar rostos, identificar celebridades, 
analisar emoções e muito mais. Neste guia, vamos aprender a detectar celebridades em imagens usando o Rekognition
## Descrição
Este projeto em Python utiliza a biblioteca face_recognition para identificar celebridades em imagens. O código compara rostos detectados em uma imagem com um banco de dados de 
rostos de celebridades e marca os rostos identificados com um retângulo verde, exibindo o nome da celebridade. Rostos não identificados são marcados com um retângulo vermelho.

## Funcionalidades
* **Detecção de rostos:** Identifica rostos em imagens utilizando a biblioteca face_recognition.
* **Reconhecimento de celebridades:** Compara os rostos detectados com um banco de dados de celebridades e identifica aquelas presentes na imagem.
* **Marcação de rostos:** Desenha retângulos verdes ao redor dos rostos de celebridades identificadas e retângulos vermelhos para rostos não identificados.
* **Exibição de nomes:** Exibe o nome da celebridade identificada próximo ao rosto.
## Passo 1: Configuração
* Conta AWS: Crie uma conta na AWS em https://aws.amazon.com/pt/.
* Chaves de acesso: Gere suas chaves de acesso (Access Key ID e Secret Access Key) no console da AWS, em "IAM" > "Usuários" > "Suas credenciais de segurança".
* SDK AWS: Instale o SDK da AWS para Python (Boto3):
  
  ``pip intall boto3``
## Passo 2: Código Python
````
import boto3

# Configurar cliente Rekognition
rekognition = boto3.client('rekognition', 
                           aws_access_key_id='SUA_ACCESS_KEY_ID', 
                           aws_secret_access_key='SUA_SECRET_ACCESS_KEY', 
                           region_name='SUA_REGIAO')

# Função para detectar celebridades
def detectar_celebridades(nome_arquivo):
    with open(nome_arquivo, 'rb') as imagem:
        resposta = rekognition.recognize_celebrities(Image={'Bytes': imagem.read()})

    for rosto in resposta['CelebrityFaces']:
        nome = rosto['Name']
        # Informações sobre a celebridade
        id_celebridade = rosto['Id']
        url_info = rosto['Face']['ExternalImageId']
        # Caixa delimitadora do rosto
        caixa = rosto['Face']['BoundingBox']
        print(f"Celebridade: {nome} (ID: {id_celebridade})")
        print(f"Informações: {url_info}")
        print(f"Caixa: {caixa}")

# Exemplo de uso
detectar_celebridades('imagem.jpg')
````
## Passo 3: Explicação do código
* Importação de bibliotecas: Importamos o Boto3 para interagir com a AWS.
* Cliente Rekognition: Criamos um cliente Rekognition com nossas credenciais e região.
* Função detectar_celebridades:
  * Lê a imagem do arquivo.
  * Chama a função recognize_celebrities do Rekognition.
  * Itera sobre os rostos de celebridades detectados.
  * Extrai o nome, ID, informações e caixa delimitadora de cada rosto.
  * Imprime as informações.
## Passo 4: Execução
* Salve o código: Salve o código em um arquivo Python (ex: detectar_celebridades.py).
* Prepare a imagem: Coloque a imagem que você deseja analisar na mesma pasta do código.
* Execute o script:
## Observações
* Região: Certifique-se de usar a região da AWS onde você ativou o Rekognition.
* Custos: O Rekognition é um serviço pago. Consulte a página de preços da AWS para mais informações.
* Limites: O Rekognition possui limites de requisição. Consulte a documentação da AWS para mais informações.
## Recursos adicionais
* Documentação do Amazon Rekognition: [https://aws.amazon.com/pt/rekognition/]
* Documentação do Boto3: [https://boto3.amazonaws.com/v1/documentation/api/latest/index.html]
## Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
