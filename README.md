
LUCIDE-CHAT - Real-Time WebSocket Application
-----------------------------------------------------------------------------------------------------------------------
A lightweight, production-structured real-time chat application built with FastAPI (Python) and 
Native Web Technologies (HTML5 and CSS3). 
This project demonstrates how to implement a bidirectional communication channel using WebSockets 
without complex frontend frameworks.

-----------------------------------------------------------------------------------------------------------------------
FEATURES
- Real-Time Communication: Instant message delivery to all connected clients via WebSockets.

- Clean Architecture: A monolithic directory structure separating static assets, styles, and backend logic.

- Responsive Design: Mobile-first user interface styled with native CSS, featuring the classic left/right 
message alignment depending on the sender.

- Safe Lifecycle Management: Robust connection handling with dedicated `try-except` blocks for clean 
client disconnections.

-----------------------------------------------------------------------------------------------------------------------
PROJECT STRUCTURE

src/
 |__ main.py
       |__ ui/
               |__ index.html
               |__ assets/
                      |__ styles.css
               |__ static/
               |__ png-de-fondo.png
  |__ requirements.txt
  |__ README.md

Thanks for read... Made with too much love 🥰🥰