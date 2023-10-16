
#%%
from PySide6.QtCore import QObject, Signal, Slot, Property

class TestClass(QObject):
    """
    A class to test the signals and slots mechanism.
    """
    p0Changed:Signal = Signal()
    @Property(str, notify=p0Changed)
    def p0(self) -> str:
        return self._p0
    @p0.setter
    def p0(self, value:str) -> None:
        self._p0 = value
        self.p0Changed.emit()

    p1Changed:Signal = Signal()
    @Property(str, notify=p1Changed)
    def p1(self) -> str: 
        return self._p1
    @p1.setter
    def p1(self, value:str) -> None:
        self._p1 = value
        self.p1Changed.emit()

    p2Changed:Signal = Signal()
    @Property(str, notify=p2Changed)
    def p2(self) -> str:
        return self._p2
    @p2.setter
    def p2(self, value:str) -> None:     
        self._p2 = value
        self.p2Changed.emit()

    p3Changed:Signal = Signal()
    @Property(str, notify=p3Changed)
    def p3(self) -> str:
        return self._p3
    @p3.setter
    def p3(self, value:str) -> None:
        self._p3 = value
        self.p3Changed.emit()

# %%
TestClass.__dict__
# %%
setattr(TestClass, "p10086", property(TestClass.p0.fget, TestClass.p0.fset))
# %%
TestClass.__dict__
# %%
cls = TestClass
import types
new_class = types.new_class("TestClass", cls.__bases__, exec_body=lambda ns:ns.update(cls.__dict__))
new_class.__dict__
# %%
TestClass is new_class
#%%
del TestClass
TestClass
# %%
import sys
del TestClass
sys.modules["__main__"].__dict__["TestClass"]  = new_class
print(TestClass is new_class)
TestClass
# %%
TestClass.__dict__
