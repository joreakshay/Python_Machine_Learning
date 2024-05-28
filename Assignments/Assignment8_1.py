class   BookStore:
    NoOfBooks=0
    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print("{0} by {1}. No fo books : {2}".format(self.Name,self.Author, BookStore.NoOfBooks))

def main():
    Obj1=BookStore("Linux system programming","Robert Love")
    Obj1.Display()
    Obj2=BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__=="__main__":
    main()
