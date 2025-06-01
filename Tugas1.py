import tkinter as tk
from tkinter import ttk
from tkinter import font

def hitung_kata():
    teks = entry.get("1.0", tk.END).lower().replace(".", "")
    words = teks.split()
    counts = {}

    for i in range(len(words)):
        kata1 = words[i]
        count = 0
        for j in range(len(words)):
            kata2 = words[j]
            if kata1 == kata2:
                count += 1
        counts[kata1] = count

    # Tampilkan hasil
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    for kata, jumlah in counts.items():
        result_text.insert(tk.END, f"{kata}: {jumlah}\n")
    result_text.config(state=tk.DISABLED)

# Setup window
root = tk.Tk()
root.title("Penghitung Jumlah Kata")
root.geometry("600x500")
root.configure(bg="#ffffff")

# Gaya huruf
judul_font = font.Font(family="Helvetica", size=16, weight="bold")
isi_font = font.Font(family="Arial", size=11)

# Judul
judul = tk.Label(root, text="Penghitung Jumlah Kata", bg="#f0f4f7", fg="#333", font=judul_font)
judul.pack(pady=10)

# Label Input
label = tk.Label(root, text="Masukkan Kalimat:", bg="#f0f4f7", fg="#333", font=isi_font)
label.pack()

# Entry Text
entry = tk.Text(root, height=5, width=60, font=isi_font, wrap="word", bg="white", relief=tk.RIDGE, bd=2)
entry.pack(pady=5)

# Tombol
button = ttk.Button(root, text="Hitung Kata", command=hitung_kata)
button.pack(pady=10)

# Label Hasil
result_label = tk.Label(root, text="Hasil:", bg="#f0f4f7", fg="#333", font=isi_font)
result_label.pack()

# Output Text
result_text = tk.Text(root, height=12, width=60, font=isi_font, bg="#fdfdfd", relief=tk.SUNKEN, bd=2, state=tk.DISABLED)
result_text.pack(pady=5)

# Jalankan
root.mainloop()
