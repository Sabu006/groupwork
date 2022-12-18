radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    n = receivedNumber
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(counter)
    if (counter > 0) {
        music.playTone(185, music.beat(BeatFraction.Breve))
    }
    
})
let num = 0
let counter = 0
let n = 0
n = 10
let me = 100
let next2 = 10
radio.setGroup(me)
let list2 = [0, 0, 0]
basic.forever(function on_forever() {
    let index: number;
    
    list2 = [0, 0, 0]
    if (counter < 0) {
        counter = 0
    }
    
    if (n - 4 < 0) {
        list2 = [0, 0, 0]
        index = 0
        while (index < 3) {
            list2[index] = n
            basic.pause(1000)
            index += 1
        }
        num = list2[1] - list2[2]
        basic.pause(1000)
    }
    
    if (list2[0] * (num * n) == -28) {
        counter = counter + 1
        index = 0
        while (index < 3) {
            list2[index] = 0
            index += 1
        }
    } else if (list2[0] * (num * n) == -75) {
        counter = counter - 1
        index = 0
        while (index < 3) {
            list2[index] = 0
            index += 1
        }
    } else {
        index = 0
        while (index < 3) {
            list2[index] = 0
            index += 1
        }
    }
    
})
