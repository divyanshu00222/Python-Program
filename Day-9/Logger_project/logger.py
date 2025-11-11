import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - Called {func.__name__}\n")
        return func(*args, **kwargs)
    return wrapper
