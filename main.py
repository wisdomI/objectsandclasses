class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        
    def change_name(self, name):
        print(f'{self.name} is a mentor')
    def change_age(self, age):
        print('He is', str(int(self.age)), 'years old')
    def add_track(self, track):
        print(f'His track is {self.track}')
    def get_score(self, score):
        print('His score is', str(float(self.score)))

    


Peter = Student('Peter', 34, 'UI/UX', 60.9)
Bob = Student("Bob", 26, ["FE","BE"],20.90)

print(Bob.name)
print(Bob.age)
print(Bob.track)
print(Bob.score)

# Expected methods
Peter.change_name("Peter")
Peter.change_age(34)
Peter.add_track("UI/UX")
Peter.get_score(60.9)
