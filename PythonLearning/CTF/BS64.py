import base64
encoded = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg=="
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)

new_encoded = input("请输入需要二次解密的encode：")
new_decoded = base64.b64decode(new_encoded).decode('utf-8')
print(new_decoded)