人感センサー = 0
P = 0
pins.set_audio_pin(AnalogPin.P0)
me = 10
next2 = 100
radio.set_group(me)

def on_every_interval():
    global P, 人感センサー
    P = pins.digital_read_pin(DigitalPin.P0)
    gp2.turn_on()
    if P == 1:
        if 人感センサー == 1:
            radio.set_group(next2)
            radio.send_number(2)
            radio.set_group(me)
        gp2.turn_off()
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        人感センサー = 0
    else:
        if 人感センサー == 0:
            radio.set_group(next2)
            radio.send_number(5)
            radio.set_group(me)
        gp2.turn_off()
        basic.show_icon(IconNames.CONFUSED)
        basic.clear_screen()
        人感センサー = 1
loops.every_interval(1000, on_every_interval)