import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HotelSejukAsri:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Sejuk Asri - Pembayaran")
        self.root.minsize(300, 300)
        self.root.configure(bg="lightsteelblue")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Hotel Sejuk Asri", justify=tk.LEFT, font=("Consolas", 20, "bold"), bg="lightsteelblue", fg="midnightblue").grid(row=1, column=0, columnspan=2, pady=5)

        self.create_input_fields()

        tk.Button(self.root, text="Hitung Pembayaran", command=self.hitung_pembayaran, fg="midnightblue", bg="aliceblue").grid(row=9, column=1, pady=10)

        self.label_pembayaran = tk.Label(self.root, text="Hasil Pembayaran", justify=tk.LEFT, font=("Consolas", 20, "bold"), bg="lightsteelblue", fg="midnightblue")
        self.label_pembayaran.grid(row=11, column=0, columnspan=3, pady=10)
        self.label_pembayaran.grid_remove()

        self.label_hasil = tk.Label(self.root, text="", justify=tk.LEFT, font=("Consolas", 10, "bold"), bg="lightsteelblue", fg="midnightblue")
        self.label_hasil.grid(row=12, column=0, columnspan=3, pady=10)

    def create_input_fields(self):
        labels = ["Nama Petugas", "Nama Customer", "Tanggal Check in (HH-BB-TTTT)", "Kode Kamar (M/S/L/A)", "Lama Sewa (hari)", "Uang Bayar"]
        self.fields = {}
        
        for i, label in enumerate(labels):
            tk.Label(self.root, text=label, font=("Consolas", 10, "bold"), bg="lightsteelblue", fg="midnightblue").grid(row=i+3, column=0, padx=10, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=i+3, column=1, padx=10, pady=5)
            self.fields[label] = entry

        self.label_nama_kamar = tk.Label(self.root, text="", bg="lightsteelblue")
        self.label_nama_kamar.grid(row=6, column=2, padx=10, pady=5)

    def hitung_pembayaran(self):
        try:
            nama_petugas = self.fields["Nama Petugas"].get()
            nama_customer = self.fields["Nama Customer"].get()
            tanggal_checkin = self.fields["Tanggal Check in (HH-BB-TTTT)"].get()
            kode_kamar = self.fields["Kode Kamar (M/S/L/A)"].get().upper()
            lama_sewa = int(self.fields["Lama Sewa (hari)"].get())
            uang_bayar = int(self.fields["Uang Bayar"].get())

            datetime.strptime(tanggal_checkin, '%d-%m-%Y')

            data_kamar = {
                'M': ("Melati", 650000),
                'S': ("Sakura", 550000),
                'L': ("Lily", 400000),
                'A': ("Anggrek", 350000),
            }

            if kode_kamar not in data_kamar:
                raise ValueError("Kode Kamar tidak tersedia")

            nama_kamar, harga_sewa = data_kamar[kode_kamar]

            jumlah_bayar = harga_sewa * lama_sewa

            if lama_sewa > 5:
                diskon = 0.10
            elif lama_sewa > 3:
                diskon = 0.05
            else:
                diskon = 0.0

            ppn = diskon * jumlah_bayar
            total_bayar = jumlah_bayar - ppn
            uang_kembali = uang_bayar - total_bayar

            if uang_kembali < 0:
                raise ValueError("Uang yang dibayarkan tidak cukup untuk membayar total biaya")

            teks_hasil = (f"Nama Petugas : {nama_petugas}\n"
                          f"Nama Customer : {nama_customer}\n"
                          f"Tanggal Check-in : {tanggal_checkin}\n"
                          f"Nama Kamar : {nama_kamar}\n"
                          f"Harga Sewa per Malam : Rp. {harga_sewa:,.2f}\n"
                          f"Lama Sewa : {lama_sewa} hari\n"
                          f"Jumlah Bayar : Rp. {jumlah_bayar:,.2f}\n"
                          f"Diskon : {diskon * 100}%\n"
                          f"PPN : Rp. {ppn:,.2f}\n"
                          f"Total Bayar : Rp. {total_bayar:,.2f}\n"
                          f"Uang Bayar : Rp. {uang_bayar:,.2f}\n"
                          f"Uang Kembali : Rp. {uang_kembali:,.2f}")
            self.label_hasil.config(text=teks_hasil)

            self.label_pembayaran.grid()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_input(self):
        for entry in self.fields.values():
            entry.delete(0, tk.END)
        self.label_hasil.config(text="")
        self.label_pembayaran.grid_remove()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelSejukAsri(root)

    tk.Button(root, text="Hapus", command=app.clear_input, fg="midnightblue", bg="aliceblue").grid(row=9, column=0, pady=10)

    root.mainloop()