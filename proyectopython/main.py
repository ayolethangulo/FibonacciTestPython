def sumar_posicion(posicion):
    if posicion > 0 :
        if posicion == 1:
            return 0
        elif posicion == 2:
            return 1
        else:
            a = 0
            b = 1
            c =0
            for i in range(1, posicion):
                a=b
                b=c
                c=a+b
            return c
    else:
        return -1