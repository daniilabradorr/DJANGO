from Library.models import Author, Book, Member, Loan

# Creando autores.
author1 = Author.objects.create(
    full_name='Pepe Castro Vazquez'
)
author2 = Author.objects.create(
    full_name='Lucía Lopez Pérez'
)
author3 = Author.objects.create(
    full_name='Daniel Labrador Benito'
)

# Creando libros.
book1 = Book.objects.create(
    ibm=7890132,
    author=author1,
    name_book='Ciencia de la programación',
    publish_date='2023-01-01'
)
book2 = Book.objects.create(
    ibm=543210,
    author=author2,
    name_book='Python avanzado',
    publish_date='2023-11-07'
)
book3 = Book.objects.create(
    ibm=987654,
    author=author3,
    name_book='Django y sus principios',
    publish_date='2023-12-25'
)

# Creando miembros de la biblioteca.
member1 = Member.objects.create(
    full_name='Tomás Labrador Benito',
    email='tomaslabrador@gmail.com',
    joined_date='2023-05-24'
)
member2 = Member.objects.create(
    full_name='Marta González Sierra',
    email='martagonzalezsierra@gmail.com',
    joined_date='2024-06-09'
)
member3 = Member.objects.create(
    full_name='Aurelio Martin Fraile',
    email='aureliomartinfraile@gmail.com',
    joined_date='2023-12-02'
)

# Crear préstamos.
loan1 = Loan.objects.create(
    member_with_loan=member1,
    book_in_loan=book1,
    loan_date='2023-04-15',
    returned=True,
    returned_date='2023-10-16'
)
loan2 = Loan.objects.create(
    member_with_loan=member2,
    book_in_loan=book2,
    loan_date='2023-11-09',
    returned=True,
    returned_date='2024-02-22'
)
loan3 = Loan.objects.create(
    member_with_loan=member3,
    book_in_loan=book3,
    loan_date='2024-04-15',
    returned=False,
    returned_date= None
)
