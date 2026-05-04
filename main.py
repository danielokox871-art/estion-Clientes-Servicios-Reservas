from abc import ABC, abstractmethod

# ================= LOGS =================
def registrar_error(error):
    with open("logs.txt", "a") as f:
        f.write(str(error) + "\n")

# ================= CLASE BASE =================
class Entidad(ABC):
    def __init__(self, id):
        if id <= 0:
            raise ValueError("El ID debe ser mayor que 0")
        self._id = id

    def get_id(self):
        return self._id

# ================= CLIENTE =================
class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        super().__init__(id)

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido")

        self._nombre = nombre
        self._correo = correo

    def get_nombre(self):
        return self._nombre

    def get_correo(self):
        return self._correo

    def mostrar_info(self):
        return f"Cliente: {self._nombre} | Correo: {self._correo}"

# ================= PRUEBAS =================
def prueba_cliente():
    print("=== PRUEBAS CLIENTE ===")

    # Cliente válido
    try:
        c1 = Cliente(1, "Andres", "andres@gmail.com")
        print(c1.mostrar_info())
    except Exception as e:
        registrar_error(e)

    # Cliente válido
    try:
        c2 = Cliente(2, "Sofia", "sofia@gmail.com")
        print(c2.mostrar_info())
    except Exception as e:
        registrar_error(e)

    # Error: correo inválido
    try:
        c3 = Cliente(3, "Valentina", "correo_mal")
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    # Error: nombre vacío
    try:
        c4 = Cliente(4, "", "jose@gmail.com")
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    print("=== FIN PRUEBAS ===")


if __name__ == "__main__":
    prueba_cliente()
