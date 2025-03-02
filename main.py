import time
from Crypto.Cipher import AES, DES, Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Fungsi untuk membaca plaintext dari file
def read_plaintext_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().encode()  # Ubah menjadi bytes

# Fungsi untuk mengukur waktu enkripsi & dekripsi
def measure_time(cipher, mode, key, data):
    cipher_obj = cipher.new(key, mode)
    
    # Enkripsi
    start_enc = time.time()
    encrypted_data = cipher_obj.encrypt(pad(data, cipher.block_size))
    enc_time = time.time() - start_enc

    cipher_obj = cipher.new(key, mode)

    # Dekripsi
    start_dec = time.time()
    decrypted_data = unpad(cipher_obj.decrypt(encrypted_data), cipher.block_size)
    dec_time = time.time() - start_dec

    return enc_time, dec_time

# Baca plaintext dari file
plaintext = read_plaintext_from_file("plaintext.txt") or ""
data = plaintext  # Pastikan dalam bentuk bytes

# Kunci untuk masing-masing algoritma
key_aes = get_random_bytes(16)  # AES-128 bit
key_des = get_random_bytes(8)   # DES-64 bit
key_blowfish = get_random_bytes(16)  # Blowfish dengan panjang kunci variabel

# Pengujian enkripsi & dekripsi
aes_time = measure_time(AES, AES.MODE_ECB, key_aes, data)
des_time = measure_time(DES, DES.MODE_ECB, key_des, data)
blowfish_time = measure_time(Blowfish, Blowfish.MODE_ECB, key_blowfish, data)

# Hasil pengujian
print(f"AES - Enkripsi: {aes_time[0]:.12f} s, Dekripsi: {aes_time[1]:.12f} s")
print(f"DES - Enkripsi: {des_time[0]:.12f} s, Dekripsi: {des_time[1]:.12f} s")
print(f"Blowfish - Enkripsi: {blowfish_time[0]:.12f} s, Dekripsi: {blowfish_time[1]:.12f} s")
