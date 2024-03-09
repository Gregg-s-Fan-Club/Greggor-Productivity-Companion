from django.core.management.base import BaseCommand
from greggor_productivity_companion.models import Category


class Command(BaseCommand):
    """Database Seeder"""
   
    def __init__(self) -> None:
        super().__init__()
        
    def handle(self, *args: list[Any], **options: dict[Any, Any]) -> None:
        
        print("SEEDING COMPLETE")


    


   