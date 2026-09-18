from django.shortcuts import render, get_object_or_404
from .models import Celebrity


def celebrity_list(request):
    celebrities = Celebrity.objects.all()
    category    = request.GET.get('category', '')

    if category:
        celebrities = celebrities.filter(category=category)

    context = {
        'page_title'       : 'Our Talent | LuminaStars',
        'meta_description' : 'Browse and book our exceptional roster of celebrities for your next event or brand campaign.',
        'celebrities'      : celebrities,
        'active_category'  : category,
        'categories'       : Celebrity.CATEGORY_CHOICES,
    }
    return render(request, 'celebrities/list.html', context)


def celebrity_detail(request, slug):
    celebrity = get_object_or_404(Celebrity, slug=slug)

    context = {
        'page_title'       : f'{celebrity.name} | LuminaStars',
        'meta_description' : f'Book {celebrity.name} — {celebrity.role}. Professional celebrity booking via LuminaStars.',
        'celebrity'        : celebrity,
    }
    return render(request, 'celebrities/detail.html', context)