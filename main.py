from utils import get_data, filter_data, sort_data, format_data


def main():
    data = get_data()

    data = filter_data(data)

    data = sort_data(data)

    for elem in format_data(data):
        print(elem)


if __name__ == "__main__":
    main()

