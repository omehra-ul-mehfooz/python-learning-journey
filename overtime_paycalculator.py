hour = int(input('number of hours worked?'))
rate = int(input('hourly rate?'))
if hour>40:
    overtime = hour - 40
    new_rate = rate * 1.5
    extra_pay = overtime * new_rate
    normal_pay = 40 * rate
    print('normal_pay:',normal_pay)
    print('extra_pay:',extra_pay)
    total = normal_pay + extra_pay
    print('total:',total)
else:
    pay = hour * rate
    print('pay:',pay)

