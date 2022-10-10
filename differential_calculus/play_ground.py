import datetime
import os
import inspect
#Identifying argument values in a function and preloading of arguments

#Preloading of arguments
import functools
def load_file(file, base_path='/', mode='rb'):
    return open(os.path.join(base_path, file), mode)

#our new function with new callables will be
load_writable=functools.partial(load_file, mode='w') #mode is changed from rb to w
#f = load_writable("example.txt")

#Introspection, identifying argument values
def example(a: int, b=1, *c, d, e=2, **f) -> str:
    pass

print(f"Our function's argument list: {inspect.getfullargspec(example)} \n\n")


def get_arguments(func, args, kwargs):
    """
        Given a function and a set of arguments, return a dictionary of argument values that will be sent to the function
    """
    arguments = kwargs.copy()
    spec = inspect.getfullargspec(func)
    arguments.update(zip(spec.args, args)) #adding positional arguments
    
    if spec.defaults: #configuring the defaults from func that were not overridden by the arguments provided.
        for i, name in enumerate(spec.args[-len(spec.defaults):]):
            if name not in arguments:
                arguments[name] = spec.defaults[i]
                
    if spec.kwonlydefaults:
        for name, value in spec.kwonlydefaults.items():
            if name not in arguments:
                arguments[name] = value
    
    return arguments

print(get_arguments(example, (1,), {"f": 4}))