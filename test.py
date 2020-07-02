import socketio
import eventlet
from flask import Flask

sio = socketio.server()

app = Flask(__name__) #'__main__'

@sio.on('connect')
def connect(sid, environ):
	print('Connected')


if __name__ == '__main__':
	app = socketio.Middleware(sio, app)
	eventlet.wsgi.server(eventlet.listen(('',4567)), app)