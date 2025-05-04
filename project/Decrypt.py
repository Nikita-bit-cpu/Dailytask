# decrypt.js
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
from cryptography.exceptions import InvalidSignature
import base64
import binascii
from pathlib import Path

def DAES(key, iv):
    segment_path = Path.cwd() / "Segments" / "0.txt"
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    with segment_path.open("rb") as f:
        content = f.read()

    decryptor = cipher.decryptor()
    decrypted_content = decryptor.update(content) + decryptor.finalize()

    with segment_path.open("wb") as f:
        f.write(decrypted_content)

def DBlowFish(key, iv):
    segment_path = Path.cwd() / "Segments" / "1.txt"
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)

    with segment_path.open("rb") as f:
        content = f.read()

    decryptor = cipher.decryptor()
    decrypted_content = decryptor.update(content) + decryptor.finalize()

    with segment_path.open("wb") as f:
        f.write(decrypted_content)

def DTrippleDES(key, iv):
    segment_path = Path.cwd() / "Segments" / "2.txt"
    backend = default_backend()
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)

    with segment_path.open("rb") as f:
        content = f.read()

    decryptor = cipher.decryptor()
    decrypted_content = decryptor.update(content) + decryptor.finalize()

    with segment_path.open("wb") as f:
        f.write(decrypted_content)

def DIDEA(key, iv):
    segment_path = Path.cwd() / "Segments" / "3.txt"
    backend = default_backend()
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv), backend=backend)

    with segment_path.open("rb") as f:
        content = f.read()

    decryptor = cipher.decryptor()
    decrypted_content = decryptor.update(content) + decryptor.finalize()

    with segment_path.open("wb") as f:
        f.write(decrypted_content)

def DFernet(key):
    segment_path = Path.cwd() / "Segments" / "4.txt"
    fer = Fernet(key)

    with segment_path.open("rb") as f:
        content = f.read()

    try:
        base64.urlsafe_b64decode(content)
        decrypted_content = fer.decrypt(content)
    except (InvalidToken, InvalidSignature, binascii.Error):
        print("Invalid token or signature. Skipping decryption.")
        return

    with segment_path.open("wb") as f:
        f.write(decrypted_content)

def HybridDeCryptKeys():
    original_path = Path.cwd() / "Original.txt"
    infos_dir = Path.cwd() / "Infos"

    with original_path.open("rb") as f:
        key = f.read()

    fer = Fernet(key)

    for info_file in infos_dir.glob("*"):
        print(info_file)

        with info_file.open("rb") as f:
            content = f.read()

        print(content)

        try:
            decrypted_content = fer.decrypt(content)
        except (InvalidToken, InvalidSignature, binascii.Error):
            print(f"Invalid token or signature for {info_file.name}. Skipping decryption.")
            continue

        with info_file.open("wb") as f:
            f.write(decrypted_content)
            print(f"Decrypted {info_file.name}")
