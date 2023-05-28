"""" """
import subprocess


def method_name_decorator(function):
    """The decorator that displays a message in the console with the name
    of the method before calling it. """

    def print_name(*args, **kwargs):
        print(f"Calling method: {function.__name__}")
        return function(*args, **kwargs)

    return print_name


def pylint_decorator(function):
    """ The decorator, using the subprocess module, launches the console command
    "pylint, nazvafaylu" where the file name is the file in which the method is located."""

    def pylint(*args, **kwargs):
        module_name = function.__module__
        file_name = module_name.replace(".", "/") + ".py"
        command = f"pylint {file_name}"
        subprocess.run(command, check=True)
        return function(*args, **kwargs)

    return pylint