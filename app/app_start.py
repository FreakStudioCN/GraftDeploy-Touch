# app_start.py - 应用入口文件
from app_utils import AppResources

# 全局应用实例（方便外部终止）
app_instance = None

def start_app():
    """启动应用（核心函数）"""
    global app_instance
    app_instance = AppResources()
    print("\n===== 应用启动成功 =====")
    # 应用主循环（可被外部中断）
    while app_instance.is_running:
        app_instance.led_blink()

def stop_app():
    """停止应用并释放资源（供外部调用）"""
    global app_instance
    if app_instance:
        app_instance.release_resources()
        app_instance = None
        print("\n===== 应用已退出 =====")
    else:
        print("应用未运行，无需退出")

# 若直接运行该文件，自动启动应用（可选）
if __name__ == "__main__":
    start_app()