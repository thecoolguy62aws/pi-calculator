import sys, time
def typePrint(text, delay=0.05, newlines=1):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    for _ in range(newlines):
        print()