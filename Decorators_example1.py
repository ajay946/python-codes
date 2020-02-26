def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the original function')

        original_func()

        print('some extra code after original function')
    return wrap_func()

@new_decorator
def func_need_decorator():
    print('I WANT TO BE A DECORATOR')

func_need_decorator()