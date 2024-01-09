from django.shortcuts import render

from .forms import UserForm


def user_form_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm(request.POST or None)
    context = {
        'form':form
    }

    return render(request, 'home.html', context)