from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from pathlib import Path
app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

"""
app.mount("/ui", StaticFiles(directory="ui"), name="ui")
templates = Jinja2Templates(directory="ui")
"""

app.mount("/ui", StaticFiles(directory=str(BASE_DIR / "ui")), name="ui")
templates = Jinja2Templates(directory=str(BASE_DIR / "ui"))

active_connections: list[WebSocket] = []

@app.get("/", response_class=HTMLResponse)
async def get_chat_room(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        
        while True:
            
            raw_data = await websocket.receive_text()
            
           
            for connection in active_connections:
               
                is_me = (connection == websocket)
                
                
                await connection.send_text(json.dumps({
                    "message": raw_data,
                    "isMe": is_me
                }))
                
    except WebSocketDisconnect:
        
        print("INFO: Un cliente se ha desconectado de forma segura.")
        active_connections.remove(websocket)
        
    except Exception as e:
       
        print(f"ERROR inesperado en el WebSocket: {e}")
        if websocket in active_connections:
            active_connections.remove(websocket)