from django.core.management.base import BaseCommand
from greggor_productivity_companion.models import Category, User, Task, WorkPeriod
from datetime import datetime, timedelta, date

class Command(BaseCommand):
    """Database Seeder"""
   
    def __init__(self) -> None:
        super().__init__()
        
    def handle(self, *args,  **options) -> None:
        self.create_users()
        self.create_categories()
        self.create_work_periods()
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
    
    def create_users(self):
        if not User.objects.filter(username = "@janedoe", email="janedoe@example.com"):
            user = User.objects.create_user(
            username= "@janedoe",
            email="janedoe@example.com",
            password= "admin"
            )
        else:
            user = User.objects.filter(username = "@janedoe", email="janedoe@example.com")[0]
        
        self.create_tasks(user)
        
    
    def create_tasks(self, user):
        category = Category.objects.filter(name = "Education")
        if not category:
            self.create_categories()
        category = Category.objects.filter(name = "Education")[0]

        category = Category.objects.filter(name = "Education")[0]
        if not Task.objects.filter(user = user, category=category, name = "CourseWork Assignment"):
            Task.objects.create(
            user= user,
            name = "CourseWork Assignment",
            description = "CourseWork Assignment",
            expected_work_time = timedelta(hours = 2),
            category=category,
            completed = False
            )
        
        if not Task.objects.filter(user = user, category=category, name = "Lectures"):
            Task.objects.create(
            user= user,
            name = "Lectures",
            description = "Lectures",
            expected_work_time = timedelta(hours = 2),
            category=category,
            completed = False
            )
        

        category = Category.objects.filter(name = "Health")
        if not category:
            self.create_categories()
        category = Category.objects.filter(name = "Health")[0]

        category = Category.objects.filter(name = "Health")[0]
        if not Task.objects.filter(user = user, category=category, name = "Go for a run"):
            Task.objects.create(
            user= user,
            name = "Go for a run",
            description = "Put some running shoes and get some fresh air.",
            expected_work_time = timedelta(hours = 2),
            category=category,
            completed = False
            )
        
        if not Task.objects.filter(user = user, category=category, name = "Go to doctor"):
            Task.objects.create(
            user= user,
            name = "Go to doctor",
            description = "Go to doctor",
            expected_work_time = timedelta(hours = 2),
            category=category,
            completed = False
            )
        
        category = Category.objects.filter(name = "Hobbies")
        if not category:
            self.create_categories()
        category = Category.objects.filter(name = "Hobbies")[0]

        category = Category.objects.filter(name = "Hobbies")[0]
        if not Task.objects.filter(user = user, category=category, name = "Football"):
            Task.objects.create(
            user= user,
            name = "Football",
            description = "Football",
            expected_work_time = timedelta(hours = 1),
            category=category,
            completed = False
            )
        
        if not Task.objects.filter(user = user, category=category, name = "Read Harry Potter"):
            Task.objects.create(
            user= user,
            name = "Read Harry Potter",
            description = "Read Harry Potter",
            expected_work_time = timedelta(hours = 2),
            category=category,
            completed = True
            )


    def create_work_periods(self):
        task = Task.objects.filter(name = "Football")
        if not task:
            self.create_tasks()
        task = Task.objects.filter(name = "Football")[0]

        if not WorkPeriod.objects.filter(date = datetime(2024, 3, 8), start_time="12:12:12", end_time ="14:14:14", task=task):
            WorkPeriod.objects.create(
            date= datetime(2024, 3, 8),
            start_time = "12:12:12",
            end_time ="14:14:14",
            points = 230,
            task=task
        
            )
        
        task = Task.objects.filter(name = "Go to doctor")
        if not task:
            self.create_tasks()
        task = Task.objects.filter(name = "Go to doctor")[0]

        if not WorkPeriod.objects.filter(date = datetime(2024, 3, 8), start_time="12:12:12", end_time ="13:13:13", task=task):
            WorkPeriod.objects.create(
            date= datetime(2024, 3, 8),
            start_time = "12:12:12",
            end_time ="13:13:13",
            points = 290,
            task=task
            )
        if not WorkPeriod.objects.filter(date = datetime(2024, 3, 1), start_time="12:12:12", end_time ="14:14:14", task=task):
            WorkPeriod.objects.create(
            date= datetime(2024, 3, 1),
            start_time = "12:12:12",
            end_time ="14:14:14",
            points = 30,
            task=task
        
            )
        


   