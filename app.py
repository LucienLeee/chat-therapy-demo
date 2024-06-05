import os
os.system("python demo_download.py LucienJMLee/chat-therapy")
os.system('streamlit run demo_chat.py --server.address=0.0.0.0 --server.port 7860')
