from blog.models import Blog
from djank.models import Client, DistributionList


def get_uniq_client():
    uniq_client = Client.objects.all()
    email_list = []
    for i in uniq_client:
        email_list.append(i.email)

    return len(set(email_list))


def get_active_distribution():
    distribution = DistributionList.objects.all().filter(status='launched')
    return len(distribution)


def get_all_distributions():
    distribution = DistributionList.objects.all()
    return len(distribution)

def get_blog():
    blog = Blog.objects.order_by("?")[:3]

    for item in blog:
        item.views += 1
        item.save()

    return blog