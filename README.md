<h1>Sistema de Reconhecimento Facial com Cadastro e Login</h1>

<p>Este projeto implementa um sistema de autenticação que utiliza reconhecimento facial para cadastrar e autenticar usuários. A aplicação oferece uma interface gráfica simples, permitindo que os usuários cadastrem seus rostos e façam login com a câmera do dispositivo. O sistema utiliza bibliotecas avançadas de processamento de imagem e reconhecimento facial, garantindo a identificação precisa de cada usuário.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Cadastro de Usuário</strong>: Capta a imagem do rosto do usuário com a câmera e realiza a verificação para evitar duplicidade de cadastro.</li>
    <li><strong>Login com Reconhecimento Facial</strong>: Autentica o usuário capturando uma imagem ao vivo e comparando-a com as imagens salvas durante o cadastro.</li>
    <li><strong>Interface Gráfica Simples</strong>: Navegação intuitiva com botões para acesso ao cadastro e login.</li>
</ul>

<h2>Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Python</strong></li>
    <li><strong>face_recognition</strong>: Para detecção e reconhecimento facial.</li>
    <li><strong>dlib</strong>: Para reconhecimento de características faciais e cálculo de descritores faciais.</li>
    <li><strong>OpenCV</strong>: Para captura e manipulação de imagens.</li>
    <li><strong>Tkinter</strong>: Para criação da interface gráfica.</li>
    <li><strong>NumPy</strong>: Para manipulação de dados numéricos no cálculo de distâncias entre as faces.</li>
</ul>

<h2>Como Usar</h2>
<ol>
    <li><strong>Cadastro</strong>: Abra a interface gráfica, clique em "Cadastrar" e siga as instruções para capturar a imagem do rosto.</li>
    <li><strong>Login</strong>: Clique em "Login" e olhe para a câmera. O sistema tentará identificar o rosto e autenticar o usuário.</li>
</ol>

<h2>Pré-requisitos</h2>
<p>Para rodar este projeto, você precisará das seguintes bibliotecas Python:</p>
<pre>
face_recognition, dlib, opencv-python, Pillow, numpy
</pre>
<p>Instale as dependências com:</p>
<pre><code>pip install face_recognition dlib opencv-python Pillow numpy</code></pre>

<h2>Observação</h2>
<p>Este projeto requer arquivos <code>.dat</code> específicos para o <strong>dlib</strong>, necessários para o reconhecimento facial. Certifique-se de que os arquivos <code>shape_predictor_68_face_landmarks.dat</code> e <code>dlib_face_recognition_resnet_model_v1.dat</code> estejam no diretório do projeto.</p>

<p>Este projeto é ideal para experimentação e aprendizado em reconhecimento facial, processamento de imagem e autenticação biométrica usando Python.</p>
