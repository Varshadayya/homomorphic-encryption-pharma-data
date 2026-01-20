from phe import paillier


def encrypt_pharma_data(data, public_key):
    encrypted_data = []
    for value in data:
        encrypted_data.append(public_key.encrypt(value))
    return encrypted_data


def compute_on_encrypted_data(encrypted_data):
    total = encrypted_data[0]
    for value in encrypted_data[1:]:
        total += value
    return total


def decrypt_result(encrypted_result, private_key):
    return private_key.decrypt(encrypted_result)


if __name__ == "__main__":
    # Generate public and private keys
    public_key, private_key = paillier.generate_paillier_keypair()

    # Sample pharmaceutical data (e.g., drug sales values)
    pharma_data = [1200, 1500, 1800, 2100]

    encrypted_data = encrypt_pharma_data(pharma_data, public_key)
    encrypted_sum = compute_on_encrypted_data(encrypted_data)
    decrypted_sum = decrypt_result(encrypted_sum, private_key)

    print("Original Data:", pharma_data)
    print("Encrypted Computation Result (Hidden)")
    print("Decrypted Total Value:", decrypted_sum)
