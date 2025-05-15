from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Pode mudar para algo mais seguro
socketio = SocketIO(app)

# Rota principal que renderiza o index.html
@app.route('/')
def index():
    return render_template('index.html')

# Função para lidar com mensagens enviadas via socket
@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem recebida: {msg}')
    send(msg, broadcast=True)  # Envia para todos os clientes conectados

if __name__ == '__main__':
    socketio.run(app, debug=True)