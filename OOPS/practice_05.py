class A:
    def f1(self): print('A')
class B:
    def f2(self): print('B')
class C(A,B): pass
C().f1();C().f2()