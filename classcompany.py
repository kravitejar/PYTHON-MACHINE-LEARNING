class company(object):
    
    def __init__(self,id,name,sal,percent):
        self.id=id
        self.name=name
        self.sal=sal
        self.percent=percent
        
    def bonus(self):
        self.sal=self.sal+(self.sal*(self.percent/100))
        return self.sal
    
    def decr(self):
        self.sal=(self.sal-(self.sal*(self.percent/100)))
        return self.sal
    
        



        
