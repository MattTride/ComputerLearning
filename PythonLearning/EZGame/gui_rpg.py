import tkinter as tk
#1.创建主窗口
window = tk.Tk()
window.title("Arthur的冒险")
window.geometry("600x400")

status_label = tk.Label(window, text="欢迎来到新手村，前方出现了一只哥布林", font=("Arial", 20))
status_label.pack()

def on_attack_click():
    status_label.config(text="横扫暴击！")

# 注意看最后，去掉了括号！
attact_btn = tk.Button(window, text="横扫暴击", font=("Arial", 16), command=on_attack_click)
attact_btn.pack()

window.mainloop()