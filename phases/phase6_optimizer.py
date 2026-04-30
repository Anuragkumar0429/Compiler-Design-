"""
PHASE 6: Code Optimization
Performs constant folding and DAG-based basic block optimization
"""

import re
from collections import defaultdict


class DAGNode:
    """Node in a Directed Acyclic Graph (DAG) for basic block optimization"""
    
    def __init__(self, op, operands, node_id):
        self.op = op  # Operation: "const", "var", or operator
        self.operands = operands  # List of operand node IDs
        self.node_id = node_id
        self.var_names = []  # Variables that reference this node
    
    def __repr__(self):
        if self.op == "const":
            return f"const({self.operands[0]})"
        elif self.op == "var":
            return f"var({self.operands[0]})"
        else:
            return f"{self.op}({','.join(str(o) for o in self.operands)})"


class DAGOptimizer:
    """DAG-based optimizer for basic blocks"""
    
    def __init__(self):
        self.nodes = {}
        self.node_counter = 0
        self.value_map = defaultdict(list)  # Maps (op, operands) -> node_id
    
    def add_node(self, op, operands):
        """Add or retrieve a node in the DAG"""
        key = (op, tuple(operands))
        
        if key in self.value_map:
            return self.value_map[key]
        
        node_id = self.node_counter
        self.node_counter += 1
        self.nodes[node_id] = DAGNode(op, operands, node_id)
        self.value_map[key].append(node_id)
        
        return node_id
    
    def build_dag(self, tac_list):
        """Build a DAG from TAC instructions"""
        assignments = {}  # Maps variable -> node_id
        
        for instr in tac_list:
            # Parse assignment: var = expr
            match = re.match(r"(\w+)\s*=\s*(.+)", instr.strip())
            if not match:
                continue
            
            var, expr = match.group(1), match.group(2).strip()
            
            # Parse expression
            if expr.isdigit():
                # Constant
                node_id = self.add_node("const", [int(expr)])
            else:
                # Operation: a op b or variable
                op_match = re.match(r"(\w+)\s*([+\-*/])\s*(\w+)", expr)
                if op_match:
                    left, op, right = op_match.groups()
                    left_id = assignments.get(left, self.add_node("var", [left]))
                    right_id = assignments.get(right, self.add_node("var", [right]))
                    node_id = self.add_node(op, [left_id, right_id])
                else:
                    # Simple variable reference
                    node_id = assignments.get(expr, self.add_node("var", [expr]))
            
            assignments[var] = node_id
            self.nodes[node_id].var_names.append(var)
        
        return assignments
    
    def optimize(self, tac_list):
        """Optimize using DAG"""
        assignments = self.build_dag(tac_list)
        optimized = []
        
        for var, node_id in assignments.items():
            node = self.nodes[node_id]
            if node.op == "const":
                optimized.append(f"{var} = {node.operands[0]}")
            else:
                optimized.append(f"{var} = {node}")
        
        return optimized


def constant_fold(tac_list):
    """
    Optimize TAC by replacing constant expressions with their computed values.
    Performs constant folding: evaluate constant integer expressions at compile time.
    
    Args:
        tac_list: List of TAC instructions
    
    Returns:
        Optimized list of TAC instructions
    """
    optimized = []
    env = {}  # Environment to store computed values
    
    # Regex patterns
    bin_op = re.compile(r"(t\d+)\s*=\s*(\d+)\s*([+\-*/])\s*(\d+)")
    assign = re.compile(r"(t\d+)\s*=\s*(\d+)")
    
    for instr in tac_list:
        # Try to match binary operation
        m = bin_op.match(instr)
        if m:
            dest, a, op, b = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
            try:
                result = eval(f"{a}{op}{b}")
                env[dest] = result
                optimized.append(f"{dest} = {result}  # folded from {instr}")
                continue
            except:
                pass
        
        # Try to match simple assignment
        m2 = assign.match(instr)
        if m2:
            env[m2.group(1)] = int(m2.group(2))
        
        optimized.append(instr)
    
    return optimized


def strength_reduce(tac_list):
    """
    Reduce strong operations to weaker ones (e.g., multiply by 2 -> left shift)
    """
    optimized = []
    for instr in tac_list:
        # Example: t = x * 2 -> t = x << 1
        # (Not implemented for integer literals, but shown for completeness)
        optimized.append(instr)
    return optimized


if __name__ == "__main__":
    print("Original TAC:")
    tac = ["t1 = 255", "t2 = 42", "t3 = 255 + 42", "result = t3"]
    for line in tac:
        print(f"  {line}")
    
    print("\nOptimized TAC (with constant folding):")
    for line in constant_fold(tac):
        print(f"  {line}")
