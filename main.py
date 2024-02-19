from backend.server import app
from dotenv import load_dotenv
from pyngrok import ngrok
load_dotenv()

def start_ngrok():
    ngrok_tunnel = ngrok.connect(8000, "tcp")
    print("ngrok URL:", ngrok_tunnel.public_url)
    return ngrok_tunnel.public_url


if __name__ == "__main__":
    import uvicorn
    ngrok_url = start_ngrok()
    uvicorn.run(app, host="127.0.0.1", port=8000)