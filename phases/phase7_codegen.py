"""
PHASE 7: Target Code Generation (Assembly)
Generates assembly code from integer literals and operations
"""


def generate_assembly(literals):
    """
    Generate assembly code from integer literals.
    
    Args:
        literals: List of tuples (name, type) where name is the literal
                 and type is "INT" or "INT_HEX"
    
    Returns:
        List of assembly instructions
    """
    code = []
    base = 2000
    regs = [f"R{i+1}" for i in range(len(literals))]
    
    code.append("; ===== Integer Literal Assembly Code =====")
    
    for i, (name, lit_type) in enumerate(literals):
        # Convert to decimal value
        val = int(name, 16) if lit_type == "INT_HEX" else int(name, 10)
        
        # Generate assembly
        code.append(f"")
        code.append(f"; Load {lit_type} literal {name} = {val} (decimal)")
        code.append(f"MOV {regs[i]}, #{name:<10}")
        code.append(f"STORE {regs[i]}, [{base + i}]")
    
    code.append(f"")
    code.append("; ===== End of Code =====")
    return code


def generate_assembly_operation(operands, op="+"):
    """
    Generate assembly code for operations on integer literals.
    
    Args:
        operands: List of tuples (name, type)
        op: Operation string ("+", "-", "*", "/")
    
    Returns:
        List of assembly instructions
    """
    code = []
    base = 2000
    regs = [f"R{i+1}" for i in range(len(operands))]
    result_reg = f"R{len(operands)+1}"
    
    code.append("; ===== Integer Literal Operation Assembly Code =====")
    
    # Load operands
    for i, (name, lit_type) in enumerate(operands):
        val = int(name, 16) if lit_type == "INT_HEX" else int(name, 10)
        code.append(f"")
        code.append(f"; Load operand {i+1}: {name}")
        code.append(f"MOV {regs[i]}, #{name}")
        code.append(f"STORE {regs[i]}, [{base + i}]")
    
    # Perform operation
    code.append(f"")
    code.append(f"; Perform operation: {operands[0][0]} {op} {operands[1][0]}")
    
    if op == "+":
        code.append(f"ADD {result_reg}, {regs[0]}, {regs[1]}")
    elif op == "-":
        code.append(f"SUB {result_reg}, {regs[0]}, {regs[1]}")
    elif op == "*":
        code.append(f"MUL {result_reg}, {regs[0]}, {regs[1]}")
    elif op == "/":
        code.append(f"DIV {result_reg}, {regs[0]}, {regs[1]}")
    
    code.append(f"STORE {result_reg}, [{base + len(operands)}]")
    
    code.append(f"")
    code.append("; ===== End of Code =====")
    return code


if __name__ == "__main__":
    print("Example 1: Load integer literals")
    lits = [("42", "INT"), ("0xFF", "INT_HEX"), ("007", "INT")]
    print("\n".join(generate_assembly(lits)))
    
    print("\n\nExample 2: Operation on literals")
    operands = [("42", "INT"), ("0xFF", "INT_HEX")]
    print("\n".join(generate_assembly_operation(operands, "+")))
