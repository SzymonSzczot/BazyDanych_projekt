import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import TyTube.models as m

import cv2
from pytube import YouTube

def add_new_clip(input_data):

    m.Clips.objects.create(
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


def add_new_face(title):
    video = m.Clips.objects.get(title=title)

    times = []

    yt = YouTube(video.link)
    stream = yt.streams.first()
    # stream.download(filename="video")
    input_movie = cv2.VideoCapture('video.mp4')

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
        # Quit when the input video file ends
        if not ret:
            break

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces) > 0:
            print("Found {0} faces!".format(len(faces)))

            # Draw a rectangle around the faces
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Faces found", frame)
            times.append(frame_number/fps)

        # All done!
    print(times)
    input_movie.release()
    cv2.destroyAllWindows()

    ranges = []

    for i in range(0, len(times) - 1):
        start = times[i]
        if times[i+1] - times[i] < 1:
            continue
        else:
            end = times[i+1]
            ranges.append((int(start), int(end)))
    print(ranges)
