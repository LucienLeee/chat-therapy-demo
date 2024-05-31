import os
#模型下载
base_path = './chat-therapy'
# download repo to the base_path directory using git
os.system('apt install git')
os.system('apt install git-lfs')
os.system(f'git clone -b InternLM7b-base https://code.openxlab.org.cn/LucienJMLee/chat-therapy.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
