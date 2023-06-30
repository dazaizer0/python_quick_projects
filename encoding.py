import base64

def encode(password):
    encoded = base64.b64encode(password.encode())
    encoded = str(encoded)
    encoded = encoded[2:]
    encoded = encoded[:-1]

    print(f'encoded password: {encoded}')

def decode(password):
    decode_password = base64.b64decode(password)
    decode_data = decode_password.decode()

    print(f'decode password: {decode_data}')

choice = input("encode or decode: ")

if choice == 'encode':
    user_pass = input("enter your password: ")
    encode(user_pass)
elif choice == 'decode':
    user_pass = input("enter your encoded password: ")
    decode(user_pass)

print("finish.", end="")
