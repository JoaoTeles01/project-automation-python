from pynput import mouse


while True:

    with mouse.Events() as Event:
        evento = Event.get()

        if type(evento) == Event.Click:
            print(evento)