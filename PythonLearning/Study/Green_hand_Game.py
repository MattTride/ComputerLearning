import random

player = {
    "name":"Arthur",
    "hp":100
}

enemy = {
    "name":"哥布林",
    "hp":50
}



while player["hp"] > 0 and enemy["hp"] > 0:
    player_hit = random.randint(10, 25)
    enemy["hp"] = enemy["hp"] - player_hit
    if enemy["hp"] <= 0:
        break
    else:
        enemy_hit = random.randint(5, 15)
        player["hp"] = player["hp"] - enemy_hit
        if player["hp"] <= 0:
            print(f"{player["name"]}倒下了！Game Over!")
            break
    print(f"当前双方剩余血量：{player["name"]}: {player["hp"]}  and {enemy["name"]}：{enemy["hp"]}")
    input("按回车键进入下一回合...")


