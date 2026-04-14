# --- Program Analisis Tabungan Sederhana ---

# Input data secara interaktif
nama = "Woro"
pemasukan = 5000000
pengeluaran = 2000000

# Perhitungan
tabungan = pemasukan - pengeluaran
rasio_tabungan = (tabungan / pemasukan) * 100

# Menampilkan hasil analisis dengan format yang rapi
print(f"--- Laporan Keuangan {nama} ---")
print(f"Total Pemasukan   : Rp{pemasukan:,}")
print(f"Total Pengeluaran : Rp{pengeluaran:,}")
print(f"Sisa Tabungan     : Rp{tabungan:,}")
print(f"Persentase Hemat  : {rasio_tabungan:.1f}%")

# Logika sederhana
if rasio_tabungan >= 30:
    print("Status: Keuangan Sehat! (Tabungan di atas 30%)")
else:
    print("Status: Perlu evaluasi pengeluaran.")
    