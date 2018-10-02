class MathDojo:
    def __init__(self,num):
        self.num = num
    def add(self,arg1,*args):
        if len(args)>0:
            for val in args:
                self.num += val
        self.num += arg1
        return self
    def subtract(self,arg1,*args):
        if len(args)>0:
            for val in args:
                self.num -= val
        self.num -= arg1
        return self
    def result(self):
        return self.num

md = MathDojo(0)
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)        