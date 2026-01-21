# app_utils.py - 应用依赖/资源模块
import time
import machine

# 模拟资源（比如占用GPIO25的LED、虚拟定时器）
class AppResources:
    def __init__(self):
        # 初始化资源：控制板载LED（GPIO25）
        self.led = machine.Pin("LED", machine.Pin.OUT)
        self.is_running = True  # 控制应用运行的标志
        self.timer_count = 0    # 模拟定时器计数
    
    def led_blink(self):
        """LED闪烁（模拟应用业务逻辑）"""
        if self.is_running:
            self.led.toggle()
            self.timer_count += 1
            print(f"[应用运行中] LED闪烁次数: {self.timer_count} | 资源占用中...")
            time.sleep(0.5)
    
    def release_resources(self):
        """释放所有资源"""
        self.is_running = False
        self.led.off()  # 关闭LED
        print(f"[资源释放] LED已关闭 | 定时器计数停止: {self.timer_count}")
        del self.led    # 释放GPIO资源
        print("[资源释放] 所有应用资源已释放完成")