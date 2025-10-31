# test_toy_compiler.py
from MiPy import run_toy_code

if __name__ == "__main__":
    code = """x = 2
if x>3
    print("xyz"
"""
    print("Testing PDA-based Python toy compiler:\n")
    run_toy_code(code)
