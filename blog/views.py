from django.shortcuts import render

from blog.models import Blog
from djank.models import DistributionList, Client
from djank.services import get_uniq_client, get_active_distribution, get_all_distributions, get_blog


# Create your views here.

def home(request):
    context = {
        'all_distributions': get_all_distributions(),
        'active_distribution': get_active_distribution(),
        'uniq_client': get_uniq_client(),
        'object_list': Blog.objects.all(),
        'random_blog': get_blog()
    }
    return render(request, 'djank/home.html', context)