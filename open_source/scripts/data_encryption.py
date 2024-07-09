python
from cryptography.fernet import Fernet

# Generate key
def generate_key():
    return Fernet.generate_key()

# Encrypt data
def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

# Decrypt data
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

# Example usage
if __name__ == "__main__":
    key = generate_key()
    data = "Sensitive information"
    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted Data: {encrypted_data}")
    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Decrypted Data: {decrypted_data}")
