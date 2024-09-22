import secrets

print("Super simple password generator!")

letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = letters.upper()
symbols = " /-+=*&^%#@!();:' "
numbers = "0123456789"

password = ''.join(secrets.choice(letters + upper_letters + symbols + numbers) for i in range(14))

print(password)
