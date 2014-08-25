__author__ = 'vivek.gour'


def makebold(fn):
    def g():
        return "<b>" + fn() + "<b/>"
    return g

def makeitalic(fn):
    def g():
        return "<i>" + fn() + "<i/>"
    return g

# @makeitalic
# @makebold
def vivek():
    return 'i am a good boy'



vivek = makebold(makeitalic(vivek))
print vivek()