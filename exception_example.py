from decimal import DivisionByZero


def division(number, divider):
    try:
        return number/divider
    except ZeroDivisionError as ex:
        print("DivisionByZero occurred, Divider can not be Zero")
        print(ex)
    except Exception as ex:
        print("Some exception occurred while performing division")
        print(ex)
    finally:
        print("Finally executed")


r = division(10, 2)
print(r)
