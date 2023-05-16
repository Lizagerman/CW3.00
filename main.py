from utils import get_data, filter_data, sort_data, format_data


def main():
    #print('Получение данных из файла... ', end='')
    data = get_data()
    #print('OK')

    #print('Фильтрация транзакций... ', end='')
    data = filter_data(data)
    #print('OK')

    #print('Сортировка транзакций... ', end='')
    data = sort_data(data)
    #print('OK')

    for elem in format_data(data):
        print(elem)


if __name__ == "__main__":
    main()

