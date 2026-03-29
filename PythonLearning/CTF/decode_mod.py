g = 3
p = 104729
A = 83210
b = 45678 
enc = 'c1cbc6c0d4cbc2c6d5d1ced1c0c8c4d5d6d3dbc8d2'

password = pow(A, b, p)
key = password % 256
enc_bytes = bytes.fromhex(enc)

ordgin = (for x in enc_bytes)





