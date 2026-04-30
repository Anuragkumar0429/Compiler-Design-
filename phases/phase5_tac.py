"""
PHASE 5: Intermediate Code Generation
Generates Three-Address Code (TAC) from integer literals
"""


def generate_tac(target, operands, op="+"):
    """
    Generate Three-Address Code for operations on integer literals
    
    Args:
        target: Variable to store result
        operands: List of integer literals
        op: Operator (default: "+")
    
    Returns:
        List of TAC instructions
    """
    tac = []
    temps = []
    
    for i, lit in enumerate(operands):
        # Convert hex or decimal to decimal value
        val = int(lit, 16) if lit.lower().startswith("0x") else int(lit, 10)
        tac.append(f"t{i+1} = {val}")
        temps.append(f"t{i+1}")
    
    if len(temps) >= 2:
        result_temp = f"t{len(operands)+1}"
        tac.append(f"{result_temp} = {temps[0]} {op} {temps[1]}")
        tac.append(f"{target} = {result_temp}")
    elif len(temps) == 1:
        tac.append(f"{target} = {temps[0]}")
    
    return tac


def generate_tac_assignment(target, value):
    """Generate TAC for simple assignment"""
    tac = []
    val = int(value, 16) if value.lower().startswith("0x") else int(value, 10)
    tac.append(f"t1 = {val}")
    tac.append(f"{target} = t1")
    return tac


if __name__ == "__main__":
    print("Example 1: result = 0xFF + 42")
    print("TAC:")
    for line in generate_tac("result", ["0xFF", "42"]):
        print(f"  {line}")
    
    print("\nExample 2: x = 0x1A")
    print("TAC:")
    for line in generate_tac_assignment("x", "0x1A"):
        print(f"  {line}")
