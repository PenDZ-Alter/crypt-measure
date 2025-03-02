# Crypt Measure
This is a measure of the number of bits required to represent a number in a cryptographic system. That used AES, DES, and Blowfish.

## How to use?
1. Uninstall Unnecessary pip library
    ```bash
    pip uninstall -r unins_req.txt
    ```

2. Install needed pip library
    ```bash
    pip install -r requirements.txt
    ```

3. Generate plain text
    ```bash
    python generate.py
    ```
    You can change the number of bytes inside `generate.py`
    ```python
    number_of_bytes = 1024 * 1024
    ```

4. Run the tester
    ```bash
    python main.py
    ```
    You can measure length of bit in refer this code : 
    ```python
    # Kunci untuk masing-masing algoritma
    key_aes = get_random_bytes(16)  # AES-128 bit = 16 Bytes
    key_des = get_random_bytes(8)   # DES-64 bit = 8 Bytes
    key_blowfish = get_random_bytes(16)  # Blowfish dengan panjang kunci variabel
    ```