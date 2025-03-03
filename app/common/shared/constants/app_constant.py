from dataclasses import dataclass

@dataclass(frozen=True)
class AppConstants:
    
    @dataclass(frozen=True)
    class Page:
        INDEX_DEFAULT: int = 100
        SIZE_DEFAULT: int = 10
        