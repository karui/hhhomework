def cache_decorator(func):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    results = {}
    def wrapper(*args, **kwargs):
        if args not in results:
            results[args] = func(*args, **kwargs)
            print(args, 'сохранено в кэш')
        else:
            print(args, 'взято из кэша')
        return results[args]
    return wrapper
