from threading import Thread

from django.shortcuts import render

import _thread


is_started = 0


def main(request):
    global is_started

    def dummy():
        pass

    def start_new_thread(function):

        def decorator(*args, **kwargs):
            t = Thread(target=function, args=args, kwargs=kwargs)
            t.daemon = True
            t.start()

        return decorator

    if is_started == 0:
        try:
            print("STARTING")
        except:
            pass

        try:
            _thread.start_new_thread(dummy, ())
        except:
            print("Error: unable to start thread")

        is_started = 1

    return render(request, "home.html", {'title': "FaceTube"})
