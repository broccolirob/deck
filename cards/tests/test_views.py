from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
from mock import patch, Mock
from cards.models import WarGame, Player
from cards.tests.factories import WarGameFactory
from cards.utils import create_deck


class ViewTestCase(TestCase):
    def setUp(self):
        create_deck()

    def test_cards_page(self):
        response = self.client.get(reverse('cards'))
        self.assertIn('<p>Suit: spade, Rank: two</p>', response.content)
        self.assertEqual(response.context['cards'].count(), 52)

    def test_faq_page(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('<p>A: Nope, this is not real, sorry.</p>', response.content)

    def test_filters_page(self):
        response = self.client.get(reverse('first'))
        self.assertIn('<p>Suit: club, Rank: ace</p>', response.content)
        self.assertEqual(response.context['cards'].count(), 52)

    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test',
            'phone': '652-154-4875',
            'first_name': 'tony',
            'last_name': 'montana'
        }
        response = self.client.post(reverse('register'), data)
        print("objects are %s" % Player.objects.all())
        # Check this user was created in the database
        self.assertTrue(Player.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))

    def test_profile_page(self):
        # Create user and log them in
        password = 'passsword'
        user = Player.objects.create_user(username='test-user', email='test@test.com', password=password)
        self.client.login(username=user.username, password=password)

        # Set up some war game entries
        WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
        record = user.get_record_display()

        # Make the url call and check the html and games queryset length
        response = self.client.get(reverse('profile'))
        self.assertInHTML('<p>Results: {}</p>'.format(record), response.content)
        self.assertInHTML('<p>Your email address is {}</p>'.format(user.email), response.content)
        self.assertEqual(len(response.context['games']), 9)

    @patch('cards.utils.requests')
    def test_home_page(self, mock_requests):
        mock_comic = {
            'num': 1433,
            'year': "2014",
            'safe_title': "Lightsaber",
            'alt': "A long time in the future, in a galaxy far, far, away.",
            'transcript': "An unusual gamma-ray burst originating from somewhere across the universe.",
            'img': "http://imgs.xkcd.com/comics/lightsaber.png",
            'title': "Lightsaber",
        }
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_comic
        mock_requests.get.return_value = mock_response
        response = self.client.get(reverse('index'))
        self.assertIn('<h3>{} - {}</h3>'.format(mock_comic['safe_title'], mock_comic['year']),
                      response.content)
        self.assertIn('<img alt="{}" src="{}">'.format(mock_comic['alt'], mock_comic['img']),
                      response.content)
        self.assertIn('<p>{}</p>'.format(mock_comic['transcript']), response.content)
