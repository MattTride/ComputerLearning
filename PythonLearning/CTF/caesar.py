COMMON_WORDS = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL",
                "CAN", "HER", "WAS", "ONE", "OUR", "OUT", "DAY", "GET",
                "HAS", "HIM", "HIS", "HOW", "ITS", "MAY", "NEW", "NOW",
                "OLD", "SEE", "TWO", "WHO", "THIS", "MY", "PASSWORD",
                "PUT", "SAY", "SHE", "TOO", "USE", "IS"]

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            position = ord(char) - ord('A')
            new_position = (position - shift + 26) % 26
            new_char = chr(new_position + ord('A'))
            result += new_char
        else:
            result += char
    return result

def score(text):
    words = text.upper().split()
    return sum(1 for word in words if word in COMMON_WORDS)

def brute_force(text):
    print("暴力破解结果：\n")
    best_score = -1
    best_result = ""
    best_shift = 0

    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        s = score(decrypted)          # ← 对解密结果打分，不是密文

        if s > best_score:
            best_score = s
            best_result = decrypted
            best_shift = shift

        print(f"shift={shift:2d} | 得分={s} | {decrypted}")

    print(f"\n🏆 最可能的答案（shift={best_shift}）：{best_result}")

# 主程序
ciphertext = input("请输入密文：")
print(f"\n密文：{ciphertext}")
brute_force(ciphertext)

