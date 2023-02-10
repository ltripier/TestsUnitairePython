import sys
sys.path.append('C:/Users/lucas/Documents/Python/TestsUnitairePython/app')
from Bibliotheque import Book, Library, Client
import unittest

class BookTest(unittest.TestCase):
    def test_valid_inputs(self):
        # Test avec des entrées valides
        book = Book("Un Bon Libre", "Moi")
        self.assertEqual(book.title, "Un Bon Libre")
        self.assertEqual(book.author, "Moi")
    
    def test_invalid_inputs(self):
        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            book = Book("", "Auteur du livre")
        with self.assertRaises(ValueError):
            book = Book("Titre du livre", "")
        with self.assertRaises(ValueError):
            book = Book("Titre du livre", 5) 

class LibraryTest(unittest.TestCase):
    def test_add_book(self):
        # Test pour ajouter un livre à la bibliothèque

        # Test avec des entrées valides
        library = Library()
        book = Book("UnBonLivre", "Moi")
        library.add_book(book)

        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            library = Library()
            library.add_book("Un mauvais livre")

        with self.assertRaises(ValueError):
            library = Library()
            library.add_book(1052)

    
    def test_check_out_book(self):
        # Test pour vérifier un livre

        # Test avec des entrées valides
        library = Library()
        book = Book("Un bon livre", "Moi")
        library.add_book(book)
        library.check_out_book("Un bon livre")

        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            library = Library()
            book = Book("Un bon livre", "Moi")
            library.add_book(book)
            library.check_out_book("")

        with self.assertRaises(ValueError):
            library = Library()
            book = Book("Un bon livre", "Moi")
            library.add_book(book)
            library.check_out_book(122)
    
    def test_check_in_book(self):
        # Test pour retourner un livre

        # Test avec des entrées valides
        library = Library()
        book = Book("Un bon livre", "Moi")
        library.add_book(book)
        library.check_out_book("Un bon livre")
        library.check_in_book("Un bon livre")

        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            library = Library()
            book = Book("Un bon livre", "Moi")
            library.add_book(book)
            library.check_out_book("Un bon livre")
            library.check_in_book("")

        with self.assertRaises(ValueError):
            library = Library()
            book = Book("Un bon livre", "Moi")
            library.add_book(book)
            library.check_out_book("Un bon livre")
            library.check_in_book(122)

class ClientTest(unittest.TestCase):
    def test_valid_inputs(self):
        # Test avec des entrées valides
        client = Client("Lucas")
        self.assertEqual(client.name, "Lucas")

    def test_invalid_inputs(self):
         # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            client = Client("")
        with self.assertRaises(ValueError):
            client = Client(32315614)
    
    def test_check_out_book(self):
        # Test avec des entrées valides
        client = Client("Lucas")
        library = Library()
        client.check_out_book(library, "Un titre")

        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            client = Client("Lucas")
            library = Library()
            client.check_out_book(library, "")

        with self.assertRaises(ValueError):
            client = Client("Lucas")
            library = Library()
            client.check_out_book("library", "Un titre")

    def test_check_in_book(self):
        # Test avec des entrées valides
        client = Client("Lucas")
        library = Library()
        client.check_in_book(library, "Un titre")

        # Test avec des entrées non valides
        with self.assertRaises(ValueError):
            client = Client("Lucas")
            library = Library()
            client.check_in_book(library, "")

        with self.assertRaises(ValueError):
            client = Client("Lucas")
            library = Library()
            client.check_in_book("library", "Un titre")

clientTest = ClientTest()
clientTest.test_valid_inputs()
clientTest.test_invalid_inputs()
clientTest.test_check_out_book()
clientTest.test_check_in_book()

bookTest = BookTest()
bookTest.test_valid_inputs()
bookTest.test_invalid_inputs()

library = LibraryTest()
library.test_add_book()
library.test_check_out_book()
library.test_check_in_book()