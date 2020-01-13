from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    return {
        '+' :lambda a,b: a + b,
        '-' :lambda a,b: a - b,
        '/' :lambda a,b: a / b,
        '*' :lambda a,b: a * b,
        '**':lambda a,b: a ** b
        }[operation](a,b)

if __name__ == '__main__':
    while 1:
        try:
            a = int(input('Введите целое число (a): '))
            b = int(input('Введите целое число (b): '))
            operation = input('Введите операцию (+ - / * **): ')

            print('Результат:', calculator(a, b, operation))

        except ValueError:
            print('Упс! Какое-то левое число.')
        except KeyError:
            print('Упс! Не знаю такой операции.')
        except ZeroDivisionError:
            print('Упс! Нам на ноль делить не разрешают.')
        except KeyboardInterrupt:
            print()
            quit()
