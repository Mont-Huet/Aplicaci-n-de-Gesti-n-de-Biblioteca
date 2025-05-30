class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_info(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}'
    
class Revista(Libro):
    def __init__(self, titulo, autor, isbn, numero_edicion):
        super().__init__(titulo, autor, isbn)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Edición: {self.numero_edicion}'
    
class Usuario:
    def __init__(self, nombre, tipo_usuario):
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    def prestar(self, libro):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def devolver(self, libro):
        return f'{self.nombre} ha devuelto el libro: {libro.titulo}'

class Estudiante(Usuario):
    def prestar(self, libro):
        return f'El estudiante {self.nombre} ha solicitado prestar el libro: {libro.titulo}'

class Profesor(Usuario):
    def prestar(self, libro):
        return f'El profesor {self.nombre} ha solicitado prestar el libro: {libro.titulo} con prioridad.'
    
# Creación de instancias
libro1 = Libro("1984", "George Orwell", "123456789")
revista1 = Revista("National Geographic", "Varios", "987654321", 5)

estudiante = Estudiante("Juan", "Estudiante")
profesor = Profesor("Ana", "Profesor")

# Mostrar información
print(libro1.mostrar_info())
print(revista1.mostrar_info())

# Préstamos
print(estudiante.prestar(libro1))
print(profesor.prestar(revista1))