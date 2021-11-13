from dataclasses import dataclass as component

@component
class Transform:
    x: float = 0
    y: float = 0
    sx: float = 1
    sy: float = 1
    theta: float = 0
    
@component
class Char:
    char: str = ''
    size: int = 12
    
