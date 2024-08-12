#CONSULTAS EJERICIO
from todos.models import Author, Book, Member, Loan
from datetime import date
#Consultas Básicas.
# Consultar todos los autores.
authors = Author.objects.all()
for author in authors:
    print(author.full_name)

# Consultar todos los libros de la biblioteca.
books = Book.objects.all()
for book in books:
    print(f'{book.name_book} escrito por {book.author.full_name}, publicado en {book.publish_date} con el ISBN:{book.ibm}')

# Consultar todos los miembros de la biblioteca.
members = Member.objects.all()
for member in members:
    print(f'{member.full_name}, email:{member.email}, con fecha de unión:{member.joined_date}')

# Consultar todos los préstamos de libros de la biblioteca.
loans = Loan.objects.all()
for loan in loans:
    print(f"Book: {loan.book_in_loan.name_book}, Member: {loan.member_with_loan.full_name}, Returned: {loan.returned}")

#Limpiar un campo de la base de datos.
Member.objects.all().delete()

#Crear nuevos registros de nuevo. ponemos id para porque sino incrementaria el id automáticamente.
member1 = Member.objects.create(id=1, full_name='Tomás Labrador Benito', email='tomaslabrador@gmail.com', joined_date=date(2023, 5, 24))
member2 = Member.objects.create(id=2, full_name='Marta González Sierra', email='marta.gonzalez@gmail.com', joined_date=date(2024, 6, 9))
member3 = Member.objects.create(id=3, full_name='Aurelio Martin Fraile', email='aurelio.martin@gmail.com', joined_date=date(2023, 12, 2))

#Consultas Avanzadas
# Consultar los libros del autor 'Daniel Labrador Benito'
books_by_Daniel = Book.objects.filter(author__full_name='Daniel Labrador Benito')
for book in books_by_Daniel:
    print(f'{book.name_book} escrito por {book.author.full_name}, publicado en {book.publish_date} con el ISBN:{book.ibm}')

#Obtener todos los miembros que se unieron después de '2023-01-15'
members_filter_date = Member.objects.filter(joined_date__gt= '2023-01-15')
for member_filter_date in members_filter_date:
    print(f'{member_filter_date.full_name}, email: {member_filter_date.email}, fecha de unión: {member_filter_date.joined_date}')

#Obtener todos los préstamos que no han sido devueltos
loans_not_returned = Loan.objects.filter(returned = False)
for loan_not_returned in loans_not_returned:
    print(f'El préstamo del libro{loan_not_returned.book_in_loan} no ha sido devuelto aún.')

#AGREGACIONES Y ANOTACIONES.
# Obtener el total de libros
total_books = Book.objects.aggregate(total_books=Count('pk'))
#pongo la pk ya que id es una keyword.
print(f'Total de libros: {total_books["total_books"]}')

# Obtener el libro más reciente por fecha de publicación.
latest_book = Book.objects.aggregate(latest=Max('publish_date'))
print(f'Último libro publicado: {latest_book["latest"]}')

# Contar el número de libros para cada autor
authors_with_book_count = Author.objects.annotate(num_books=Count('book'))
for author in authors_with_book_count:
    print(f'{author.full_name} tiene {author.num_books} libros')

# Calcular el promedio del año de publicación
average_year = Book.objects.annotate(
    publish_year=F('publish_date__year')).aggregate(
    avg_year=Avg('publish_year'))
print(f'Promedio del año de publicación: {average_year["avg_year"]}')

#Consulta de optimización son 'select_related'.
#Obtenemos todos los libros y sus autores con su fechas asociados en una sola consulta.
libros = Book.objects.select_related('author').all()
for libro in libros:
    print(f'{libro.name_book} escrito por {libro.author.full_name}, publicado en {libro.publish_date}')

#Prueba de errores y excepciones.
try:
    libro_inexistente = Book.objects.get(ibm=9999)  # Cambia '9999' por un ID no existente
except Book.DoesNotExist:
    print("El libro no existe.")
