#####################################
# Реализация очереди на основе list #
#####################################

def create():
    """ Создаем пустую очередь """
    return list()  # Возвращаем пустой список


def enqueue(x, queue):
    """ Добавляем x в конец очереди """
    queue.append(x)


def dequeue(queue):
    """ Удаляем и возвращаем первый элемент в очереди.
        Очередь не должна быть пустой      
    """
    return queue.pop(0)


def empty(queue):
    """ Если очередь пуста, возвращаем True, иначе False """
    return len(queue) == 0


def length(queue):
    """ Возвращаем длину очереди """
    return len(queue)


def print_queue(queue):
    """ Печатаем содержимое очереди """
    if empty(queue):
        print("Очередь пуста")
    else:
        print(queue)

# Проверка очереди
if __name__ == "__main__":
    # Создаем пустую очередь
    queue = create()
    print_queue(queue)

    # Добавляем в очередь числа 10, 20, 30
    enqueue(10, queue)
    enqueue(20, queue)
    enqueue(30, queue)
    print("В очереди:")
    print_queue(queue)

    n = length(queue)  # Длина очереди
    print("Длина очереди:", n)

    # Извлекаем из очереди все числа
    while not empty(queue):
        print("Извлекаем", dequeue(queue))

    print_queue(queue)
    
