class Matematika:

    @classmethod
    def persamaan(cls, n):
        return round((n + 1/n) ** 2, 1)
        # return "{:.1f}".format((n + 1/n) ** 2)

print(Matematika.persamaan(5.0))