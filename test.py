import unittest
from snake_game import snake, cube, randomSnack

class TestSnakeGame(unittest.TestCase):
    
    def setUp(self):
        self.snake = snake((255,0,0), (10, 10))  # Inicializa la serpiente en la posición (10, 10)
        self.snake.addCube()  # Añade un cubo para simular el cuerpo de la serpiente
    
    def test_initial_position(self):
        """Prueba que la serpiente inicie en la posición correcta."""
        self.assertEqual(self.snake.head.pos, (10, 10))
    
    def test_move_right(self):
        """Prueba el movimiento hacia la derecha."""
        self.snake.dirnx, self.snake.dirny = 1, 0
        self.snake.move()
        self.assertEqual(self.snake.head.pos, (11, 10))  # Verificamos que se movió correctamente

    def test_grow_on_eat(self):
        """Prueba que la serpiente crezca al comer un snack."""
        initial_length = len(self.snake.body)
        self.snake.addCube()  # Simulamos que la serpiente come un snack
        self.assertEqual(len(self.snake.body), initial_length + 1)  # Verificamos que ha crecido
    
    def test_random_snack_generation(self):
        """Prueba que el snack se genere en una posición válida."""
        snack_pos = randomSnack(20, self.snake)  # Generamos una posición para el snack
        self.assertNotIn(snack_pos, list(map(lambda c: c.pos, self.snake.body)))  # Verificamos que no esté sobre la serpiente

if __name__ == '__main__':
    unittest.main()
