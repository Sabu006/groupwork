def on_received_number(receivedNumber):
    global n
    n = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_number(counter)
    if counter > 0:
        music.play_tone(185, music.beat(BeatFraction.BREVE))
input.on_button_pressed(Button.A, on_button_pressed_a)

num = 0
counter = 0
n = 0
n = 10
me = 100
next2 = 10
radio.set_group(me)
list2 = [0, 0, 0]

def on_forever():
    global counter, num, list2
    list2 = [0, 0, 0]
    if counter < 0:
        counter = 0
    if n - 4 < 0:
        list2 = [0, 0, 0]
        index = 0
        while index < 3:
            list2[index] = n
            basic.pause(1000)
            index += 1
        num = list2[1] - list2[2]
        basic.pause(1000)
    if list2[0] * (num * n) == -28:
        counter = counter + 1
        index = 0
        while index < 3:
            list2[index] = 0
            index += 1
    elif list2[0] * (num * n) == -75:
        counter = counter - 1
        index = 0
        while index < 3:
            list2[index] = 0
            index += 1
    else:
        index = 0
        while index < 3:
            list2[index] = 0
            index += 1

basic.forever(on_forever)