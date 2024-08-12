from django.db import models

#Manager personalizado para obtener los libros que no han sido devueltos.
class UnreturnedBooksManager(models.Manager):
    def not_returned(self):
        #Filtra los libros que no han sido devueltos y elimina duplicados.
        return self.filter(loan__returned = False).distinct()
# Modelo que representa un Autor
class Author(models.Model):
    full_name = models.CharField(max_length=140)  # Nombre completo del autor

    def __str__(self):
        #Representación en cadena del autor (útil para el admin y shell).
        return self.full_name

# Modelo que representa un Libro.
class Book(models.Model):
    ibm = models.IntegerField(primary_key=True)  # Identificador único del libro
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Relación con el autor
    name_book = models.CharField(max_length=140)  # Nombre del libro
    publish_date = models.DateField()  # Fecha de publicación del libro

    # Manager personalizado para libros no devueltos.
    unreturned_books = UnreturnedBooksManager()

    #Manager por defecto.
    objects = models.Manager()

    #Clase meta para modificarle el nombrado,etc de la clase Book.
    class Meta:
        db_table = 'book'  #Nombre de la tabla en la base de datos.
        ordering = ['-publish_date']  #Orden predeterminado por fecha de publicación descendente.
        verbose_name = 'book'  #Nombre singular del modelo.
        verbose_name_plural = 'books'  #Nombre plural del modelo.

    def __str__(self):
        #Representación en cadena del libro.
        return self.name_book
    
# Modelo que representa un Miembro de la biblioteca
class Member(models.Model):
    full_name = models.CharField(max_length=140)  # Nombre completo del miembro
    email = models.EmailField(unique=True)  # Correo electrónico único del miembro
    joined_date = models.DateField()  # Fecha en que el miembro se unió

    def __str__(self):
        # Representación en cadena del miembro
        return self.full_name

# Modelo que representa un Préstamo de libro
class Loan(models.Model):
    member_with_loan = models.ForeignKey(Member, on_delete=models.CASCADE)  #Relación con el miembro que tomó el préstamo.
    book_in_loan = models.ForeignKey(Book, on_delete=models.CASCADE)  #Relación con el libro prestado.
    loan_date = models.DateField()  #Fecha del préstamo.
    returned = models.BooleanField(default=False)  #Indicador de si el libro fue devuelto.
    returned_date = models.DateField(blank=True, null=True)  #Fecha de devolución del libro (si aplica).

    def __str__(self):
        #Representación en cadena del préstamo.
        return f'{self.book_in_loan.name_book} loaned to {self.member_with_loan.full_name}'

