from pyscript import document
from mpmath import mp

# output_div.innerText = digits

def isNum(s):
    try:
        s = int(s)
        if s >= 2 and s <= 1500: return True
        else: return False
    except ValueError:
        return False

def getpi(event):
    input_number = document.querySelector("#digits")
    digits = input_number.value
    output_div = document.querySelector("#output")
    pi_div = document.querySelector("#pi")
    
    if isNum(digits):
        mp.dps = digits
        output_div.innerText = f"Here's your {digits} digits of pi:"
        pi_div.innerText = f"{mp.pi}"
    else:
        output_div.innerText = f"Please enter a valid number that is more than 1 and less than 1500."