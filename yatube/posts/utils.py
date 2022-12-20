from django.core.paginator import Paginator
from django.conf import settings


def get_pagin(queryset, request):
    paginator = Paginator(queryset, (settings.LIMIT))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
