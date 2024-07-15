def encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted += char
    return decrypted

def main():
    while True:
        print("\nMenu:")
        print("1. Enkripsi plaintext")
        print("2. Deskripsi plaintext")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")
        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            key = input("Masukkan key (1-25): ")
            try:
                key = int(key)
                if 1 <= key <= 25:
                    encrypted_text = encrypt(plaintext, key)
                    print(f"Hasil enkripsi: {encrypted_text}")
                else:
                    print("Key harus antara 1 dan 25")
            except ValueError:
                print("Key harus berupa bilangan bulat.")
        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            key = input("Masukkan key (1-25): ")
            try:
                key = int(key)
                if 1 <= key <= 25:
                    decrypted_text = decrypt(ciphertext, key)
                    print(f"Hasil deskripsi: {decrypted_text}")
                else:
                    print("Key harus antara 1 dan 25")
            except ValueError:
                print("Key harus berupa bilangan bulat.")
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")



if __name__ == "__main__":
    main()
