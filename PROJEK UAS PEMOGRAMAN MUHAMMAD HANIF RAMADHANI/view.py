class View:
    def tampilkan(self, mahasiswa, grade):
        print("\n+----------------+----------------------+")
        print("| DATA NILAI MAHASISWA               |")
        print("+----------------+----------------------+")
        print(f"| Nama           | {mahasiswa.nama:<20} |")
        print(f"| NIM            | {mahasiswa.nim:<20} |")
        print(f"| Nilai          | {mahasiswa.nilai:<20} |")
        print(f"| Grade          | {grade:<20} |")
        print("+----------------+----------------------+")