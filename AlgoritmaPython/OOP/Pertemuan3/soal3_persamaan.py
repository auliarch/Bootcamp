class Matematika:

    @classmethod
    def persamaan(cls, x):
        return round((2*x - 5) * (3*x - 1), 3)

    @staticmethod
    def persamaan2(x): # tidak menggunakan cls
        return round((2*x - 5) * (3*x - 1), 3)

print(Matematika.persamaan2(5))