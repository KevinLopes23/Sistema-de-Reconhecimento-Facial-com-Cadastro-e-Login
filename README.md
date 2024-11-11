Sistema de Reconhecimento Facial com Cadastro e Login
Este projeto implementa um sistema de autenticação que utiliza reconhecimento facial para cadastrar e autenticar usuários. A aplicação oferece uma interface gráfica simples, permitindo que os usuários cadastrem seus rostos e façam login com a câmera do dispositivo. O sistema utiliza bibliotecas avançadas de processamento de imagem e reconhecimento facial, garantindo a identificação precisa de cada usuário.

Funcionalidades
Cadastro de Usuário: Capta a imagem do rosto do usuário com a câmera e realiza a verificação para evitar duplicidade de cadastro.
Login com Reconhecimento Facial: Autentica o usuário capturando uma imagem ao vivo e comparando-a com as imagens salvas durante o cadastro.
Interface Gráfica Simples: Navegação intuitiva com botões para acesso ao cadastro e login.
Tecnologias Utilizadas
Python
face_recognition: Para detecção e reconhecimento facial.
dlib: Para reconhecimento de características faciais e cálculo de descritores faciais.
OpenCV: Para captura e manipulação de imagens.
Tkinter: Para criação da interface gráfica.
NumPy: Para manipulação de dados numéricos no cálculo de distâncias entre as faces.
Como Usar
Cadastro: Abra a interface gráfica, clique em "Cadastrar" e siga as instruções para capturar a imagem do rosto.
Login: Clique em "Login" e olhe para a câmera. O sistema tentará identificar o rosto e autenticar o usuário.
Pré-requisitos
Para rodar este projeto, você precisará das seguintes bibliotecas Python:

face_recognition
dlib
opencv-python
Pillow
numpy
Instale as dependências com:

bash
Copiar código
pip install face_recognition dlib opencv-python Pillow numpy
Observação
Este projeto requer arquivos .dat específicos para o dlib, necessários para o reconhecimento facial. Certifique-se de que os arquivos shape_predictor_68_face_landmarks.dat e dlib_face_recognition_resnet_model_v1.dat estejam no diretório do projeto.
