import psutil

def find_process_by_port(port):
    """通过端口号查找进程ID"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    return proc.pid
        except psutil.AccessDenied:
            continue
    return None

def kill_process(pid):
    """终止指定进程ID的进程"""
    try:
        proc = psutil.Process(pid)
        proc.kill()  # 强制终止进程
        proc.wait(timeout=3)
        print(f"进程 {pid} 已被强制终止。")
    except psutil.NoSuchProcess:
        print(f"进程 {pid} 不存在。")
    except psutil.AccessDenied:
        print(f"没有权限终止进程 {pid}。")
    except psutil.TimeoutExpired:
        print(f"强制终止进程 {pid} 超时。")
    except Exception as e:
        print(f"强制终止进程 {pid} 时出错: {e}")

def main():
    port = 7860
    pid = find_process_by_port(port)
    if pid:
        print(f"端口 {port} 被进程 {pid} 占用，正在强制终止...")
        kill_process(pid)
    else:
        print(f"没有进程占用端口 {port}。")

if __name__ == "__main__":
    main()
