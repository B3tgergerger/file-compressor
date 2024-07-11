import os
import zipfile
import tarfile
import zstandard as zstd
import brotli
import customtkinter as ctk
from tkinter import filedialog, messagebox

def compress_files(files, method='zip', level=1, password=None):
    if method == 'zip':
        return compress_zip(files, level, password)
    elif method == 'tar':
        return compress_tar(files, level)
    elif method == 'gzip':
        return compress_gzip(files, level)
    elif method == 'zstandard':
        return compress_zstd(files, level)
    elif method == 'brotli':
        return compress_brotli(files, level)
    else:
        raise ValueError("Unsupported compression method")

def compress_zip(files, level, password):
    zip_filename = 'compressed_files.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file)
        if password:
            zipf.setpassword(password.encode())
    return zip_filename

def compress_tar(files, level):
    tar_filename = 'compressed_files.tar'
    with tarfile.open(tar_filename, 'w') as tarf:
        for file in files:
            tarf.add(file)
    return tar_filename

def compress_gzip(files, level):
    tar_filename = 'compressed_files.tar.gz'
    with tarfile.open(tar_filename, 'w:gz') as tarf:
        for file in files:
            tarf.add(file)
    return tar_filename

def compress_zstd(files, level):
    zstd_filename = 'compressed_files.zst'
    cctx = zstd.ZstdCompressor(level=level)
    with open(zstd_filename, 'wb') as f:
        with cctx.stream_writer(f) as compressor:
            for file in files:
                with open(file, 'rb') as input_file:
                    compressor.write(input_file.read())
    return zstd_filename

def compress_brotli(files, level):
    brotli_filename = 'compressed_files.br'
    with open(brotli_filename, 'wb') as f:
        for file in files:
            with open(file, 'rb') as input_file:
                compressed_data = brotli.compress(input_file.read(), quality=level)
                f.write(compressed_data)
    return brotli_filename

def extract_files(filename):
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename, 'r') as zipf:
            zipf.extractall()
    elif filename.endswith('.tar.gz') or filename.endswith('.tgz'):
        with tarfile.open(filename, 'r:gz') as tarf:
            tarf.extractall()
    elif filename.endswith('.tar'):
        with tarfile.open(filename, 'r') as tarf:
            tarf.extractall()
    elif filename.endswith('.zst'):
        with open(filename, 'rb') as compressed:
            dctx = zstd.ZstdDecompressor()
            with open('extracted_files', 'wb') as output:
                dctx.copy_stream(compressed, output)
    elif filename.endswith('.br'):
        with open(filename, 'rb') as compressed:
            decompressed_data = brotli.decompress(compressed.read())
            with open('extracted_files', 'wb') as output:
                output.write(decompressed_data)
    else:
        raise ValueError("Unsupported file format")

class FileCompressorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Compressor")
        self.geometry("600x500")

        self.method_var = ctk.StringVar(value='zip')
        self.level_var = ctk.IntVar(value=1)
        self.password_var = ctk.StringVar()
        self.files = []

        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Compression Method:").pack(pady=10)
        methods = ['zip', 'tar', 'gzip', 'zstandard', 'brotli']
        for method in methods:
            ctk.CTkRadioButton(self, text=method, variable=self.method_var, value=method).pack(anchor='w')

        ctk.CTkLabel(self, text="Compression Level (1-22):").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.level_var).pack()

        ctk.CTkLabel(self, text="Password (optional):").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.password_var, show='*').pack()

        ctk.CTkButton(self, text="Select Files", command=self.select_files).pack(pady=10)
        ctk.CTkButton(self, text="Start Compression", command=self.start_compression).pack(pady=10)
        ctk.CTkButton(self, text="Extract Files", command=self.extract_files).pack(pady=10)

    def select_files(self):
        self.files = filedialog.askopenfilenames()
        messagebox.showinfo("Selected Files", f"Selected {len(self.files)} files.")

    def start_compression(self):
        if not self.files:
            messagebox.showwarning("No Files", "Please select files to compress.")
            return

        method = self.method_var.get()
        level = self.level_var.get()
        password = self.password_var.get() or None

        try:
            output_file = compress_files(self.files, method, level, password)
            messagebox.showinfo("Success", f"Files compressed to {output_file}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract_files(self):
        file = filedialog.askopenfilename()
        if not file:
            return

        try:
            extract_files(file)
            messagebox.showinfo("Success", "Files extracted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = FileCompressorApp()
    app.mainloop()
