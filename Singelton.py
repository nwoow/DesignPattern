class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def get_data(self):
        return self.data

# Example usage:
singleton1 = Singleton()
singleton1.add_data("First data")

singleton2 = Singleton()
singleton2.add_data("Second data")

print(singleton1.get_data())  # Output: ['First data', 'Second data']
print(singleton2.get_data())  # Output: ['First data', 'Second data']

# Check if singleton1 and singleton2 are the same instance
print(singleton1 is singleton2)  # Output: True
