import unittest
from unittest.mock import patch
import pygame
from snake import snake, cube, randomSnack

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        # Setup del Snake antes de cada prueba
        self.s = snake((255, 0, 0), (10, 10))

    def test_snake_initial_position(self):
        # Verifica que el snake empieza en la posición correcta
        self.assertEqual(self.s.head.pos, (10, 10))

    def test_snake_move_right(self):
        # Simula movimiento hacia la derecha
        self.s.move()
        self.assertEqual(self.s.head.pos, (11, 10))

    def test_snake_grow(self):
        # Prueba que el snake crece correctamente al comer un snack
        initial_length = len(self.s.body)
        self.s.addCube()
        new_length = len(self.s.body)
        self.assertEqual(new_length, initial_length + 1)

    def test_snake_collision_with_wall(self):
        # Simula que el snake choca con la pared
        self.s.head.pos = (19, 10)  # Posición cerca del borde derecho
        self.s.dirnx = 1  # Dirección hacia la derecha
        self.s.move()
        self.assertTrue(self.s.head.pos[0] >= 20)

    @patch('snake_game.randomSnack')
    def test_snack_random_position(self, mock_randomSnack):
        # Prueba que el snack se genera en una posición válida
        mock_randomSnack.return_value = (5, 5)
        snack = cube(randomSnack(20, self.s), color=(0, 255, 0))
        self.assertEqual(snack.pos, (5, 5))

    def test_snake_self_collision(self):
        # Prueba que el snake se reinicia tras colisionar consigo mismo
        self.s.body.append(cube((10, 11)))  # Añadir un segmento a la serpiente
        self.s.body.append(cube((10, 12)))
        self.s.head.pos = (10, 12)  # Simula una colisión con el cuerpo
        with patch('builtins.print') as mocked_print:
            self.s.move()
            mocked_print.assert_called_with('Score:', len(self.s.body))
            self.assertEqual(self.s.head.pos, (10, 10))  # Se reinicia a la posición inicial

if __name__ == '__main__':
    unittest.main()
