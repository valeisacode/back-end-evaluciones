from getpass import getpass
from pathlib import Path

import mysql.connector
from mysql.connector import Error


BASE_DIR = Path(__file__).resolve().parent
SQL_FILE = BASE_DIR / "sql" / "01_configuracion.sql"


def main():
    if not SQL_FILE.is_file():
        print(f"No se encontró el archivo: {SQL_FILE}")
        return

    print("Preparación de la base de datos en XAMPP")
    print("MySQL/MariaDB debe estar iniciado.")
    print("Se ejecutará sql/01_configuracion.sql.")
    print("Esto también establecerá la contraseña del usuario de la app.")

    host = input("Servidor [127.0.0.1]: ").strip() or "127.0.0.1"
    port_text = input("Puerto [3306]: ").strip() or "3306"
    user = input("Usuario administrador [root]: ").strip() or "root"
    password = getpass(
        "Contraseña del administrador (Enter si no tiene): "
    )

    try:
        port = int(port_text)
    except ValueError:
        print("El puerto debe ser un número.")
        return

    confirmation = input(
        "¿Ejecutar el script y configurar la cuenta? Escribe SI: "
    ).strip()

    if confirmation.upper() != "SI":
        print("Operación cancelada.")
        return

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            connection_timeout=10,
            autocommit=True,
        )
        cursor = connection.cursor()

        sql = SQL_FILE.read_text(encoding="utf-8-sig")

        # Separador válido para este archivo simple, sin procedimientos.
        statements = [
            statement.strip()
            for statement in sql.split(";")
            if statement.strip()
        ]

        for number, statement in enumerate(statements, start=1):
            print(f"Ejecutando instrucción {number}...")
            cursor.execute(statement)

        cursor.execute(
            "SHOW DATABASES LIKE 'control_tareas'"
        )

        if cursor.fetchone():
            print("\nBase de datos control_tareas disponible.")
            print("Usuario y permisos configurados.")
            print("Ahora ejecuta las migraciones de Django.")

    except Error as error:
        print("\nNo se pudo completar la configuración.")
        print(f"Código de error: {error.errno}")
        print(f"Detalle: {error.msg}")
        print("Si falló a mitad del proceso, algunas instrucciones")
        print("anteriores podrían haberse aplicado.")

    except (OSError, UnicodeError) as error:
        print(f"No se pudo leer el archivo SQL: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()