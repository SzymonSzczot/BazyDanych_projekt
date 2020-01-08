# coding=utf-8
import threading

import cv2
from django.shortcuts import render
from pytube import YouTube

from .models import (
    WhenFaceAppears,
    Clips
)


def find_ranges(video_id):

    print("STARTED")
    video = Clips.objects.get(video_id=video_id)

    times = []

    yt = YouTube(video.link)
    stream = yt.streams.first()
    stream.download(filename=video_id)
    input_movie = cv2.VideoCapture(f"{video_id}" + '.mp4')

    fps = input_movie.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    frame_number = 0

    while True:
        # Grab a single frame of video
        ret, frame = input_movie.read()
        frame_number += 1

        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            break

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces) > 0:

            # Draw a rectangle around the faces
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Faces found", frame)
            times.append(frame_number / fps)

    input_movie.release()
    cv2.destroyAllWindows()

    print(times)

    times = map(int, times)

    times = list(set(times))

    for start in times:

        link = f"https://youtu.be/{video_id}?t=" + str(start)
        WhenFaceAppears.objects.get_or_create(video=video, appeared_start=start, appeared_end=0, link=link)


def add_new_face(request, video_id):

    x = threading.Thread(target=find_ranges, args=(video_id,))
    x.start()

    video = Clips.objects.get(video_id=video_id)

    all_times = WhenFaceAppears.objects.filter(video=video)

    template_name = 'TyTube/show_times.html'
    context = {'object_list': all_times, 'title': "Times"}
    return render(request, template_name, context)


def show_times(request, video_id):
    """
    All Times list view
    """

    vid = Clips.objects.get(video_id=video_id)

    all_times = WhenFaceAppears.objects.filter(video=vid)

    # paging
    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(all_times, 50)
    # try:
    #     all_times = paginator.page(page)
    # except PageNotAnInteger:
    #     all_times = paginator.page(1)
    # except EmptyPage:
    #     all_times = paginator.page(paginator.num_pages)

    # frontend
    template_name = 'TyTube/show_times.html'
    context = {'object_list': all_times, 'title': "Times"}
    return render(request, template_name, context)
