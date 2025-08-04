# TYP E S  D E FIN I TION S   IN  PYTHON  

'''
Type hints are added using the colon (:) syntax for variables and the -> syntax for 
function return types.
'''

n : int = 5

name : str = "ankit"

def sum(a:int, b:int) -> int:
    return a+b


print(sum(7,2))


# Variable type hint 
age: int = 25 
 
# Function type hints 
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 
 
# Usage 
print(greeting("Alice"))  # Output: Hello, Alice!



