import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def xor_encrypt_decrypt(input_path, key, output_path):
    try:
        with open(input_path, 'rb') as file:
            data = bytearray(file.read())

        for i in range(len(data)):
            data[i] ^= key

        with open(output_path, 'wb') as file:
            file.write(data)

        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, path)

def open_image(path):
    try:
        img = Image.open(path)
        img.show()
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open image: {e}")

def encrypt():
    path = file_entry.get()
    key = key_entry.get()

    if not path or not key:
        messagebox.showwarning("Missing input", "Please select a file and enter a key.")
        return

    try:
        key = int(key)
    except ValueError:
        messagebox.showwarning("Invalid key", "Key must be an integer.")
        return

    output_file = "encrypted_image.png"
    if xor_encrypt_decrypt(path, key, output_file):
        status_label.config(text=f"✅ Encrypted and saved as {output_file}", fg="green")
        messagebox.showinfo("Done", f"Encrypted image saved.\nNow ready to decrypt.")
        
        # 🔁 Auto-load the encrypted image into the path
        file_entry.delete(0, tk.END)
        file_entry.insert(0, output_file)

def decrypt():
    path = file_entry.get()
    key = key_entry.get()

    if not path or not key:
        messagebox.showwarning("Missing input", "Please select a file and enter a key.")
        return

    try:
        key = int(key)
    except ValueError:
        messagebox.showwarning("Invalid key", "Key must be an integer.")
        return

    output_file = "decrypted_image.png"
    if xor_encrypt_decrypt(path, key, output_file):
        status_label.config(text=f"✅ Decrypted and saved as {output_file}", fg="blue")
        open_image(output_file)

# GUI setup
root = tk.Tk()
root.title("Image XOR Encryptor/Decryptor")
root.geometry("500x220")

tk.Label(root, text="Image File:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

tk.Label(root, text="Key (number):").grid(row=1, column=0, padx=10)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1)

tk.Button(root, text="Encrypt", command=encrypt, bg="lightgreen").grid(row=2, column=0, pady=20)
tk.Button(root, text="Decrypt", command=decrypt, bg="lightblue").grid(row=2, column=1)

status_label = tk.Label(root, text="", fg="black")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()