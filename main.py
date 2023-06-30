import tkinter as tk
from parser_1 import Parser
from lexical import lexical_analyzer

def process():
    # Menghapus teks pada label
    la_output.delete("1.0", tk.END)
    parse_output.delete("1.0", tk.END)

    # Mengambil teks dari input_string dan menghapus spasi di awal dan akhir
    string = input_string.get("1.0", tk.END).strip()

    # Melakukan analisis leksikal pada string input menggunakan lexical_analyzer
    tokens = lexical_analyzer(string)
    la_output.insert(tk.END, tokens) 

    # Melakukan parsing menggunakan parser dengan tokens hasil analisis leksikal
    parser = Parser(tokens)
    if parser.parse():
        parse_result = "Valid"
    else:
        parse_result = "Invalid"
    #parse_result = Parser(tokens).parse
    parse_output.insert(tk.END, parse_result)

# Membuat jendela utama menggunakan modul tkinter
root = tk.Tk()
root.title("TUBES TBA")

# Mengatur ukuran jendela
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Membuat label dan entry untuk inputan
input_label = tk.Label(root, text="Masukkan Formula:")
input_label.grid(row=0, column=0, sticky=tk.W)
input_string = tk.Text(root, height=5, width=60)
input_string.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Membuat tombol "Hitung"
process_button = tk.Button(root, text="Process", command=process)
process_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Membuat label untuk menampilkan hasil token lexical
la_label = tk.Label(root, text="Hasil Lexical Analysis:")
la_label.grid(row=2, column=0, padx=5, sticky=tk.W)
la_output = tk.Text(root, height=5, width=60)
la_output.grid(row=2, column=1, padx=5, sticky=tk.W)

# Membuat label untuk menampilkan hasil parser
parse_label = tk.Label(root, text="Hasil Parse:")
parse_label.grid(row=3, column=0, padx=5, sticky=tk.W) 
parse_output = tk.Text(root, height=5, width=60)
parse_output.grid(row=3, column=1, padx=5, sticky=tk.W)

root.mainloop()
