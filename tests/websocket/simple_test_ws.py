import websocket

ws = websocket.WebSocket()

url = 'ws://192.168.0.13:8123/api/websocket'
ws.connect(url)
ws.send('Hello, World')
