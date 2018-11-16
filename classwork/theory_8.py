# unpack
def add_1(a=0, b=0):
    return a + b


def add_2(**kwargs):
    t = 0
    for i, j in kwargs.items():
        t += j
    return t


d = {'a': 2, 'b': 3}
print(add_1(2, 3))
print(add_1(**d))
print(add_2(**d))

# iter

a = [1, 2, 3]
b = iter(a)
print(b)  # <list_iterator object at 0x7f1a399b5d68>

# print(next(a))  # TypeError: 'list' object is not an iterator
print(next(b))  # 1

for i in b:
    print(i)  # 2 3

# print(next(b))  # error StopIteration

# comprehension generator
a = [x*2 for x in [1,2,3]]
print(a)  # [2, 4, 6]
a = (x*2 for x in [1,2,3])
print(a)  # <generator object <genexpr> at 0x7f3374b09c50>
a = tuple(x*2 for x in [1,2,3])
print(a)  # (2, 4, 6)


with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line)

# decorator
def bread(func):
   def wrapper():
      print("</------\>")
      func()
      print("<\______/>")
   return wrapper

def ingradients(func):
   def wrapper():
      print("Салат")
      func()
      print("Помидоры")
   return wrapper

@bread
@ingradients
def sandwich(food='Ветчина'):
   print(food)


print(sandwich())



#! coding: utf-8

# decorator

def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё
    def wrapper():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    return wrapper


def stand_alone_function():
    print("Простая функция.")

decorated = my_shiny_new_decorator(stand_alone_function)


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Другая простая функция")

another_stand_alone_function()



def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)
        print("Послевсего напечатаем")
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)


print_full_name("Саша", "Мороз")
