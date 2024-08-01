# mortgage.py
#
# Exercise 1.7

PRINCIPAL = 500000.00
RATE = .05
PAYMENT = 2684.11
TOTAL_PAID = 0.0

while PRINCIPAL > 0:
    PRINCIPAL = PRINCIPAL * (1 + RATE/12) - PAYMENT
    TOTAL_PAID = TOTAL_PAID + PAYMENT

print("Total paid:", round(TOTAL_PAID,2))

#
# Exercise 1.8
#

PRINCIPAL = 500000.00
RATE = .05
PAYMENT = 2684.11
TOTAL_PAID = 0.0
# MONTH_EXTRA = 0
MONTHS_TOTAL = 0

while PRINCIPAL > 0:
    while MONTHS_TOTAL < 12:
        PRINCIPAL = PRINCIPAL * (1 + RATE/12) - (PAYMENT + 1000)
        # MONTH_EXTRA = MONTH_EXTRA + 1
        MONTHS_TOTAL = MONTHS_TOTAL + 1
        TOTAL_PAID = TOTAL_PAID + PAYMENT + 1000
    PRINCIPAL = PRINCIPAL * (1 + RATE/12) - PAYMENT
    TOTAL_PAID = TOTAL_PAID + PAYMENT
    MONTHS_TOTAL = MONTHS_TOTAL + 1

print("Total paid:", round(TOTAL_PAID,2), "over", MONTHS_TOTAL, "months...")

#
# Exercise 1.9
#

PRINCIPAL = 500000.00
RATE = .05
PAYMENT = 2684.11
EXTRA_PAYMENT_START = 0
EXTRA_PAYMENT_END = 0
EXTRA_PAYMENT = 0
EXTRA_PAYMENT_START = int(
    input("Which month would you like to start your extra payments? "))
EXTRA_PAYMENT_END = int(
    input("Which month wouold you like to finish your extra payments? "))
EXTRA_PAYMENT = float(
    input("How much extra would you like to pay per month? "))
TOTAL_PAID = 0.0
# MONTH_EXTRA = 0
MONTHS_TOTAL = 0

while PRINCIPAL > 0:
    MONTHS_TOTAL = MONTHS_TOTAL + 1
    if MONTHS_TOTAL == EXTRA_PAYMENT_START:  
        while MONTHS_TOTAL <= EXTRA_PAYMENT_END:
            PRINCIPAL = PRINCIPAL * (1 + RATE/12) - (PAYMENT + EXTRA_PAYMENT)
            # MONTH_EXTRA = MONTH_EXTRA + 1
            TOTAL_PAID = TOTAL_PAID + PAYMENT + EXTRA_PAYMENT
            MONTHS_TOTAL = MONTHS_TOTAL + 1
    PRINCIPAL = PRINCIPAL * (1 + RATE/12) - PAYMENT
    TOTAL_PAID = TOTAL_PAID + PAYMENT
    

print("Total paid:", round(TOTAL_PAID,2), "over", MONTHS_TOTAL, "months...")

#
# Exercise 1.10
#

PRINCIPAL = 500000.00
RATE = .05
PAYMENT = 2684.11
EXTRA_PAYMENT_START = 0
EXTRA_PAYMENT_END = 0
EXTRA_PAYMENT = 0
EXTRA_PAYMENT_START = int(
    input("Which month would you like to start your extra payments? "))
EXTRA_PAYMENT_END = int(
    input("Which month wouold you like to finish your extra payments? "))
EXTRA_PAYMENT = float(
    input("How much extra would you like to pay per month? "))
TOTAL_PAID = 0.0
MONTHS_TOTAL = 0

while PRINCIPAL > 0:
    MONTHS_TOTAL = MONTHS_TOTAL + 1
    if MONTHS_TOTAL == EXTRA_PAYMENT_START:
        while MONTHS_TOTAL <= EXTRA_PAYMENT_END:
            PRINCIPAL = PRINCIPAL * (1 + RATE/12) - (PAYMENT + EXTRA_PAYMENT)
            TOTAL_PAID = TOTAL_PAID + PAYMENT + EXTRA_PAYMENT
            print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2), 
                  "- Extra payment month")
            MONTHS_TOTAL = MONTHS_TOTAL + 1
    PRINCIPAL = PRINCIPAL * (1 + RATE/12) - PAYMENT
    TOTAL_PAID = TOTAL_PAID + PAYMENT
    print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2))

print("Total paid:", round(TOTAL_PAID,2), "over", MONTHS_TOTAL, "months...")

#
# Exercise 1.11
#

PRINCIPAL = 500000.00
RATE = .05
PAYMENT = 2684.11
EXTRA_PAYMENT_START = 0
EXTRA_PAYMENT_END = 0
EXTRA_PAYMENT = 0
EXTRA_PAYMENT_START = int(
    input("Which month would you like to start your extra payments? "))
EXTRA_PAYMENT_END = int(
    input("Which month wouold you like to finish your extra payments? "))
EXTRA_PAYMENT = float(
    input("How much extra would you like to pay per month? "))
TOTAL_PAID = 0.0
MONTHS_TOTAL = 0

while PRINCIPAL > 0:
    MONTHS_TOTAL = MONTHS_TOTAL + 1
    if MONTHS_TOTAL == EXTRA_PAYMENT_START:
        while MONTHS_TOTAL <= EXTRA_PAYMENT_END and PRINCIPAL > 0:
            PRINCIPAL = PRINCIPAL * (1 + RATE/12) - (PAYMENT + EXTRA_PAYMENT)
            TOTAL_PAID = TOTAL_PAID + PAYMENT + EXTRA_PAYMENT
            if PRINCIPAL > 0:
                print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2), 
                  "- Extra payment month")
                MONTHS_TOTAL = MONTHS_TOTAL + 1
            else:
                PAYMENT = -PRINCIPAL
                TOTAL_PAID = TOTAL_PAID - PAYMENT
                PRINCIPAL = PRINCIPAL + PAYMENT
                print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2))
    if PRINCIPAL > 0:
        PRINCIPAL = PRINCIPAL * (1 + RATE/12) - PAYMENT
        TOTAL_PAID = TOTAL_PAID + PAYMENT
        if PRINCIPAL < 0:
            PAYMENT = -PRINCIPAL
            TOTAL_PAID = TOTAL_PAID - PAYMENT
            PRINCIPAL = PRINCIPAL + PAYMENT
            print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2))
    if PRINCIPAL > 0:
        print(MONTHS_TOTAL, round(TOTAL_PAID,2), round(PRINCIPAL,2))

print("Total paid:", round(TOTAL_PAID,2), "over", MONTHS_TOTAL, "months...")
