class volumeCubo:
    def __init__(self):
        
       aresta = float(input("Entre com um valor para a aresta do cubo: "))
       a = aresta**3
       print(f"O volume do cubo é {a} m3")
       
volume = volumeCubo()