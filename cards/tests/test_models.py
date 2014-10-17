from django.test import TestCase
from cards.models import Card, WarGame, Player
from cards.tests.factories import WarGameFactory


class CardModelTestCase(TestCase):

    def test_get_ranking(self):
        card = Card.objects.create(suit=Card.CLUB, rank='jack')
        self.assertEqual(card.get_ranking(), 11)

    def test_get_war_result_equal(self):
        user_card = Card.objects.create(suit=Card.CLUB, rank='five')
        computer_card = Card.objects.create(suit=Card.CLUB, rank='five')
        self.assertEqual(user_card.get_war_result(computer_card), 0)

    def test_get_war_result_loss(self):
        user_card = Card.objects.create(suit=Card.CLUB, rank='five')
        computer_card = Card.objects.create(suit=Card.CLUB, rank='six')
        self.assertEqual(user_card.get_war_result(computer_card), -1)

    def test_get_war_result_win(self):
        user_card = Card.objects.create(suit=Card.CLUB, rank='five')
        computer_card = Card.objects.create(suit=Card.CLUB, rank='four')
        self.assertEqual(user_card.get_war_result(computer_card), 1)


class PlayerModelTestCase(TestCase):

    def test_get_wins(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
        self.assertEqual(user.get_wins(), 2)

    def test_get_losses(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        self.assertEqual(user.get_losses(), 3)

    def test_get_ties(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
        self.assertEqual(user.get_ties(), 4)

    def test_get_record_display(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
        self.assertEqual(user.get_record_display(), "2-3-4")
