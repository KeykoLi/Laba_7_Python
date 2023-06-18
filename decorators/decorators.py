"""" """
import os
import subprocess
import logging


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
        subprocess.run(command, text=True)
        return function(*args, **kwargs)

    return pylint


def logged(exception, mode):
    """
    The decorator logged using the logging module

    Arguments:
        exception
        mode (console / file)
            In console mode, logging takes place in the console,
            and in file mode, logging is written to a file.

    """

    def logged_decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(f'Exception: {e}')
                elif mode == "file":
                    file = "py_log.txt"
                    if os.path.exists(file):
                        os.remove(file)
                    logging.basicConfig(filename=file, level=logging.ERROR, filemode="w",
                                        format="%(asctime)s %(levelname)s %(message)s")
                    logging.error(f'Exception: {e}', exc_info=True)
                else:
                    raise ValueError("Invalid logging mode. Please choose 'console' or 'file'.")

        return wrapper

    return logged_decorator
