from django.test import TestCase

from cards.models import Card
from cards.tests.utils import run_pyflakes_for_package, run_pep8_for_package
from cards.utils import create_deck


class UtilTestCase(TestCase):

    def test_create_deck_count(self):
        create_deck()
        self.assertEqual(Card.objects.count(), 52)


class SyntaxTest(TestCase):

    def test_syntax(self):
        packages = ['cards']
        warnings = []
        for package in packages:
            warnings.extend(run_pyflakes_for_package(package, extra_ignore=("_settings",)))
            warnings.extend(run_pep8_for_package(package, extra_ignore=("_settings",)))
        if warnings:
            self.fail("{0} Syntax warnings!\n\n{1}".format(len(warnings), "\n".join(warnings)))
