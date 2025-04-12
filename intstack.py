##########################################
# Реализация стека на основе списка list #
##########################################

def create():
    """ Создаем стек """
    return list()  # Возвращаем пустой список


def push(x, stack):
    """ Заносим x в стек """
    stack.append(x)


def pop(stack):
    """ Извлекаем и возвращаем верхний элемент стека.
        Стек не должен быть пустым.
    """
    return stack.pop()


def empty(stack):
    """ Если стек пуст, возвращаем True, иначе False """
    return len(stack) == 0


def top(stack):
    """ Возвращаем верхний элемент непустого стека.
        Стек остается без изменений
    """  
    return stack[-1]


def depth(stack):
    """ Глубина стека """
    return len(stack)  # Возвращаем длину списка


def print_stack(stack):
    """ Выводим содержимое стека """
    if empty(stack):
        print("Стек пуст")
    else:
        print(stack)


# Проверка стека
if __name__ == "__main__":
    # Создаем пустой стек
    stack = create()

    print_stack(stack)

    # Добавляем в стек числа 10, 20, 30
    push(10, stack)
    push(20, stack)
    push(30, stack)
    print("В стеке:")
    print_stack(stack)

    x = top(stack)  # Число на вершине стека
    print("В вершине стека", x)

    n = depth(stack)  # Глубина стека
    print("Глубина стека:", n)

    # Извлекаем из стека все числа
    while not empty(stack):
        print("Извлекаем", pop(stack))

    print_stack(stack)
