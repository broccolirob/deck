import factory
from cards.models import WarGame


class WarGameFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = WarGame


# class PlayerFactory(factory.django.DjangoModelFactory):
#
#     class Meta:
#         model = Player
#
#     password = 'password'
#     email = 'test@test.com'
#     username = factory.Sequence(lambda n: "user_%d" % n)
#
#     @classmethod
#     def _create(cls, model_class, *args, **kwargs):
#         """Override the default ``_create`` with our custom call."""
#         manager = cls._get_manager(model_class)
#         # The default would use ``manager.create(*args, **kwargs)``
#         return manager.create_user(*args, **kwargs)
