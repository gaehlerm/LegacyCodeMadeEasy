from abc import abstractmethod

class Animal:
    def move(self):
        print(f'Animal is moving')

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print(f'Dog is eating meat')

    def move(self):
        print("Dog is running")
        super().move()

dog = Dog()
dog.move()