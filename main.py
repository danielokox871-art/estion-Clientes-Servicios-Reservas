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
        self._id = id   # encapsulado

    def get_id(self):
        return self._id

# ================= CLIENTE =================
class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        super().__init__(id)

        # Validaciones
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido")

        self._nombre = nombre
        self._correo = correo

    # Encapsulación (getters)
    def get_nombre(self):
        return self._nombre

    def get_correo(self):
        return self._correo

    # Método extra 
    def mostrar_info(self):
        return f"Cliente: {self._nombre} | Correo: {self._correo}"
