import tkinter as tk
import random



# ================= 1. 核心引擎区 =================
class Role:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp

    def attack(self, target):
        damage = random.randint(10, 25)
        target.hp = target.hp - damage
        return f"⚔️ {self.name} 造成了 {damage} 点伤害！\n{target.name} 剩余血量: {target.hp}"

    def heal(self):
        if self.mp >= 10:
            self.mp = self.mp - 10
            self.hp = self.hp + 20

            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return f"{self.name}使用了恢复术！恢复20HP，消耗10MP \n当前血量{self.hp},当前蓝量{self.mp}"
        else:
            return "没蓝了"

    def reset_hp(self):
        self.hp = self.max_hp
        self.mp = self.max_mp


hero = Role("Arthur", 100, 50)
goblin = Role("哥布林", 50, 0)

# =================  视觉窗口区 =================
window = tk.Tk()
window.title("Arthur的冒险")
window.geometry("600x400")

def on_attack_click():
    if goblin.hp <= 0:
        status_label.config(text="哥布林被打败了！")
        return

    hero_report = hero.attack(goblin)

    if goblin.hp > 0:
        goblin_report = goblin.attack(hero)
        final_report = f"{hero_report}\n\n敌人反击！{goblin_report}"
    else:
        final_report = f"{hero_report}\n\n哥布林死了"
    status_label.config(text=final_report)

def on_heal_click():
    if goblin.hp <= 0:
        status_label.config(text="哥布林已经死透了，不需要回血了")
        return
    heal_report = hero.heal()
    goblin_report = goblin.attack(hero)
    final_report = f"{heal_report}\n\n{goblin.name}反击了!{goblin_report}"
    status_label.config(text=final_report)

def on_reset_click():
    hero.reset_hp()
    goblin.reset_hp()
    rest_message = (
        f"⏳ 遭遇 {goblin.name}！\n\n"
        f"👤 {hero.name} 状态：HP {hero.hp}/{hero.max_hp} | MP {hero.mp}/{hero.max_mp}\n"
        f"👹 {goblin.name} 状态：HP {goblin.hp}/{goblin.max_hp}"
    )
    status_label.config(text=rest_message)

status_label = tk.Label(window, text=f"遭遇 {goblin.name}！\n当前血量: {goblin.hp}", font=("Arial", 18))
status_label.pack(pady=40)




attack_btn = tk.Button(window, text="横扫暴击 ⚔️", font=("Arial", 16), command=on_attack_click)
heal_btn = tk.Button(window, text="回血", font=("Arial", 16), command=on_heal_click)
reset_btn = tk.Button(window, text="再玩一次", font=("Arial", 16), command=on_reset_click)
attack_btn.pack(pady=10)
heal_btn.pack(pady=10)
reset_btn.pack(pady=20)

window.mainloop()