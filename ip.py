import re

def t(__: str):
    ___ = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    
    with open(__, 'r', encoding='utf-8') as file:
        _ = file.readlines()
        
        for _____, tser in enumerate(_, start=1):
            _______ = ___.search(tser)
            if _______:
                print(f"Ligne {_____}: {tser.strip()} (IP: {_______.group(0)})")

if __name__ == "__main__":
    __ = 'tfd.txt'
    t(__)
