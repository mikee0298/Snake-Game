import unittest
from snake_game import snake, cube  # Asegúrate de tener el código del juego en 'snake_game.py'

class TestSnakeGame(unittest.TestCase):
    
    def setUp(self):
        # Este método se ejecuta antes de cada prueba
        self.s = snake((255, 0, 0), (10, 10))  # Crear una instancia de la serpiente

    def test_snake_initial_position(self):
        """Verifica que el snake comience en la posición correcta"""
        self.assertEqual(self.s.head.pos, (10, 10))  # El snake debería empezar en (10, 10)

    def test_snake_move_right(self):
        """Simula un movimiento hacia la derecha"""
        self.s.dirnx = 1  # Dirección derecha
        self.s.dirny = 0  # No moverse verticalmente
        self.s.move()  # Ejecuta el movimiento
        self.assertEqual(self.s.head.pos, (11, 10))  # El snake debe haber avanzado a (11, 10)

    def test_snake_grow(self):
        """Prueba que el snake crezca correctamente"""
        initial_length = len(self.s.body)  # Longitud inicial del snake
        self.s.addCube()  # Simula comer un snack y crecer
        new_length = len(self.s.body)  # Nueva longitud
        self.assertEqual(new_length, initial_length + 1)  # Verifica que el snake ha crecido en 1

if __name__ == '__main__':
    unittest.main()
