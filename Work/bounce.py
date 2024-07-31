# bounce.py
#
# Exercise 1.5

HEIGHT = 100 # Height of the drop (meters)
Q_BOUNCE_BACK = 3/5 # Distance traveled upon bouncing back (coefficient)
BOUNCE_COUNT = 0

while BOUNCE_COUNT in range(10):
    HEIGHT = Q_BOUNCE_BACK * HEIGHT
    BOUNCE_COUNT = BOUNCE_COUNT + 1
    print(BOUNCE_COUNT, round(HEIGHT, 4))

