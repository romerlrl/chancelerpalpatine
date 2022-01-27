from unittest import TestCase
from bot.termooo.termoo import Termoo

class TestTermoo(TestCase):
    
    def test_instancing_termoo(self):
        game = Termoo()
        self.assertTrue(isinstance(game, Termoo))
    
    def test_if_word_out_of_csv_is_invalid(self):
        game = Termoo()
        guess = game.e2e("ABCDE")
        self.assertEqual(guess, "invalid word")
    
    def test_cool_game(self):
        game = Termoo()
        game.word = "CALOR"
        game.make_guess("CORRE")
        turn = game.history[0]
        self.assertEqual(turn, ("CORRE", list('GYYRR')))
        r = game.e2e("NEVAR")
        r = game.e2e("NEVARE")
        r = game.e2e("VACAS")
        txt = '\n> :regional_indicator_c: :regional_indicator_o: :regional_indicator_r: :regional_indicator_r: :regional_indicator_e:  \n> :green_circle: :yellow_circle: :yellow_circle: :red_circle: :red_circle: \n\n> :regional_indicator_n: :regional_indicator_e: :regional_indicator_v: :regional_indicator_a: :regional_indicator_r:  \n> :red_circle: :red_circle: :red_circle: :yellow_circle: :green_circle: \n\n> :regional_indicator_v: :regional_indicator_a: :regional_indicator_c: :regional_indicator_a: :regional_indicator_s:  \n> :red_circle: :green_circle: :yellow_circle: :red_circle: :red_circle: \n'
        self.assertEqual(r, txt)

    def test_end_game(self):
        game = Termoo()
        game.word = "CALOR"
        self.assertFalse(game.over)
        game.make_guess("VACAS")
        self.assertFalse(game.over)
        game.make_guess("CALOR")
        self.assertTrue(game.over)

    def test_to_string(self):
        game = Termoo()
        ot = game.output_tuple("ABC", ["R", "G", "G"])        
        self.assertEqual(ot, '\n> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c:  \n> :red_circle: :green_circle: :green_circle: \n')
        
