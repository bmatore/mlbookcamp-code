class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)
        
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
        
    def method2(self, someString):
        print("anotherClass method2 " + someString)
        
def main():
    c = myClass()
    c.method1()
    c.method2("Blessing")
    
    c1 = anotherClass()
    c1.method1()
    c1.method2("Matore")
    

    
if __name__ == '__main__':
    main()