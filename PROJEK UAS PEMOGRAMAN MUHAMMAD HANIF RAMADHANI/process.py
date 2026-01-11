class NilaiProcess:
    def hitung_grade(self, nilai):
        if nilai >= 85:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        else:
            return "D"