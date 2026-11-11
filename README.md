<div align="center">

# 🙂 Login por Reconhecimento Facial

**App desktop em Python que cadastra usuários pelo rosto e faz login pela webcam, usando dlib e face_recognition.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-008000?style=for-the-badge)
![face_recognition](https://img.shields.io/badge/face__recognition-FF6F00?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

</div>

---

## 💡 Sobre

Projeto de estudo de autenticação biométrica: em vez de senha, o usuário se cadastra mostrando o rosto para a câmera e depois faz login da mesma forma. O sistema extrai um descritor facial de 128 dimensões com a rede ResNet do dlib e compara o rosto capturado com os cadastrados pela distância entre os descritores.

## ✨ Funcionalidades

- **Menu gráfico (Tkinter)** com as opções Cadastrar, Login e Sair.
- **Cadastro com câmera** — pede o nome, mostra o vídeo ao vivo e salva a foto em `usuarios/<nome>.jpg`.
- **Sem cadastro duplicado** — antes de salvar, compara o rosto com todos os já cadastrados.
- **Detecção estável** — só captura depois de 5 frames seguidos com rosto detectado.
- **Login facial** — compara o rosto da webcam com os cadastrados (distância < 0,6) e dá boas-vindas pelo nome.
- **Desempenho** — resolução 640×480 e frame reduzido pela metade antes do processamento.

## 🔄 Como funciona

```text
main.py (menu Tkinter)
├── Cadastrar → cadastro.py
│     webcam → 5 frames com rosto → já existe? → salva usuarios/<nome>.jpg
└── Login → login.py
      carrega usuarios/*.jpg → descritor 128-D (dlib ResNet)
      webcam → [Espaço] captura → menor distância < 0.6 → "Bem-vindo, <nome>!"
                                                      → senão "Usuário não reconhecido."
```

## 🛠️ Tecnologias

- **Python 3**
- **dlib** — detector frontal, 68 landmarks e modelo ResNet de reconhecimento
- **face_recognition** — encodings e cálculo de distância
- **OpenCV** — captura e exibição da webcam
- **Tkinter + Pillow** — interface gráfica
- **NumPy**

## 🚀 Como rodar

Requer uma webcam. A instalação do `dlib` precisa de CMake e de um compilador C++ (no Windows, Visual Studio Build Tools).

```bash
git clone https://github.com/KevinLopes23/Sistema-de-Reconhecimento-Facial-com-Cadastro-e-Login.git
cd Sistema-de-Reconhecimento-Facial-com-Cadastro-e-Login
pip install face_recognition dlib opencv-python Pillow numpy
python main.py
```

Os modelos `shape_predictor_68_face_landmarks.dat` e `dlib_face_recognition_resnet_model_v1.dat` já estão no repositório e precisam ficar na mesma pasta dos scripts. No login, pressione **Espaço** para tentar autenticar e **Esc** para sair.

## 📄 Licença

Distribuído sob a licença [MIT](LICENSE).

## 👤 Autor

Feito por [Kevin Lopes](https://github.com/KevinLopes23)
