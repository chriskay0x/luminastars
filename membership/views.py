from django.shortcuts import render, redirect, get_object_or_404
from .models import MembershipPlan, MembershipApplication
from .forms import MembershipApplicationForm


def membership_page(request):
    plans = MembershipPlan.objects.all()
    form  = MembershipApplicationForm()

    context = {
        'page_title'       : 'Management Membership | LuminaStars',
        'meta_description' : 'Join the LuminaStars management community. Choose from Regular, Premium or VIP membership.',
        'plans'            : plans,
        'form'             : form,
    }
    return render(request, 'membership/membership.html', context)


def apply(request, plan_id):
    plan = get_object_or_404(MembershipPlan, id=plan_id)

    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.plan = plan
            application.save()
            return redirect('membership:success', application_id=application.id)
        # If invalid, re-render with errors
        plans = MembershipPlan.objects.all()
        return render(request, 'membership/membership.html', {
            'plans'       : plans,
            'form'        : form,
            'active_plan' : plan.id,
        })

    return redirect('membership:page')


def success(request, application_id):
    application = get_object_or_404(MembershipApplication, id=application_id)

    context = {
        'page_title'  : 'Application Received | LuminaStars',
        'application' : application,
    }
    return render(request, 'membership/success.html', context)