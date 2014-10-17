from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Sum
from django.shortcuts import render, redirect
from cards.forms import EmailUserCreationForm
from cards.models import Card, WarGame, Player
from cards.utils import get_random_comic
from deck import settings


def index(request):
    return render(request, 'index.html', {'comic': get_random_comic()})


@login_required
def profile(request):
    return render(request, 'profile.html', {
        'games': WarGame.objects.filter(player=request.user),
        'wins': request.user.get_wins(),
        'losses': request.user.get_losses(),
        'record': request.user.get_record_display()
    })


def faq(request):
    return render(request, 'faq.html')


def poker(request):
    data = {
        'cards': Card.objects.order_by('?')[:5]
    }
    return render(request, 'poker.html', data)


def blackjack(request):

    data = {
        'player': Card.objects.order_by('?')[:2],
        'dealer': Card.objects.order_by('?')[:2]
    }
    return render(request, 'blackjack.html', data)


def hearts(request):
    data = {
        'cards': Card.objects.filter(suit=3)
    }
    return render(request, 'hearts.html', data)


def num_cards(request):
    data = {
        'cards': Card.objects.exclude(rank__in=['jack', 'queen', 'king', 'ace'])
    }
    return render(request, 'num_cards.html', data)


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def war(request):
    random_cards = Card.objects.order_by('?')
    user_card = random_cards[0]
    dealer_card = random_cards[1]

    result = user_card.get_war_result(dealer_card)
    player = request.user
    WarGame.objects.create(result=result, player=player)
    if WarGame.objects.filter(player=player).count() == 10:
        text_content = 'Hi {} {}! Thank you for playing War!'.format(player.first_name, player.last_name,
                                                                     player.date_joined)
        html_content = '<h2>Hi {} {}!</h2> <div>Thanks for playing War!</div>'.format(player.first_name,
                                                                                      player.last_name,
                                                                                      player.date_joined)
        msg = EmailMultiAlternatives("Thank you!", text_content, settings.DEFAULT_FROM_EMAIL, [player.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return render(request, 'war.html', {
        'user_cards': [user_card],
        'dealer_cards': [dealer_card],
        'result': result
    })


def leaderboard(request):
    users = Player.objects.annotate(record=Sum('games__result')).order_by('-record')[:5]
    data = {'users': users}
    return render(request, "leaderboard.html", data)


def cards(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'cards.html', data)


def clubs(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'clubs.html', data)


def diamonds_hearts(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'diamonds_hearts.html', data)


def just_a_spade(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'just_a_spade.html', data)


def face_only(request):
    data = {
        'cards': [card for card in Card.objects.all() if card.rank in ['jack', 'queen', 'king', 'ace']]
    }

    return render(request, 'face.html', data)


def filters(request):
    data = {
        'cards': Card.objects.all().values()
    }

    return render(request, 'card_filters.html', data)


def first(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'first_filter.html', data)
