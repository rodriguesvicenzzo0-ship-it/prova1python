soma_notas = 0
for i in range(1, 4):
    notas = float(input(f"digite a nota do {i}º bismestre:"))
    soma_notas += notas
    media = soma_notas / 3
    print(f"a media final é {media: .2f}")
