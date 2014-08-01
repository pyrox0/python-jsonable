from nose.tools import eq_

from ..jsonable import JSONable


def test_jsonable():
    
    class Bar(JSONable):
        __slots__ = ('subherp', 'subderp')
        def initialize(self, subherp, subderp):
            self.subherp = subherp
            self.subderp = subderp
    
    class Foo(JSONable):
        __slots__ = ('herp', 'bars')
        def initialize(self, herp, bars):
            self.herp = herp
            self.bars = list(Bar(b) for b in bars)
        
    herp = 5
    bars = [Bar("string", 334.34), Bar("foo", {"derp": 3.1})]
    foo = Foo(herp, bars)
    
    eq_(foo.herp, herp)
    eq_(foo.bars, bars)
    eq_(foo, Foo(foo))
    eq_(foo, Foo(foo.to_json()))
