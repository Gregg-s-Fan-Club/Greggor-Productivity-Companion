from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.conf import settings

def paginate(page: int, list_input,
             number_per_page: int = settings.NUMBER_OF_ITEMS_PER_PAGE) -> Page:
    """paginate lists and tables to be displayed to user"""
    list_of_items: list[Any] = []
    paginator: Paginator = Paginator(list_input, number_per_page)
    try:
        list_of_items: Page = paginator.page(page)
    except PageNotAnInteger:
        list_of_items: Page = paginator.page(1)
    except EmptyPage:
        list_of_items: Page = paginator.page(paginator.num_pages)

    return list_of_items