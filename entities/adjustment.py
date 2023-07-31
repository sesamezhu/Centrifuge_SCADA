import string
import time
import typing
from dataclasses import dataclass, asdict, fields, replace, field


@dataclass
class Test:
    a: int = 0


@dataclass
class Adjustment:
    instrument_id: int = 0
    pressure: float = 0.0
    begin: float = time.time()
    end: float = 0.0
    effect: bool = False
    success: bool = False
    a: Test = Test()
    aa: typing.List[int] = field(default = None)


# aa = [1, 2]
a = Adjustment()
j = {"end": 1, "aa":[Test(),Test(a='bb')]}
b = replace(a, **j)
print(b, j, asdict(b))
print(replace(a,**asdict(b)))