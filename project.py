s1 = 1
s2 = 0

def setup():
    pinMode(2, INPUT)
    pinMode(13, OUTPUT)
    pinMode(12, OUTPUT)
    pinMode(11, OUTPUT)
    pinMode(3, INPUT)
    pinMode(10, OUTPUT)
    pinMode(9, OUTPUT)
    pinMode(8, OUTPUT)

def loop():
    if digitalRead(2) == 1:
        on1()
    elif digitalRead(3) == 1:
        on2()
    else:
        if s1:
            on2()
        elif s2:
            on1()

def on1():
    off2()
    s1 = 1
    s2 = 0
    digitalWrite(11, LOW)
    digitalWrite(13, HIGH)
    delay(3000)
    digitalWrite(13, LOW)
    digitalWrite(12, HIGH)
    delay(2000)
    digitalWrite(12, LOW)
    digitalWrite(11, HIGH)

def off1():
    digitalWrite(13, LOW)
    digitalWrite(12, LOW)
    digitalWrite(11, HIGH)

def on2():
    off1()
    s2 = 1
    s1 = 0
    digitalWrite(8, LOW)
    digitalWrite(10, HIGH)
    delay(3000)
    digitalWrite(10, LOW)
    digitalWrite(9, HIGH)
    delay(2000)
    digitalWrite(9, LOW)
    digitalWrite(8, HIGH)

def off2():
    digitalWrite(10, LOW)
    digitalWrite(9, LOW)
    digitalWrite(8, HIGH)