import tkinter as tk
import random


# ================= 1. 核心引擎区 =================
class Role:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self, target):
        damage = random.randint(10, 25)
        target.hp = target.hp - damage
        return f"⚔️ {self.name} 造成了 {damage} 点伤害！\n{target.name} 剩余血量: {target.hp}"

    def heal(self):
        if self.mp >= 10:
            self.mp -= 10
            self.hp += 20
            return f"✨ {self.name} 使用了恢复术！恢复 20 HP，消耗 10 MP"
        else:
            return "❌ 蓝量不足，施法失败！"


# 创建角色实体
hero = Role("Arthur", 100, 50)
goblin = Role("哥布林", 50, 0)


# ================= 2. 视觉窗口区 =================

# tk.Tk() 是 tkinter 的"总部"，它创建整个程序的主窗口
# 一个程序里只能有一个 tk.Tk()，它是所有控件的根容器
window = tk.Tk()
window.title("Arthur的冒险")
window.geometry("600x450")

# ---- 状态栏标签 ----
# tk.Label 专门用来在窗口里显示一段静态或动态文字
# 参数说明：
#   window      -> 这个标签放在哪个容器里（这里放在主窗口）
#   text="..."  -> 标签默认显示的文字
#   font=(字体, 大小) -> 字体设置
#   fg="颜色"   -> fg 是 foreground（前景色），也就是文字颜色
#   justify=    -> 多行文字的对齐方式（LEFT / CENTER / RIGHT）
status_bar = tk.Label(
    window,
    text="",          # 先留空，等 refresh_status() 函数来填
    font=("Arial", 13),
    fg="#555555",
    justify=tk.CENTER
)
# .pack() 把控件"打包"放进窗口，pady 是上下留白的像素距离
status_bar.pack(pady=8)

# ---- 战报标签 ----
# wraplength 控制文字超过多少像素就自动换行，防止文字溢出窗口
battle_log = tk.Label(
    window,
    text=f"遭遇 {goblin.name}！准备战斗！",
    font=("Arial", 16),
    wraplength=500,
    justify=tk.CENTER
)
battle_log.pack(pady=30)

# ---- 按钮区域 ----
# tk.Frame 是一个"透明的容器盒子"，本身不显示内容
# 我们用它来把多个按钮横向排在一行（默认 pack 是竖向排列的）
btn_frame = tk.Frame(window)
# side=tk.LEFT 表示从左向右依次排列，而不是从上往下
# padx 是左右留白

attack_btn = tk.Button(
    btn_frame,
    text="横扫暴击 ⚔️",
    font=("Arial", 15),
    width=14,         # width 控制按钮的宽度（单位是字符数）
    command=lambda: on_attack_click()  # lambda 是一种匿名函数写法，等价于 command=on_attack_click
)
attack_btn.pack(side=tk.LEFT, padx=10)

heal_btn = tk.Button(
    btn_frame,
    text="圣光治疗 ✨",
    font=("Arial", 15),
    width=14,
    command=lambda: on_heal_click()
)
heal_btn.pack(side=tk.LEFT, padx=10)

btn_frame.pack(pady=10)

# ---- 重新开始按钮 ----
# 这个按钮单独一行，初始时隐藏
restart_btn = tk.Button(
    window,
    text="重新开始 🔄",
    font=("Arial", 14),
    command=lambda: restart_game()
)
# 注意：这里暂时先不 .pack()，等游戏结束时再让它出现


# ================= 3. 功能函数区 =================

def refresh_status():
    """
    每次行动后调用这个函数，用 .config() 刷新状态栏的文字。
    .config() 是 tkinter 里用来"遥控修改控件属性"的万能方法。
    创建完控件后，随时都可以用它修改 text、fg（字体颜色）、bg（背景色）等属性。
    """
    status_bar.config(
        text=f"Arthur — HP: {hero.hp}  MP: {hero.mp}        哥布林 — HP: {goblin.hp}"
    )


def end_game(message):
    """
    游戏结束时调用：
    1. 把结束信息显示到战报栏
    2. 用 .config(state=tk.DISABLED) 禁用攻击和治疗按钮
       state 有两个值：tk.NORMAL（正常可点击）和 tk.DISABLED（灰色不可点击）
    3. 让重新开始按钮出现（用 .pack() 把它添加到窗口里）
    """
    battle_log.config(text=message)
    attack_btn.config(state=tk.DISABLED)   # 禁用按钮，玩家无法再点击
    heal_btn.config(state=tk.DISABLED)
    restart_btn.pack(pady=15)              # 游戏结束后才把重新开始按钮显示出来


def restart_game():
    """
    重新开始游戏：
    把英雄和哥布林的属性重置，然后恢复按钮，隐藏重新开始按钮。
    """
    # 重置角色数据（直接修改对象的属性）
    hero.hp = 100
    hero.mp = 50
    goblin.hp = 50

    # 恢复战报和状态栏
    battle_log.config(text=f"遭遇 {goblin.name}！准备战斗！")
    refresh_status()

    # 用 .config(state=tk.NORMAL) 把按钮重新激活
    attack_btn.config(state=tk.NORMAL)
    heal_btn.config(state=tk.NORMAL)

    # .pack_forget() 是 .pack() 的反操作：把控件从窗口里"藏起来"
    # 控件本身还存在（没有被销毁），只是暂时看不见了
    restart_btn.pack_forget()


def check_game_over():
    """
    检查游戏是否结束，返回 True（已结束）或 False（继续）。
    把判断逻辑单独抽成函数，这样攻击和治疗两个事件都能复用它，不用写两遍。
    """
    if goblin.hp <= 0:
        end_game(f"🎉 {goblin.name} 倒下了！\nArthur 获胜！")
        return True
    if hero.hp <= 0:
        end_game(f"💀 Arthur 倒下了！\nGame Over...")
        return True
    return False


def on_attack_click():
    # 如果游戏已经结束就什么都不做
    if goblin.hp <= 0 or hero.hp <= 0:
        return

    # 英雄攻击
    hero_report = hero.attack(goblin)

    # 检查哥布林是否死亡
    if check_game_over():
        refresh_status()
        return

    # 哥布林还活着，触发反击
    goblin_report = goblin.attack(hero)
    final_report = f"{hero_report}\n\n敌人反击！{goblin_report}"
    battle_log.config(text=final_report)

    # 检查 Arthur 是否死亡
    check_game_over()

    # 刷新状态栏（无论谁死了都要刷新一次，显示最终数据）
    refresh_status()


def on_heal_click():
    if goblin.hp <= 0 or hero.hp <= 0:
        return

    # 英雄施法（heal 函数会返回施法成功或失败的文字）
    heal_report = hero.heal()

    # 不管施法成不成功，哥布林都会趁机反击
    goblin_report = goblin.attack(hero)
    final_report = f"{heal_report}\n\n敌人趁机反击！{goblin_report}"
    battle_log.config(text=final_report)

    # 检查 Arthur 有没有被打死
    check_game_over()

    refresh_status()


# ================= 4. 启动区 =================

# 程序刚启动时先刷新一次状态栏，把初始数值填进去
refresh_status()

# window.mainloop() 必须放在最后一行
# 它会启动 tkinter 的"事件监听循环"，让窗口一直保持打开状态
# 并且随时监听用户的鼠标点击、键盘输入等事件
# 如果没有这行，窗口会一闪而过立刻关闭
window.mainloop()