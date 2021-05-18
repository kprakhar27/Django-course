def print_fancy_name(prefix):
    try:
        while True:
            name = (yield)
            print(prefix + ':' + name)
    except GeneratorExit:
        print('Done !')

co = print_fancy_name('cool')
next(co)
co.send('kumar')
co.send('prakhar')