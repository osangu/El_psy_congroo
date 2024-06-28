# 1. Process Socket
# 2. WebSocket(4 hand shake, packet structure)
# 3. How does fastapi implement websocket

from app import create_app

app = create_app()

if __name__ == '__main__':
    from uvicorn import run

    run(app)
