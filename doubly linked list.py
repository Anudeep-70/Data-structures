class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    
    def insert_at_beghinning(self,data):
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
    
    def display(self):
        head=self.head
        if head is None:
            print("empty")
            return
        a=[]
        while head:
            a.append(head.data)
            head=head.next
        return a
    
    def delete(self,val):
        head=self.head
        if head is None:
            print("No dll")
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
arr=[5,4,3,2,1]

for i in arr:
    l.insert_at_end(i)
print(l.display())

l.insert_at_pos(4,6)
print("Added element 4 to 6th position :\n",l.display())

l.delete(4)
print("Deleted value 4 :\n",l.display())

l.sort_dll()
print("sorted doubly linked list :\n",l.display())