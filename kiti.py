# # Library title,genre,location
# # cataolog,book,magazine,audiobook,display
# from abc import ABC, abstractmethod
#
#
# class LibraryItem(ABC):
#     count = 0
#
#     def __init__(self, title, genre):
#         self.title = title
#         self.genre = genre
#         LibraryItem.count += 1
#
#     @abstractmethod
#     def locate(self):
#         pass
#
#     @classmethod
#     def count_get(cls):
#         return cls.count
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#
# class Book(LibraryItem):
#     def __init__(self, title, genre, isbn, authors):
#         super().__init__(title, genre)
#         self.isbn = isbn
#         self.authors = authors
#
#     def locate(self):
#         return f"Kitoblar bo'limida joy olgan"
#
#     def get_info(self):
#         return f"{self.title} {self.genre} {self.authors}"
#
#
# class Magazine(LibraryItem):
#     def __init__(self, title, genre, volume):
#         super().__init__(title, genre)
#         self.volume = volume
#
#     def locate(self):
#         return f"Jurnallar bo'limida joy olgan"
#
#     def get_info(self):
#         return f"{self.title} {self.genre} {self.volume}"
#
#
# class AudioBook(LibraryItem):
#     def __init__(self, title, genre, time):
#         super().__init__(title, genre)
#         self.time = time
#
#     def locate(self):
#         return f"Audio bo'limida joy olgan"
#
#     def get_info(self):
#         return f"{self.title} {self.genre} {self.time}"
#
#
# class DisplayBook(LibraryItem):
#     def __init__(self, title, genre, type_dvd):
#         super().__init__(title, genre)
#         self.type_dvd = type_dvd
#
#     def locate(self):
#         return f"Displaylar bo'limida joy olgan"
#
#     def get_info(self):
#         return f"{self.title} {self.genre} {self.type_dvd}"
#
#
# class Catalog:
#     def __init__(self):
#         self.books = []
#
#     def add(self, item):
#         self.books.append(item)
#
#     def get_books(self):
#         jami = [item.get_info() for item in self.books]
#         return jami
#
#     def search(self, keyword):
#         jami_list = []
#         for obj in self.books:
#             if obj.title == keyword or obj.genre == keyword:
#                 jami_list.append(obj)
#         javob = [item.locate() for item in jami_list]
#         return javob
#
#
# def brain_stop():
#     cat = Catalog()
#     print("""
#     1 Add book
#     2 Add magazine
#     3 Add audiobook
#     4 Add displaybook
#
#     5 view
#     6 search
#     """)
#     while True:
#         nums = input("Enter your choice: ")
#
#         if nums == "1":
#             title = input("Enter title: ")
#             genre = input("Enter genre: ")
#             isbn = input("Enter ISBN: ")
#             authors = input("Enter authors: ")
#             item = Book(title, genre, isbn, authors)
#             print(item.locate())
#             cat.add(item)
#         elif nums == "2":
#             title = input("Enter title: ")
#             genre = input("Enter genre: ")
#             volume = input("Enter volume: ")
#             item = Magazine(title, genre, volume)
#             print(item.locate())
#             cat.add(item)
#
#         elif nums == "3":
#             title = input("Enter title: ")
#             genre = input("Enter genre: ")
#             time = input("Enter time: ")
#             item = AudioBook(title, genre, time)
#             cat.add(item)
#
#         elif nums == "4":
#             title = input("Enter title: ")
#             genre = input("Enter genre: ")
#             type_dvd = input("Enter type: ")
#             item = DisplayBook(title, genre, type_dvd)
#             cat.add(item)
#             print(item.locate())
#         elif nums == "5":
#             print(cat.get_books())
#         elif nums == "6":
#             keyword = input("Enter keyword: ")
#             print(cat.search(keyword))
#
#
# brain_stop()


from abc import ABC, abstractmethod

class Jurnal(ABC):
    son=0
    def __init__(self,fullname,age,kasbi,time):
        self.fullname=fullname
        self.age=age
        self.kasbi=kasbi
        self.time=time
        Jurnal.son +=1

    @abstractmethod
    def doctor(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @classmethod
    def son_get(cls):
        return son


class Stomatolog(Jurnal):
    def __init__(self,fullname,age,kasbi,time):
        super().__init__(fullname,age,kasbi,time)

    def doctor(self):
        return f"Siz stomstolog ko'rigi yozildingiz,qabul {self.time} boshlanadi"

    def get_info(self):
        return f"{self.fullname} {self.age} {self.kasbi} {self.time}"
    # print(Stomatolog.doctor())

class Travmatolog(Jurnal):
    def __init__(self,fullname,age,kasbi,time):
        super().__init__(fullname,age,kasbi,time)

    def doctor(self):
        return f"siz travmatolog ko'rigiga yozildingiz,qabul {self.time} da boshlanadi"

    def get_info(self):
        return f"{self.fullname} {self.age} {self.kasbi} {self.time}"

    # print(Travmatolog.doctor())

class Lor(Jurnal):
    def __init__(self, fullname, age, kasbi, time):
        super().__init__(fullname, age, kasbi, time)

    def doctor(self):
        return f"siz Lor ko'rigiga yozildingiz,qabul {self.time} da boshlanadi"

    def get_info(self):
        return f"{self.fullname} {self.age} {self.kasbi} {self.time}"
    # print(Lor.doctor())

class Jam:
    def __init__(self):
        self.qabular=[]

    def add(self,item):
        self.qabular.append(item)

    def get_qabul(self):
        jami = [item.get_info() for item in self.qabular]
        return jami

    def search(self, word):
        jami_list = []
        for obj in self.qabular:
            if obj.fullname == word or obj.age == word:
                jami_list.append(obj)
        javob = [item.doctor() for item in jami_list]
        return javob





def ogriq_bormi():
    qabular=Jam()
    print("""
    1-doctor qabuliga yozilish
    2-meni qabularim soni
    3-search
    """)
    while True:
        use=int(input("tanlovingizni kiriting-"))
        if use == 1:
            doc=input("qayisi doctorga yozilmoqchisiz(stomatolog,travmatolig,lor)-")
            name=input("doctorning isim familiyasi-")
            age=input("doctor yoshi-")
            vaqt=input("qaysi vaqtga")
            if doc == "stomatolog":
                patient = Stomatolog(name, age, "stomatolog", vaqt)
            elif doc == "travmatolog":
                patient = Travmatolog(name, age, "travmatolog", vaqt)
            elif doc == "lor":
                patient = Lor(name, age, "lor", vaqt)
            else:
                print("Noto'g'ri doctor nomi!")
                continue

            qabular.add(patient)
            print(patient.doctor())

        elif use==2:
            print(qabular.get_qabul())

        elif use==3:
            word = input("Enter keyword: ")
            print(qabular.search(word))

ogriq_bormi()