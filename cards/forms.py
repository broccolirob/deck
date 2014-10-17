from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from cards.models import Player
from deck import settings


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = Player
        fields = ("username", "first_name", "last_name", "email", "phone", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Player.objects.get(username=username)
        except Player.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=commit)
        text_content = 'Thank you for signing up for our website, {}'.format(user.username)
        html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>'\
            .format(user.username)
        msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return user
