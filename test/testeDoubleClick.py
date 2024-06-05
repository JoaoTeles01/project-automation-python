from pynput import mouse
import time

last_click_time = time.time()

def on_click(x, y, button, pressed):
    global last_click_time

    if pressed:
        elapsed_time = time.time() - last_click_time

        if elapsed_time < 0.5:
            print('Duplo clique')
        last_click_time = time.time()


with mouse.Listener(on_click=on_click) as listener:
    input('Pressione "Enter" para parar de ouvir eventos do mouse...\n')
