# coding=utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from pytube import YouTube

from .forms import (
    ClipsModelForm,
)
from .models import (
    Clips,
)


def create_clip(request):
    """
    Add new clip
    """

    form = ClipsModelForm(request.POST or None)

    if form.is_valid():

        obj = form.save(commit=False)

        print(obj)

        video_id = obj.link.split("/")[-1]
        obj.video_id = video_id

        link = str("https://www.youtube.com/watch?v=" + video_id)

        print(link)

        YouTubeVideoObject = YouTube(link)

        print(YouTubeVideoObject)

        obj.title = YouTubeVideoObject.title
        obj.votes = YouTubeVideoObject.rating
        obj.upload_date = YouTubeVideoObject.streams
        obj.views = YouTubeVideoObject.views
        print("XD", obj.upload_date)

        # form.save()
        form = ClipsModelForm()

    # frontend
    template_name = 'form.html'
    context = {'form': form, 'tytul': "Dodaj Klip"}
    return render(request, template_name, context)


def show_clips(request):
    """
    All Videos list view
    """
    all_clips = Clips.objects.all()

    # paging
    page = request.GET.get('page', 1)

    paginator = Paginator(all_clips, 50)
    try:
        all_clips = paginator.page(page)
    except PageNotAnInteger:
        all_clips = paginator.page(1)
    except EmptyPage:
        all_clips = paginator.page(paginator.num_pages)

    # frontend
    template_name = 'TyTube/show_clips.html'
    context = {'object_list': all_clips, 'title': "Videos"}
    return render(request, template_name, context)


def auto_create_clip(input_data):

    Clips.objects.create(
        link=input_data['link'],
        title=input_data['title'],
        duration=input_data['duration'],
        face_recognized_count=0,
        face_on_screen_time=0,
        canal=input_data['canal'],
        positive_voices=input_data['p_voices'],
        negative_voices=input_data['n_voices'],
        upload_date=input_data['upload_date'],
    )

    return redirect('/main')
