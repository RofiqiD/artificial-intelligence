import tkinter as tk
from tkinter import ttk
from tkinter import font

# Fungsi brute force untuk menandai posisi kata
def brute_force_positions(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    i = 0
    while i <= n - m:
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append((i, i + m))
            i += m
        else:
            i += 1
    return positions

# Fungsi untuk memproses teks dan mewarnai hasil
def proses_teks():
    # Ambil teks dan kata kunci
    paragraph = entry_paragraph.get("1.0", tk.END).strip()
    keyword = entry_keyword.get().strip()
    hasil_text.delete("1.0", tk.END)

    if paragraph and keyword:
        hasil_text.insert(tk.END, paragraph)

        # Bersihkan tag lama
        hasil_text.tag_remove("highlight", "1.0", tk.END)

        # Cari posisi menggunakan brute force
        positions = brute_force_positions(paragraph, keyword)

        # Tandai setiap posisi yang cocok
        for start, end in positions:
            start_index = f"1.0 + {start} chars"
            end_index = f"1.0 + {end} chars"
            hasil_text.tag_add("highlight", start_index, end_index)

# GUI
root = tk.Tk()
root.title("Algoritma Brute force ")
root.geometry("600x400")

# Frame input
frame_input = ttk.Frame(root, padding=10)
frame_input.pack(fill="x")

label_paragraph = ttk.Label(frame_input, text="Masukkan Paragraf:")
label_paragraph.pack(anchor="w")
entry_paragraph = tk.Text(frame_input, height=5)
entry_paragraph.pack(fill="x")

label_keyword = ttk.Label(frame_input, text="Masukkan Kata yang Dicari:")
label_keyword.pack(anchor="w", pady=(10, 0))
entry_keyword = ttk.Entry(frame_input)
entry_keyword.pack(fill="x")

btn_proses = ttk.Button(frame_input, text="Proses", command=proses_teks)
btn_proses.pack(pady=10)

# Frame hasil
frame_hasil = ttk.Frame(root, padding=10)
frame_hasil.pack(fill="both", expand=True)

label_hasil = ttk.Label(frame_hasil, text="Hasil:")
label_hasil.pack(anchor="w")
hasil_text = tk.Text(frame_hasil, height=10)
hasil_text.pack(fill="both", expand=True)

# Definisikan tag highlight (warna kuning)
hasil_text.tag_config("highlight", background="yellow", foreground="black")

# Jalankan GUI
root.mainloop()
