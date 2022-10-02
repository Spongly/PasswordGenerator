import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pass_length = 32

passw = ''
for i in range(pass_length):
  passw += ''.join(secrets.choice(alphabet))

print(passw)
