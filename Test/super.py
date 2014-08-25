__author__ = 'vivek.gour'


class ABC(object):
    def printme(self):
        print "Vivek"

class BCD(ABC):
    def printme(self):
        print "Gour"
        super(BCD, self).printme()


a = BCD()
a.printme()