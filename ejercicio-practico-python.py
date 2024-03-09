#EJERCICIO PRACTICO – PYTHON SENTENCIAS CONDICIONALES Y OPERADORES
while True:
    nombre_trabajor = input("Ingrese el nombre del trabajador: ").upper()
    
    while not nombre_trabajor.isalpha():
         print("El nombre solo debe contener letras. Por favor, intente de nuevo.")
         nombre_trabajor = input("Ingrese el nombre del trabajador: ").upper()

    contraseña = input("Ingrese la contraseña de acuerdo al departamento que pertenece \n \t CE - Control Escolar \n \t IPF - Infraestructura y Planta Física \n \t RHC - Recursos Humanos y Capacitación \n \t ").upper()
        
    if contraseña == "CE":
        servicios = int(input(f"Ingrese la cantidad años con el servicio de {contraseña}: "))
        if servicios == 1:
            dias_vacacaciones = "10 días de vacaciones"
        elif servicios >= 2 and servicios <= 6:
            dias_vacacaciones = "15 días de vacaciones"
        elif servicios >= 7:
            dias_vacacaciones = "20 días de vacaciones"

    elif contraseña == "IPF":
        servicios = int(input(f"Ingrese la cantidad años con el servicio de {contraseña}: "))
        if servicios == 1:
            dias_vacacaciones = "12 días de vacaciones"
        elif servicios >= 2 and servicios <= 6:
            dias_vacacaciones = "15 días de vacaciones"
        elif servicios >= 7:
            dias_vacacaciones = "22 días de vacaciones"

    elif contraseña == "RHC":
        servicios = int(input(f"Ingrese la cantidad años con el servicio de {contraseña}: "))
        if servicios == 1:
            dias_vacacaciones = "15 días de vacaciones"
        elif servicios >= 2 and servicios <= 6:
            dias_vacacaciones = "20 días de vacaciones"
        elif servicios >= 7:
            dias_vacacaciones = "30 días de vacaciones"

    else:
        dias_vacaciones = "Contraseña inválida"

    print(f"El trabajador {nombre_trabajor} tiene derecho a {dias_vacacaciones}")

    opcion_continuar = input("¿Desea continuar? (S/N): ").upper()
    if opcion_continuar != "S":
        break
