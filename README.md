README - Aplicação Flask com WebSockets

Descrição:
-----------
Esta é uma aplicação web simples construída com o framework Flask e utilizando Flask-SocketIO para comunicação em tempo real via WebSockets. A aplicação permite que mensagens enviadas por um usuário sejam transmitidas a todos os usuários conectados (broadcast).

Requisitos:
-----------
- Python 3.10 ou superior
- Flask
- Flask-SocketIO

Instalação:
-----------
1. Clone o repositório ou copie os arquivos da aplicação.
2. Crie um ambiente virtual (opcional, mas recomendado):
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
3. Instale as dependências:
   pip install flask flask-socketio

Execução:
---------
1. Certifique-se de que o arquivo `index.html` está na pasta `templates/`.
2. Execute a aplicação com:
   python nome_do_arquivo.py
   (Substitua `nome_do_arquivo.py` pelo nome real do arquivo Python.)

3. Acesse no navegador:
   http://localhost:5000

Estrutura dos Arquivos:
------------------------
- app.py (ou outro nome): Código principal da aplicação Flask.
- templates/
  └── index.html: Página HTML servida pela rota principal.

Funcionamento:
--------------
- A página inicial é servida na rota `/`.
- Quando um cliente envia uma mensagem, ela é capturada por um WebSocket e retransmitida a todos os outros clientes conectados.
- O `SECRET_KEY` deve ser alterado para algo mais seguro em produção.

Observações:
------------
- Esta aplicação está em modo de desenvolvimento (`debug=True`). Para uso em produção, utilize um servidor como Gunicorn com suporte a WebSocket (ex: eventlet ou gevent).
- Este é um exemplo básico que pode ser estendido com autenticação, histórico de mensagens, suporte a salas, etc.

Autor:
------
Styven

Licença:
--------
(Especifique a licença, ex: MIT, GPL, etc.)
