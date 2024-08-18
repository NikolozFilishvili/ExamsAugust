from preloaded import Animal
#import might bug out but it works in codewars
class Cat(Animal):
    def speak(this):
        return f"{this.name} meows."