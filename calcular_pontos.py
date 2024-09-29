def calcular_pontos(valor_compra, na_rede_x, usou_cartao_x):
    valor_compra_int = int(valor_compra)

    if na_rede_x and usou_cartao_x:
        pontos = valor_compra_int * 3

    elif na_rede_x:
        pontos = valor_compra_int * 1.5
    
    elif usou_cartao_x:
        pontos = valor_compra_int
    
    else:  
        pontos = 0

    return int(pontos)
