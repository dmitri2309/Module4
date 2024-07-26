# вызов функции inner_function внутри функции test_function
# def test_function():
#     pass
#     def inner_function():
#         n = 'Я в области видимости функции test_function'
#         print(n)
#     inner_function()
# test_function()

# функцию inner_function за пределами фукнкции test_function вызвать нельзя
# код не работает
def test_function():
    def inner_function():
        n = 'Я в области видимости функции test_function'
        print(n)
inner_function()
