from collections import OrderedDict
from typing import Any, List

def encode(v: Any) -> str:
    if isinstance(v, int):
        return f'i{v}e'
    
    elif isinstance(v, str):
        return f'{len(v)}:{v}'

    elif isinstance(v, bytes):
        return f'{len(v)}:{v.decode("utf8")}'
    
    elif isinstance(v, list | OrderedDict):
        return f'l{"".join(encode(i) for i in v)}e'
        
    elif isinstance(v, dict):
        out = 'd'
        for key, value in v.items():
            key = encode(key)
            value = encode(value)
            out += f'{key}{value}'
        return out + 'e'
