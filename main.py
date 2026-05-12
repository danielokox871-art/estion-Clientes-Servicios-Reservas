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


# ================= SERVICIO =================
class Servicio(Entidad, ABC):

    def __init__(self, id, nombre, precio_base):
        super().__init__(id)

        if not nombre.strip():
            raise ValueError("Nombre inválido")

        if precio_base <= 0:
            raise ValueError("Precio inválido")

        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

# ================= SALA =================
class Sala(Servicio):

    def __init__(self, id, nombre, precio_base, horas):
        super().__init__(id, nombre, precio_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayor que 0")

        if horas > 8:
            raise ValueError("La sala no puede reservarse por más de 8 horas")

        self._horas = horas

    def calcular_costo(self):
        return self._precio_base * self._horas

    def mostrar_info(self):
        return (
            f"Sala: {self._nombre} | "
            f"Horas: {self._horas} | "
            f"Total: ${self.calcular_costo():,.0f}"
        )

# ================= EQUIPO =================
class Equipo(Servicio):

    def __init__(self, id, nombre, precio_base, cantidad):
        super().__init__(id, nombre, precio_base)

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        self._cantidad = cantidad

    def calcular_costo(self):
        return self._precio_base * self._cantidad

    def mostrar_info(self):
        return (
            f"Equipo: {self._nombre} | "
            f"Cantidad: {self._cantidad} | "
            f"Total: ${self.calcular_costo():,.0f}"
        )


# ================= ASESORIA =================
class Asesoria(Servicio):

    def __init__(self, id, nombre, precio_base, horas):
        super().__init__(id, nombre, precio_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayor que 0")

        if horas > 4:
            raise ValueError("La asesoría no puede durar más de 4 horas")

        self._horas = horas

    def calcular_costo(self):
        return self._precio_base * self._horas * 1.5

    def mostrar_info(self):
        return (
            f"Asesoría: {self._nombre} | "
            f"Horas: {self._horas} | "
            f"Total: ${self.calcular_costo():,.0f}"
        )


# ================= RESERVA =================
class Reserva:

    def __init__(self, cliente, servicio):

        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ValueError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_info(self):
        return (
            f"{self.cliente.mostrar_info()} | "
            f"{self.servicio.mostrar_info()} | "
            f"Estado: {self.estado}"
        )

# ================= PRUEBAS CLIENTE =================
def prueba_cliente():

    print("=== PRUEBAS CLIENTE ===")

    try:
        c1 = Cliente(1, "Andres", "andres@gmail.com")
        print(c1.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        c2 = Cliente(2, "Sofia", "sofia@gmail.com")
        print(c2.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    # Correo inválido
    try:
        c3 = Cliente(3, "Valentina", "correo_mal")
        print(c3.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    # Nombre vacío
    try:
        c4 = Cliente(4, "", "jose@gmail.com")
        print(c4.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    print("=== FIN PRUEBAS CLIENTE ===\n")


# ================= PRUEBAS SERVICIOS =================
def prueba_servicios():

    print("=== PRUEBAS SERVICIOS ===")

    try:
        s = Sala(1, "Sala VIP", 100, 2)
        print(s.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        s2 = Sala(2, "Sala Error", 100, -1)
        print(s2.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        e = Equipo(3, "Proyector", 50, 3)
        print(e.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        e2 = Equipo(4, "Equipo Error", 50, 0)
        print(e2.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        a = Asesoria(5, "Consultoria", 80, 2)
        print(a.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        a2 = Asesoria(6, "Asesoria Error", 80, 10)
        print(a2.mostrar_info())
    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    print("=== FIN PRUEBAS SERVICIOS ===\n")


# ================= PRUEBAS RESERVAS =================
def prueba_reservas():

    print("=== PRUEBAS RESERVAS ===")

    try:
        cliente1 = Cliente(10, "Sebastian", "sebastian@correo.com")
        servicio1 = Sala(11, "Sala Ejecutiva", 120, 2)

        reserva1 = Reserva(cliente1, servicio1)
        reserva1.confirmar()

        print(reserva1.mostrar_info())

    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        cliente2 = Cliente(-1, "Error", "error@correo.com")
        servicio2 = Equipo(12, "Laptop", 60, 1)

        reserva2 = Reserva(cliente2, servicio2)

        print(reserva2.mostrar_info())

    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    try:
        cliente3 = Cliente(13, "Maria", "maria@correo.com")
        servicio3 = Asesoria(14, "Asesoria Premium", 100, 3)

        reserva3 = Reserva(cliente3, servicio3)
        reserva3.cancelar()

        print(reserva3.mostrar_info())

    except Exception as e:
        print("Error capturado:", e)
        registrar_error(e)

    print("=== FIN PRUEBAS RESERVAS ===")

# ================= EJECUCIÓN =================
if __name__ == "__main__":

    prueba_cliente()
    prueba_servicios()
    prueba_reservas()
