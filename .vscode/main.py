# class Hero:
#     def __init__(self, name, position):
#         self.__name = name
#         self.__position = position 

#     # def serang(self, bunuh):
#     #     self.attack = print("serang" + bunuh)

#     # def diserang(self, bertahan):
#     #     self.bertahan = print("serang" + bertahan)
#     @property
#     def getname(self):
#         return self.__name
#     @property
#     def getposition(self):
#         return self.__position

#     @getname.setter
#     def name(self, newname):
#      self.__name = newname

#     @getposition.setter
#     def position(self, newposition):
#      self.__position = newposition

# hero1 = Hero("bobiboy", "pahlawan")

# print(hero1.name)
# print(hero1.getposition)
# hero1.name = "gopal"
# hero1.position = "penjahat"
# print(hero1.name)
# print(hero1.getposition)
# # abstrac, dekorator, megic. multipke haritage   (codeium)

# class Kapal:
#     def __init__(self, nama, Level_baterai, mode_operasi):
#         self.__nama = nama
#         self.Level_baterai = Level_baterai
#         self.mode_operasi = mode_operasi
    
#     @property
#     def nama(self):
#         return self.__nama
    
#     @nama.setter
#     def nama(self, newnama):
#         self.__nama = newnama
    
#     def Level_baterai(self, Level_baterai):
#         if 0 <= Level_baterai <= 100:
#             self.Level_baterai = Level_baterai
#         else:
#             print("Level baterai tidak valid")

#     def operasi(self, mode_operasi):
#         if mode_operasi == "operasi":
#             self.mode_operasi = mode_operasi
#         elif mode_operasi == "manual":
#             self.mode_operasi = mode_operasi
#         else:
#             print("Mode operasi tidak valid")
#         self.mode_operasi = mode_operasi

#     def info(self):
#         print(f"Nama Kapal: {self.__nama}")
#         print(f"Level Baterai: {self.Level_baterai}")
#         print(f"Mode Operasi: {self.mode_operasi}")


# kapal1 = Kapal("Kapal Tanker 1", 20, "operasi")
# kapal2 = Kapal("Kapal Penumpang 2", 30, "jancuk")
# kapal1.info()
# kapal2.info
# kapal2.nama = "Kapal Penumpang 3"
# kapal2.info()

#singly linked list
# class Node:
#     def __init__(self, data, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = None
    
#     def __str__(self):
#         return str(self.data)
    

# class LinkedList:
#     def __init__(self, root=None):
#         self.root = None
#         self.size = 0
    
#     def addNode(self, data):
#         new_node = Node(data)
#         if self.root is None:
#             self.root = new_node
#         else:
#             current = self.root
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current
            
#         self.size += 1
        
#     def findNode(self, data):
#         current = self.root
#         while current is not None:
#             if current.data == data:
#                 return current
#             current = current.next
#         return None

#     def deleteNode(self, data):
#         current = self.root
#         while current is not None:
#             if current.data == data:
#                 if current.prev is not None:
#                     current.prev.next = current.next
#                 else:
#                     self.root = current.next
#                 if current.next is not None:
#                     current.next.prev = current.prev
#                 self.size -= 1
#                 return True
#             current = current.next
#         return False

#     def printList(self):
#         current = self.root
#         while current is not None:
#             print(current.data, end="->")
#             current = current.next
#         print("None")
    
# nodenode = LinkedList()
# nodenode.addNode("A")
# nodenode.addNode("B")
# nodenode.addNode("C")
# nodenode.addNode("D")
# nodenode.addNode("E")
# nodenode.printList()
# nodenode.deleteNode("C")
# nodenode.printList()
    
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.last = root
        self.size = 0
    
    def addNode(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.root
            self.last = new_node
        
        self.size += 1
    
    def removeNodeDLL(self, data):
        current = self.root

        while current is not None:
            if current.dataNode == data:
                # Jika node yang dihapus adalah root (node pertama)
                if current == self.root:
                    self.root = current.next
                    if self.root:  # Jika masih ada node setelahnya
                        self.root.prev = None
                    else:
                        self.last = None  # Jika list menjadi kosong
                    
                # Jika node yang dihapus adalah node terakhir
                elif current == self.last:
                    self.last = current.prev
                    self.last.next = None
                
                # Jika node di tengah
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1  # Kurangi ukuran list
                return "Data was successfully removed"

            current = current.next

        return "Data was not found"
    
    def printList(self):
        current = self.root
        while current is not None:
            print(current.data, end="<->")
            current = current.next
        print("None")

nodenode = LinkedList()
nodenode.addNode("A")
nodenode.addNode("B")
nodenode.addNode("C")
nodenode.addNode("D")
nodenode.addNode("E")
nodenode.printList()

nodenode.removeNode("C")
nodenode.printList()
 