class conta():
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
def main():
    obj = conta(46879123,"005.462.352-98","Carlos Dambleerley Silva de Sousa",500.00)
    print(f"Numero da conta {obj.numero}")
    print(f"CPF {obj.cpf}")
    print(f"Nome do titular {obj.nomeTitular}")
    print(f"Saldo da conta {obj.saldo}")
    
if __name__ == "__main__":
    main()