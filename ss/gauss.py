import numpy as np

# Matriks koefisien kendala
A = np.array([[2, 3, 1],
              [3, 1, 2],
              [1, 1, 1]])

# Vektor koefisien fungsi tujuan
c = np.array([-100, -150, 0])

# Vektor batas kendala
b = np.array([600, 800, 400])

# Batasan non-negativitas
bounds = [(0, None), (0, None), (0, None)]

# Menyelesaikan masalah optimasi linear
res = np.linalg.solve(A, -c)

# Menampilkan hasil optimal
print('Jumlah unit barang A yang harus diproduksi: ', round(res[0]))
print('Jumlah unit barang B yang harus diproduksi: ', round(res[1]))
print('Jumlah karyawan yang harus digunakan: ', round(res[2]))
print('Laba maksimum yang dapat diperoleh: $', round(np.dot(c, res)))