
def servico(x,y):
    somar = x*y/100
    print("💰 Valor da comisão R$:{:.2f}".format(somar))

mdo = int(input("\033[0;1;32mMão de obra: \033[1;00mR$"))
porc = int(input("Porcentagem: "))
servico(mdo,porc)