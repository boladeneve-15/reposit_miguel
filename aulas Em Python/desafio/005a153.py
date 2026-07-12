print("carregando arquivo")
for i in range(5):
    print("preparando arquivo ({}Mb/4Mb)".format(i))
    for j in range(101):
        print("carregando arquivos ({}Kb/100Kb) arquivos preparados ({}Mb/4Mb)".format(j,i))
        for k in range(1001):
                print("carregando dados ({}B/1000B) carregado arquivos ({}/100Kb) terminando arquivos ({}Mb/4Mb)".format(k,j,i))