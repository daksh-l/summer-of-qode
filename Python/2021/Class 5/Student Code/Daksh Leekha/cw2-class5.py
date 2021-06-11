var = "test"

print(var)


def changeVar():
    global var

    var = "not a test now"


changeVar()

print(var)
