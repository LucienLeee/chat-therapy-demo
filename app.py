import os
os.system("python demo_download.py")
os.system('streamlit run demo_chat.py --server.address=0.0.0.0 --server.port 6060')
