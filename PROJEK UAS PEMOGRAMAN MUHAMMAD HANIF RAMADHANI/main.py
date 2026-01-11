from data import Mahasiswa
from process import NilaiProcess
from view import View

try:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    nilai = float(input("Masukkan Nilai: "))

    mahasiswa = Mahasiswa(nama, nim, nilai)
    proses = NilaiProcess()
    view = View()

    grade = proses.hitung_grade(nilai)
    view.tampilkan(mahasiswa, grade)

except ValueError:
    print("Nilai harus berupa angka!")