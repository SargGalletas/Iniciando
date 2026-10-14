name = "SargGalletas"
user = "choclo123"
password = "elpepe34"
print("Bienvenido a tu código python")

user_input = input("Ingresa tu usuario para continuar: ")
if user_input == user:
    print(f"Bienvenido de nuevo, {name}")
    password_input = input("Ingresa tu contraseña para continuar: ")
    if password_input == password:
        print("Contraseña correcta, sesión iniciada")
        
        select_option = input("¿Cómo puedo ayudarte, Carlos? ")
        print(f"Perfecto, trabajaremos con: {select_option}")
        if select_option == "cambiar contraseña":
            new_password = input("Ingresa nueva contraseña: ")
            print("Tu contraseña fue cambiada exitosamente")
        elif select_option == "cambiar usuario":
            new_user = input("Ingresa nuevo usuario: ")
            print("Tu usuario fue cambiado exitosamente")
        elif select_option == "destruir el planeta":
            destroy = input("¿Estás seguro de realizar esta acción? ")
            if destroy == "si":
                print("Iniciando destrucción masiva")
            else:
                print("La destrucción no fue efectuada")
        elif select_option == "ayudame con mi tarea":
            help_task = input("¿En qué curso puedo ayudarte? ")
            if help_task == "analisis intelectual del papoi":
                print(f"Estoy trabajando en ayudarte con {help_task}")
                print("En conclusión, los papois no son intelectuales")
            elif help_task == "bases farmacologicas":
                print("Aún no veo ese curso, estoy en nada igual que tu :p")
            elif help_task == "olvidalo":
                print("ok :c")
        elif select_option == "Cerrar sesión":
            print("Cerrando sesión")
        elif select_option 
            
        
    else:
        print("Contraseña incorrecta, usted deberá iniciar sesión nuevamente")
else:
    print("El usuario no existe")