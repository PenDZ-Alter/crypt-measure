import os

number_of_bytes = 1024 * 1024

# Generate 16 karakter acak
random_text = os.urandom(number_of_bytes).hex()[:number_of_bytes]

# Simpan ke file
with open("plaintext.txt", "w", encoding="utf-8") as file:
    file.write(random_text)

print(f"File plaintext.txt berhasil dibuat dengan isi: {random_text}")
