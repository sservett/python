for i in range(1, int(input())):
    print(((10 ** i) // 9) * i)


def servet(ali):
    def arzu():
        print("Ben Arzu")
        ali()

    return arzu


@servet
def ince():
    print("INCEEE")


ince()
