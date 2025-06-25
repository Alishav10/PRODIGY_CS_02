# PRODIGY_CS_02
# Image Encryption Tool with GUI - Task 2
This is Task 2 of my Cybersecurity Internship at **Prodigy InfoTech**.
## About the Project
This Python-based tool allows you to **encrypt and decrypt image files** using a simple XOR-based algorithm. It features a **user-friendly GUI made with Tkinter**, making it easy to interact with.
## What is XOR Encryption?
Each byte of the image is XOR-ed (exclusive OR) with a key. The same key is used to decrypt it. If the wrong key is used, the image remains scrambled.
## Features
- Select image files (`.png`, `.jpg`, `.jpeg`, etc.)
- Input encryption/decryption key
- Encrypt button to hide the image
- Decrypt button to recover the image
- Confirmation messages and output images saved automatically
##Technologies Used
- Python
- Tkinter (built-in GUI library)
- XOR encryption logic (no external libraries)
## Files Included
- `image_encryptor_gui.py` – Main application script
- `input.png` – Test image (user-supplied)
- `encrypted_image.png` – Output after encryption
- `decrypted_image.png` – Output after decryption
- `README.md` – Project documentation

