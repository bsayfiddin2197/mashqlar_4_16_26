# 1

class Kitob:
    def __init__(self, nomi, mualif, sahif_nomi):
        self.nomi = nomi
        self.mualif = mualif
        self.sahif_nomi = sahif_nomi

    def info(self):
        print(f"nomi: {self.nomi}")
        print(f"mualif: {self.mualif}")
        print(f"sahif_nomi: {self.sahif_nomi}")
s1 = Kitob(f"otgan kunlar", "A.Qodriy", 300)
s1.info()

# 2

class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs
    def info(self):
        print(f"ism: {self.ism}")
        print(f"yosh: {self.yosh}")
        print(f"kurs: {self.kurs}")

k2 = Talaba("Ali", 20, 2)
k2_2 = Talaba("Vali", 22, 3)
k2.info()
print("$" * 8)
k2_2.info()

# 3

class Telefon:
    def __init__(self, model, rang, narx):
        self.model = model
        self.rang = rang
        self.narx = narx
    def info(self):
        print(f"model: {self.model}")
        print(f"rang: {self.rang}")
        print(f"narx: {self.narx}")

k3 = Telefon("Iphone 13", "qora", 700)
k3_2 = Telefon("Samsung S21", "0q", 900)
k3.info()
k3_2.info()
