import random

class Role:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self, target):
        damage = random.randint(10,25)
        target.hp = target.hp - damage
        print(f"{self.name}攻击了{target.name}, 造成了{damage}点伤害")

    def heal(self):
        if self.mp >= 10:
            self.mp = self.mp - 10
            self.hp = self.hp + 20
            print(f"{self.name}使用了治疗术")
            print(f"{self.name}当前状态{self.hp}, {self.mp}")
        else:
            print(f"❌法力不足")

hero = Role("Arthur", 100, 50)
goblin = Role("Goblin", 50, 0)

while hero.hp > 0 and goblin.hp > 0:
    print(f"{hero.name}的回合")
    choice = input("攻击1，回血2: ")
    if choice == "1":
        hero.attack(goblin)
    elif choice == "2":
        hero.heal()
    else:
        print("输入错误，分神了")

    print(f"现在双方血量：{hero.name}:{hero.hp},{goblin.name}:{goblin.hp}")

    if goblin.hp <= 0:
        print(f"{goblin.name}被击败了，{hero.name}获胜！")
        break

    if goblin.hp > 0:
        goblin.attack(hero)
        print(f"现在双方血量：{hero.name}:{hero.hp},{goblin.name}:{goblin.hp}")

    if hero.hp <= 0:
        print(f"废物{hero.name}，连{goblin.name}都打不过")
        break
