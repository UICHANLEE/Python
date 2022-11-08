# Attribute 추가는 __init__, self로 추가

# __특수한 예약 함수나 변수 그리고 함수명 변경(맨글링)으로 사용

class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % \
            (self.back_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. My back number is %d" % \
            (self.name, self.back_number)

# self를 추가해야만 class 함수로 인정됨

Uichan = SoccerPlayer("Uichan", "CB", 5)
Uichan.back_number = 4


class Note(object):
    def __init__(self, content=None):
        self.content = content

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = ""

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content

class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당페이지는 존재하지 않습니다")
    
    def get_number_of_pages(self):
        return len(self.notes.keys())
            
# inheritance. polymorphism, Visibility
# inheritance = 부모클래스로부터 속성과 메소드를 물려받은 자식 클래스를 생성하는것
# polymorphism = 다형성, 같은 이름의 메소드의 내부 로직을 다르게 작성 => 같은 개념이지만 다른 행동을 하는 것(raise)
# __ private 개체 생성
# @property = Property Decorater 내부에서는 접근 가능
# Visibility = 객체의 정보를 볼 수 있는 레벨을 조절하는 것
# super = 부모클래스를 상속
# Encapsulation = 클래스 간 간섭/정보공유의 최소화

# Decorate : 복잡한 클로져 함수를 간단하게
"""
First-class

- 일등함수 또는 일급 객체
- 변수나 데이터 구조에 할당이 가능한 객체
- 파라미터로 전달이 가능 + 리턴 값으로 사용

Inner Function

- 함수 내에 또 다른 함수가 존재
- closures : inner function을 return값으로 반환


"""



