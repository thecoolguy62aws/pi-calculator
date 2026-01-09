from pyscript import document
from decimal import Decimal, getcontext
#
# output_div.innerText = digits

def isNum(s):
    try:
        s = int(s)
        if s >= 1 and s <= 5000000: return True
        else: return False
    except ValueError:
        return False

def getpi(event):
    input_number = document.querySelector("#digits")
    digits = input_number.value
    output_div = document.querySelector("#output")
    pi_div = document.querySelector("#pi")
    
    if isNum(digits):
        getcontext().prec = int(digits)

        if digits == 1 or digits == "1":
            pi = "3"
        else:
            pi = sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) for k in range(100))
        formatteddigits = str("{:,}".format(int(digits)))
        if int(digits) > 1:
            output_div.innerText = f"Here's your {formatteddigits} digits of pi:"
        else:
            output_div.innerText = f"Here's your {formatteddigits} digit of pi:"
        pi_div.innerText = f"{pi}"
    elif str(digits) != "":
        output_div.innerText = f"Please enter a valid number that is at least 2 and at most 5,000,000."
        pi_div.innerText = ""