import comandos

while(True):
    print("""
=================================================================================
                                TRABALHO FINAL
=================================================================================
1- CREATE
2- READ(ALL)
3- READ(ID)
4- UPDATE
5- DELETE
6- EXIT
""")

    comando = int(input(">: "))
    if comando == 1:
        comandos.CREATE()
    if comando == 2:
        comandos.READ_ALL()
    if comando == 3:
        comandos.READ_ID()
    if comando == 4:
        comandos.UPDATE()
    if comando == 5:
        comandos.DELETE()
    if comando == 6:
        break
