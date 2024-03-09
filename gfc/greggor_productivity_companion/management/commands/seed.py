from django.core.management.base import BaseCommand
from greggor_productivity_companion.models import Category


class Command(BaseCommand):
    """Database Seeder"""
   
    def __init__(self) -> None:
        super().__init__()
        
    def handle(self, *args,  **options) -> None:
        self.create_categories()
        print("SEEDING COMPLETE")
    
    def create_categories(self):
        if not Category.objects.filter(name = "Health"):
            Category.objects.create(
            name= "Health",
            max_points_per_cycle = 100
            )
        
        if not Category.objects.filter(name = "Work"):
            Category.objects.create(
            name= "Work",
            max_points_per_cycle = 100
            )
        if not Category.objects.filter(name = "Education"):
            Category.objects.create(
            name= "Education",
            max_points_per_cycle = 100
            )
        if not Category.objects.filter(name = "Hobbies"):
            Category.objects.create(
            name= "Hobbies",
            max_points_per_cycle = 100
            )



    


   