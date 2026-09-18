from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from celebrities.models import Celebrity
from membership.models import MembershipPlan

def home(request):
    return render(request, 'core/home.html')

def about(request):
    context = {
        'page_title'       : 'About Us | LuminaStars',
        'meta_description' : 'Learn about LuminaStars — our story, mission and the team behind the world\'s premier celebrity management agency.',
    }
    return render(request, 'core/about.html', context)


def projects(request):
    all_projects  = Project.objects.all()
    category      = request.GET.get('category', '')
    if category:
        all_projects = all_projects.filter(category=category)
    context = {
        'page_title'       : 'Projects | LuminaStars',
        'meta_description' : 'Explore LuminaStars featured projects — global tours, brand campaigns and exclusive celebrity experiences.',
        'projects'         : all_projects,
        'active_category'  : category,
        'categories'       : Project.CATEGORY_CHOICES,
    }
    return render(request, 'core/projects.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:contact_success')
    else:
        form = ContactForm()

    context = {
        'page_title'       : 'Contact Us | LuminaStars',
        'meta_description' : 'Get in touch with LuminaStars — for bookings, partnerships, membership and general enquiries.',
        'form'             : form,
    }
    return render(request, 'core/contact.html', context)


def contact_success(request):
    context = {
        'page_title' : 'Message Sent | LuminaStars',
    }
    return render(request, 'core/contact_success.html', context)


def home(request):
    featured_celebrities = Celebrity.objects.filter(is_featured=True)[:3]
    featured_projects    = Project.objects.filter(is_featured=True)[:3]
    # Fallback if no featured items set yet
    if not featured_celebrities:
        featured_celebrities = Celebrity.objects.all()[:3]
    if not featured_projects:
        featured_projects = Project.objects.all()[:3]
    context = {
        'page_title'          : 'LuminaStars | Where Stars Are Born',
        'meta_description'    : 'LuminaStars is a premier global celebrity management agency offering professional representation, strategic career management and exclusive event bookings.',
        'featured_celebrities': featured_celebrities,
        'featured_projects'   : featured_projects,
        'membership_plans': MembershipPlan.objects.all(),
    }
    return render(request, 'core/home.html', context)