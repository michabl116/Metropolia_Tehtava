def gallona_mutos(gallona):
    return gallona * 3.785

while True:
    gallona = float(input("Anna bensiinin määra "))
    if gallona < 0:
        break
    litra = gallona_mutos(gallona)
    print(f"{gallona} gallonaa on {litra:.2f} litraa.")