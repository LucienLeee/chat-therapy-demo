import subprocess
import re

def get_pid(port):
    """获取占用指定端口的进程ID"""
    try:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True,
            text=True
        )
        for line in result.stdout.splitlines():
            if f":{port}" in line:
                parts = line.split()
                pid = parts[-1]
                return pid
        return None
    except Exception as e:
        print(f"获取端口{port}的进程ID时出错: {e}")
        return None

def kill_process(pid):
    """终止指定进程ID的进程"""
    try:
        subprocess.run(["taskkill", "/PID", pid, "/F"])
        print(f"进程{pid}已被终止。")
    except Exception as e:
        print(f"终止进程{pid}时出错: {e}")

def main():
    port = 7860
    pid = get_pid(port)
    if pid:
        print(f"端口{port}被进程{pid}占用，正在终止...")
        kill_process(pid)
    else:
        print(f"没有进程占用端口{port}。")

if __name__ == "__main__":
    main()
