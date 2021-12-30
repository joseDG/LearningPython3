
from typing import Union

def div1(x: float, y: float) -> Union[float, None]:
    if y == 0:
        return None
    return x / y

from typing import Optional

def div2(x: float, y: float) -> Optional[float]:    # same as above
    if y == 0:
        return None
    return x / y


