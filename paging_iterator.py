
class Paginator:

    def __init__(self, data: list, page_size: int):
        if page_size <= 0:
            raise ValueError("page_size must be greater than 0")

        self.data = data
        self.page_size = page_size

    def __iter__(self):
        return PaginatorIterator(self.data, self.page_size)


class PaginatorIterator:
    def __init__(self, data: list, page_size: int):
        self.data = data
        self.page_size = page_size
        self.current_index = 0  # стан

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.data):
            raise StopIteration

        start = self.current_index
        end = start + self.page_size

        page = self.data[start:end]

        self.current_index = end

        return page

data = [1, 2, 3, 4, 5, 6, 7]

paginator = Paginator(data, 3)

for page in paginator:
    print(page)