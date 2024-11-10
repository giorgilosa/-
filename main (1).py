
#######################
#task1
###


# Node კლასი, რომელიც წარმოადგენს ცალკეულ ელემენტს დაკავშირებულ სიაში
class Node:
    def __init__(self, data=None):
        # ინიციალიზაცია: ახალი ნოდის შექმნა მონაცემებით და შემდეგ ნოდის მითითების none-ით
        self.data = data
        self.next = None  # მიუთითებს შემდეგ ნოდზე, საწყისად არის None, რადგან ახალი ნოდია

#  კლასი, რომელიც მართავს ნოდებს და მოიცავს მეთოდებს, როგორიცაა დამატება, წაშლა და ჩვენება
class LinkedList:
    def __init__(self):
        #  ცარიელი სიის სათავე,  საწყისად არის None
        self.head = None

    def append(self, data):
        #  ახალი ნოდის შექმნა მიღებული მონაცემებით
        new_node = Node(data)
        #  თუუ სია ცარიელია (head არის None), სათავეს  ახალ ნოდი გახდა
        if self.head is None:
            ### სათავეს ქმნის ახალ ნოდზე, რადგან ეს არის პირველი ელემენტი
            self.head = new_node
            return

        #  სიაში ბოლო ნოდის მოძებნა
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # გადადის შემდეგ ნოდზე, სანამ last_node.next არ გახდება None

        # ბოლო ნოდის შემდეგი  ახალ ნოდზე მითითებაა, რითაც იგი ემატება სიას
        last_node.next = new_node

    def remove_at(self, index):
        #  ამოწმებსს, არის თუ არა ინდექსი ვალიდური ან სია არისვ ცარიელი
        if index < 0 or self.head is None:
            return  # არაფერი აკეთე ბს, თუ ინდექსი არასწორია ან სია ცარიელია

        # ამ პიირობის შემთხვევაში ვშლით სიის სათავის ანუ ნოდს
        if index == 0:
            # სათავის  შემდეგ ნოდზე გადატანა ხდება, რის შედეფგადაც იშლება current head
            self.head = self.head.next
            return

        # სიაში გადასვლა იმ ნოდამდე რომელიც არის წასაშლელის წინ
        current_node = self.head
        current_position = 0

        # გადადის, სანამ მივა იმ ნოდამდე, რომელიც არის წასაშლელის წინ
        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        # ნაბიჯი 4: თუ შემდეგი ნოდი არსებობს, ხდბეა მისი გამოტოვება და წაშლა
        if current_node.next:
            current_node.next = current_node.next.next  # წაშლისას გამოტოვებს ნოდს

    def display(self):
        #  სიის სათავიდან  თითოეული ნოდის მონაცემის აჩვენე ბს
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')  # მონაცემების ჩვენება, რომელსაც მიჰყვება ისარი ანუ გადასვლაა შემდგომ ნოდზე
            current_node = current_node.next  # გადადის სიის შემდეგ ნოდზე

        print()  # ახალი ხაზზე გადადის და მონაცემებს აჩვენებს

#
linked_list = LinkedList()

# ნოდების დამატება სიაშიი
linked_list.append(50)  # ნოდი ინდექს 0ზე
linked_list.append(15)  # ნოდი ინდექს 1ზე
linked_list.append(20)  # ნოდი ინდექს 2ზე
linked_list.append(11)  # ნოდი ინდექს 3ზე
linked_list.append(5)   # ნოდი ინდექს 4ზე
linked_list.append(25)  # ნოდი ინდექს 5ზე

# საწყისი სიის ჩვენება
linked_list.display()  # აჩვნებს: 50 -> 15 -> 20 -> 11 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 2 (მონაცემები 20) და აჩვენებს ახალ სიას.
linked_list.remove_at(2)
linked_list.display()  # აჩვნებს: 50 -> 15 -> 11 -> 5 -> 25 ->

# ისევ ნოდის წაშლა ინდექსზე 2 (მონაცემები 11) და აჩვენებს ახალ სიას.
linked_list.remove_at(2)
linked_list.display()  # აჩვნებს: 50 -> 15 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 0 (მონაცემები 50) აჩვენებს ახალ სიას.
linked_list.remove_at(0)
linked_list.display()  # აჩვნებს: 15 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 2 (მონაცემები 25) და აჩვენებს ახალ სიას.
linked_list.remove_at(2)
linked_list.display()  # აჩვნებს: 15 -> 5 ->

#####
####task2
#########################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def remove_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def insert_at(self, index, data):
        if index < 0:
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print()

linked_list = LinkedList()
linked_list.append(5)
linked_list.append(10)
linked_list.append(15)

linked_list.show()
linked_list.remove_value(10)
linked_list.show()
linked_list.insert_at(1, 12)
linked_list.show()
