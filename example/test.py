#%%
import pathlib
import sys
from typing import Optional
from PySide6.QtCore import QByteArray, QObject, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlEngine, qmlRegisterType, QQmlApplicationEngine

from qdataclass import qDataClass

@qDataClass
class TestClass(QObject):
    p0:str
    p1:int
    p2:float

    def __init__(self, parent: QObject = None) -> None:
        # super().__init__(parent)
        super(TestClass, self).__init__(parent)
        self.p0Changed.connect(self.onP0Changed)
        self.p1Changed.connect(self.onP1Changed)
        self.p2Changed.connect(self.onP2Changed)
    
    def onP0Changed(self, value: Optional[str]) -> None:
        print(f"p0 changed to {value}")

    def onP1Changed(self, value: Optional[int]) -> None:
        print(f"p1 changed to {value}")

    def onP2Changed(self, value: Optional[float]) -> None:
        print(f"p2 changed to {value}")



t = TestClass()
t.p0 = "123456"
t.p1 = 123456
t.p2 = 123456.123456
# %%
qmlRegisterType(TestClass, "testclass", 1, 0, "TestClass")

app = QGuiApplication(sys.argv)

# %%
engine = QQmlApplicationEngine()
engine.load(QUrl("qml/main.qml"))
if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec())
# %%
