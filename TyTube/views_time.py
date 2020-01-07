# coding=utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .forms import (
    WhenFaceAppearsModelForm,
)
from .models import (
    WhenFaceAppears,
)


def create_time(request):
    """
    Add new clip
    """

    form = WhenFaceAppearsModelForm(request.POST or None)

    print(form.is_valid())

    if form.is_valid():
        form.save()
        form = WhenFaceAppearsModelForm()

    # frontend
    template_name = 'form.html'
    context = {'form': form, 'tytul': "Dodaj Czas"}
    return render(request, template_name, context)


def show_times(request):
    """
    All Times list view
    """
    all_times = WhenFaceAppears.objects.all()

    # paging
    page = request.GET.get('page', 1)

    paginator = Paginator(all_times, 50)
    try:
        all_times = paginator.page(page)
    except PageNotAnInteger:
        all_times = paginator.page(1)
    except EmptyPage:
        all_times = paginator.page(paginator.num_pages)

    # frontend
    template_name = 'TyTube/show_times.html'
    context = {'object_list': all_times, 'title': "Times"}
    return render(request, template_name, context)
