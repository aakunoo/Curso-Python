def validarUsuarios(usuario):
    error1 = "El usuario no puede tener menos de 5 caracteres"
    error2 = "El usuario no puede tener mas de 15 caracteres"
    error3 = "El usuario solo puede contener letras y números"

    while True:

        if not usuario:
            print("\nEl usuario no puede estar vacio. ")
            continue

        elif len(usuario) < 5:
            return error1

        elif len(usuario) > 15:
            return error2

        elif not usuario.isalnum():
            return error3

        elif len(usuario) >= 5 and len(usuario) <= 15 and usuario.isalnum():
            return True


def validarContra(contra):

    mayuscula = False
    minuscula = False

    while True:

        if len(contra) < 10:
            return "La contraseña debe tener más de 10 caracteres"

        elif contra.isalnum():
            return "La contraseña debe contener un carácter que no sea ni letra ni número"

        for i in contra:
            if i.isupper():
                mayuscula = True
            elif i.islower():
                minuscula = True

        if mayuscula == False or minuscula == False:
            return "La contraseña no es segura"

        for j in contra:
            if (j == " "):
                return "La contraseña no puede contener espacios en blanco"

        else:
            return True
