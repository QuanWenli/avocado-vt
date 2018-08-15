
while True:
    try:
        _input = raw_input
    except NameError:
        _input = input
    in_put = _input("")
    if in_put in ['exit', 'quit']:
        print("Bye")
        break
