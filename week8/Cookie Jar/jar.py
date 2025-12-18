class Jar:

    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0
        if self.capacity < 0:
            raise ValueError("Negative value added")

    def __str__(self):
        cookies = ""
        if self.size == 0:
            return ""
        else:
            for cookie in range(self.size):
                cookies += "🍪"
        return cookies

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError("Maximum capacity exceeded")
        print(f"{n} cookies added")
        return self._size

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies inside")

        self._size -= n
        print(f"{n} cookies eatten")
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Negative value added")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError("Maximum capacity exiceeded")
        self._size = n

def main():
    cookies = Jar()
    cookies.deposit(10)
    cookies.deposit(1)
    cookies.withdraw(5)
    cookies.withdraw(3)
    print(cookies)

if __name__ == "__main__":
    main()
