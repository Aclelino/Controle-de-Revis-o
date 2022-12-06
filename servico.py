import time
import sqlite3

conn = sqlite3.connect("servico.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS oficina(id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,modelo TEXT NOT NULL,revisao TEXT NOT NULL,valor FLOAT NOT NULL,data TEXT NOT NULL)")

def inserir():
    
    modelo = [
        "Neo 125",
        "Fluo 125",
        "Nmax 160",
        "Xmax 250",
        "Factor 125",
        "Factor 150",
        "Fazer 150",
        "Crosser 150",
        "Fz 15",
        "Fz 25",
        "Lander 250",
        "Mt 03",
        "R3",
        "Mt 07",
        "Mt 09",
        "Trace gt",
        
        ]
        
    revisao = [
    "Lavagem",
    "Troca de Oleo",
    "Ajuste de Corrente",
    "Geral",
    "Serviço Eletrico",
    "Serviço Rapido",
    "Trocar de  Kit",
    "Troca de retentor",
    "Recall ECU Reprogramação",
    "Garantia Luz de Seta",
    "Garantia Sensor de Freio",
    "Garantia Painel",
    "Garantia retentor",
    "Garantia Bateria",
    "Garantia Retificador",
    "Garantia Estator",
    "Garantia caixa de Direção", 
    "1.000 km",
    "3.000 km",
    "5.000 km",
    "6.000 km",
    "9.00 km",
    "10.000 km",
    "15.000 km",
    "20.000 km",
    "25.000 km",
    "30.000 km",
    "35.000 km",
    "40.000 Km",
    '45.000 km',
    '100.000 km',
    ]
    
    print("\nSELECIONE UM MODELO 🛵")
    time.sleep(0.9)
    print("CARREGANDO ...")
    time.sleep(1.5)
    for i in modelo:
    
        print(f"[{modelo.index(i)}] {i}")

    moto = int(input("\nMODELO: "))
    for x in revisao:
        
        print(f"\n[{revisao.index(x)}] {x}",end=" ")
    km = int(input("\nREVISÃO: "))
    valor = float(input("\nPREÇO: "))
    
    dt = input("Data de Hoje?\n y/n")
    if dt == "y":
        dt=time.strftime("🕓 %X 📅 %x")
    elif dt == "n":
        dt = input("Informe a Hora e a Data: ")
    
    c.execute("INSERT INTO oficina(modelo,revisao,valor,data)VALUES(?,?,?,?)",(modelo[moto],revisao[km],valor,dt))
    conn.commit()
    print("💾")
    
def visualizar():
    
    d = c.execute("SELECT * FROM oficina")
    
    dt = input("Pesquisar por Data ex 01/01/22\n📅 =")
    for i in d : 
        a = dt in i[4]
        
        if a == True:
            print(f"🆔️ [{i[0]}]\n🛵 {i[1]}\n🛠 {i[2]}\n💰 R${i[3]}\n📅 {i[4]}\n")
         
def editar():
    
    visualizar()
    id = input("id: ")
  
    moto = input("Gostaria  de alterar  o modelo? y/n\n")
    if moto == "y":
        moto = input("Novo Modelo: ")
        c.execute("UPDATE oficina SET modelo = ? WHERE id =?",(moto,id))
    
    rev = input("Gostaria  de alterar a revisão? y/n\n")    
    if rev =="y":    
        rev = input("Novo Revisão: ")
        c.execute("UPDATE oficina SET revisao = ? WHERE id = ?",(rev,id))
   
    val = input("Gostaria de alterar o valor?y/n\n")
    if val =="y":
        val = ("Novo valor: ")
        
        c.execute("UPDATE oficina SET valor = ? WHERE id = ?",(val,id))
    
    dat =input("Gostaria  de alterar a data?y/n\n")
    if dat =="y":
        dat = input("Nova Data: ") 
        c.execute ("UPDATE oficina set data = ? WHERE id = ?",(dat,id)) 
    conn.commit()
    print("atualizado")
    
    
def deletar():
    visualizar()
    id = input("Id desejado")
    c.execute("DELETE FROM oficina WHERE id = {}".format(id))
    
    
    
    if input("Certeza que deseja deletar?y/n") =="y":
        conn.commit()
        print("❌ Excluido com Sucesso !")
def total():
    
    dados = c.execute("SELECT * FROM oficina")
    log = []
    free = []
    grt = []
    menu = input("\nInforme a Data Ex 01/01/22 ")
    
    for i in dados:
        
        dt = menu in i[4]
        if dt ==True:
   
            b = "Garantia" in i[2]
            
            if b ==True:
                grt.append(i[2])
                
            
            if i[2] == "1.000 km":
                
                free.append(i[3])
            elif i[2] == "3.000 km":
                
                free.append(i[3])
            elif i[2] =="5.000 km":
                
                free.append(i[3])
                
            log.append(i[3])
        else:
            print("Não existe registro nessa Data")
            
    print("Total de Garantia",len(grt))
    print("Mão de obra Gratuita R${:.2f}".format(sum(free)))
    print("Mão de obra Paga R${:.2f}".format(sum(log)-sum(free)))    	
    print("Total de Revisão R$:{:.2f}".format(sum(log)))
         
        


while True:
    
    
    menu =input("\n➕ Add Revisão.1"
	"\n🔄 Atualizar.2\n"
	"🔍 Visualizar.3\n"
	"❌ Excluir.4\n"
	"📉 Total.5\n"
	"🚪\n->: "
	)

    if menu =="1":
        inserir()
        
    elif menu =="2":
        editar()
    elif menu =="3":
        visualizar()
        
    elif menu =="4":
        deletar()
    elif menu =="5":
        total()
    else:
        print("Até logo 👋")
        exit()
    
    
    
    
    




