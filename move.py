class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.xto = xto
        self.yfrom = yfrom
        self.yto = yto

    def equals(self, other):
        return ((self.xfrom == other.xfrom) and (self.yfrom == other.yfrom) and (self.xto == other.xto) and (self.yto == other.yto))
    
    def to_string(self):
        return "(" + str(self.xfrom) +","+ str(self.yfrom)+") -> (" + str(self.xto)+","+str(self.yto)