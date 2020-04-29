# Task 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
# def stop_words(words: list):
#     pass
#
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

def stop_words(decorator_arg1):
    print("Я создаю декораторы! И я получил следующие аргументы:",
        decorator_arg1)
    def my_decorator(func):
        print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
                decorator_arg1)
        def wrapped(function_arg1):
            print ("Я - обёртка вокруг декорируемой функции.\n"
                    "И я имею доступ ко всем аргументам\n"
                    "\t- и декоратора: {0}\n"
                    "\t- и функции: {1}\n"
                    "Теперь я могу передать нужные аргументы дальше"
                    .format(decorator_arg1,
                            function_arg1))
            f = func(function_arg1).split()
            lst = []
            for words in f:
                if words in decorator_arg1:
                    lst.append('*')
                else:
                    lst.append(words)
            changed_lst = " ".join(lst)
            return changed_lst
        return wrapped
    return my_decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW !"

print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve drinks pepsi in his brand new BMW!"
