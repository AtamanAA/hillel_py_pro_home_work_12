from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Publication


class Command(BaseCommand):
    help = "Generate fake publications. Default count = 100"

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()
        publication_list = []
        for _ in range(options["count"]):
            publication_list.append(
                Publication(
                    title=fake.sentence(nb_words=5, variable_nb_words=False),
                    content=fake.text(max_nb_chars=500),
                )
            )
        publications = Publication.objects.bulk_create(publication_list)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully generated {len(publications)} publications"
            )
        )
