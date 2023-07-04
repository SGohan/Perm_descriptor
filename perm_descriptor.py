import os
import pwd
import grp
from termcolor import colored

def get_current_user():
    return os.getlogin()

def analyze_permissions(permissions):

    permissions = permissions.strip()
    parts = permissions.split()

    #Extracción info
    if len(parts) < 3:
        print(colored("Error: Formato de permisos no válido.", "red"))
        return

    file_type = parts[0][0]
    user_perms = parts[0][1:4]
    group_perms = parts[0][4:7]
    other_perms = parts[0][7:10]
    num_links = parts[1]
    owner_name = parts[2]
    group_name = parts[3]

    #Verificación permisos ejecución
    user_executable = 'x' in user_perms
    group_executable = 'x' in group_perms
    other_executable = 'x' in other_perms

    #Verificación permisos user actual
    current_user = get_current_user()
    is_owner = current_user == owner_name
    can_read = 'r' in user_perms or 'r' in group_perms or 'r' in other_perms
    can_write = 'w' in user_perms or 'w' in group_perms or 'w' in other_perms
    can_execute = user_executable or group_executable or other_executable

    #Impresión y colores a resultados
    print(colored("=== Resultados ===", "cyan"))
    print(f"{colored('Usuario actual:', 'yellow')} {current_user}")
    print(f"{colored('Tipo de archivo:', 'yellow')} {'Directorio' if file_type == 'd' else 'Archivo'}")
    print(f"{colored('Propietario:', 'yellow')} {owner_name}")
    print(f"{colored('Grupo:', 'yellow')} {group_name}")
    print(f"{colored('Permisos de usuario:', 'yellow')} {'Lectura' if 'r' in user_perms else 'No lectura'}, {'Escritura' if 'w' in user_perms else 'No escritura'}")
    print(f"{colored('Permisos de grupo:', 'yellow')} {'Lectura' if 'r' in group_perms else 'No lectura'}, {'Escritura' if 'w' in group_perms else 'No escritura'}")
    print(f"{colored('Permisos de otros:', 'yellow')} {'Lectura' if 'r' in other_perms else 'No lectura'}, {'Escritura' if 'w' in other_perms else 'No escritura'}")
    print(f"{colored('Número de enlaces:', 'yellow')} {num_links}")
    print(f"{colored('Permiso de ejecución para usuario:', 'yellow')} {'Sí' if user_executable else 'No'}")
    print(f"{colored('Permiso de ejecución para grupo:', 'yellow')} {'Sí' if group_executable else 'No'}")
    print(f"{colored('Permiso de ejecución para otros:', 'yellow')} {'Sí' if other_executable else 'No'}")
    print(f"{colored('¿Es propietario?', 'yellow')} {'Sí' if is_owner else 'No'}")
    print(f"{colored('¿Tiene permiso de lectura?', 'yellow')} {'Sí' if can_read else 'No'}")
    print(f"{colored('¿Tiene permiso de escritura?', 'yellow')} {'Sí' if can_write else 'No'}")
    print(f"{colored('¿Tiene permiso de ejecución?', 'yellow')} {'Sí' if can_execute else 'No'}")

def main():
    print(colored("======== Permissions descriptor =======", "green"))
    print(colored("=======================================", "green"))
    print()
    permissions = input("Ingrese los permisos en formato de texto: ")

    #Analisis permisos
    analyze_permissions(permissions)

if __name__ == "__main__":
    main()
