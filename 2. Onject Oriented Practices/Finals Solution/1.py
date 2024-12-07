class Singleton:
    _instance = None

    def __new__(cls):
        # __new__ is a special method in Python called before __init__.
        # It is responsible for creating a new instance of a class.
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example usage:
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(singleton_instance1 is singleton_instance2)  # Output: True
