while True:
    try:
        edad=int(input("Ingrese su edad:"))
        print("Tu edad es: {}".format(edad))
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("La ejecucion ha finalizado")