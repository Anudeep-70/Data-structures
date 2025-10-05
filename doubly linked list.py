class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    
    def display(self):
        head=self.head
        if head is None:
            print("Linked list is empty")
            return
        a=[]
        while head:
            a.append(head.data)
            head=head.next
        return a
    
    def insert_at_beginning(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        self.head.prev=new
        new.next=self.head
        self.head=new
    
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        head=self.head
        while head.next:
            head=head.next
        head.next=new
        new.prev=head

    def insert_at_pos(self,data,pos):
        new=Node(data)
        if pos==1:
            if self.head is None:
                self.head=new
                return
            self.head.prev=new
            new.next=self.head
            self.head=new
        c=1
        head=self.head
        while head and c<pos-1:
            c+=1
            head=head.next
        if head is None:
            print("out of boundary")
            return
        new.next=head.next
        head.next=new
        new.prev=head
    
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None

    def delete_at_end(self):
        head=self.head
        if head is None:
            print("Linked list is empty")
            return
        if head.next is None:
            l.delete_at_beginning()
            return
        while head.next.next:
            head=head.next
        head.next=None

    def delete_val(self,val):
        head=self.head
        if head is None:
            print("Linked list is empty")
            return
        while head:
            if head.data==val:
                if head.prev is None and head.next is None:
                    self.head=None
                    return
                if head.prev is None:
                    self.head=head.next
                    head.next.prev=None
                    return
                if head.next is None:
                    head.prev.next=None
                    return
                head.prev.next=head.next
                head.next.prev=head.prev
                return
            head=head.next
        print("No value")
    def sort_dll(self):
        arr=l.display()
        arr.sort()
        self.head=None
        for i in arr:
            l.insert_at_end(i)
            
l=dll()
arr=[3,2,1]

for i in arr:
    l.insert_at_end(i)
print(l.display())

l.insert_at_beginning(4)
print(l.display())

l.insert_at_end(0)
print(l.display())

l.delete_at_beginning()
print(l.display())

l.delete_at_end()
print(l.display())

l.sort_dll()
print(l.display())
