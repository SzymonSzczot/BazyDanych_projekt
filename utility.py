import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import TyTube.models as m


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


def add_new_face(title, times):
    video = m.Clips.objects.get(title=title)

    start, end = times

    if end > start:

        m.WhenFaceAppears.objects.create(
            video=video,
            appeared_start=start,
            appeared_end=end,
        )


if __name__ == '__main__':

    input_data = {}

    input_data['link'] = "youtube.pl"
    input_data['title'] = "FILM"
    input_data['duration'] = 10
    input_data['canal'] = "TESTOWY"
    input_data['p_voices'] = 10
    input_data['n_voices'] = 10
    input_data['upload_date'] = "2019-12-15"

    # add_new_clip(input_data)

    time = (10, 20)

    add_new_face("FILM", time)
