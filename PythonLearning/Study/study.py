import random

hit_damage = random.randint(10, 25)


hero_stat = ["Arthur", 5, 100]
hero_stat[1] = 6
hero_stat.append("红药水")
print(hero_stat)

enemies = ["哥布林", "史莱姆", "恶龙"]
for item in enemies:
    print(f"警告！前方出现{item}")


def attack(target):
    print(f"Arthur向{target}挥舞大剑！")
    print(f"对{target}造成15点伤害")
attack(enemies[0])

def calculate_hp(current_hp, hit_damage):
    goblin_hp = current_hp - hit_damage
    return goblin_hp

hp = calculate_hp(50, hit_damage)
print(f"{enemies[0]}剩余血量：{hp}, {hero_stat[0]}对其造成了{hit_damage}点伤害")
