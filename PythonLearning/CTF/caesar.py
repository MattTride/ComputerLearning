def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            char = char.upper()

            position = ord(char) - ord('A')
            new_position = (position - shift + 26)% 26
            new_char = chr(new_position + ord('A'))
            result += new_char
        else:
            result += char

    return result


def brute_force(text):
    print("尝试所有可能的值： \n")
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        print(f"shift = {shift:2d} : {decrypted}")


ciphertext = input("请输入你想破解的代码： ")
print(f"密文: {ciphertext}")
print(f"用 shift=3 解密： {decrypt(ciphertext, 3)}")
print("\n ------暴力破解-------")
brute_force(ciphertext)