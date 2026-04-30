"""
PHASE 3: Symbol Table Design
Records name, type, numeric value, and memory address for each literal
"""


class SymbolTable:
    """Symbol table for storing integer literals"""
    
    def __init__(self, start_address=2000):
        self.table = []
        self.address = start_address
    
    def insert(self, name, lit_type):
        """Insert a literal into the symbol table"""
        try:
            # Compute numeric value
            if lit_type == "INT_HEX":
                value = int(name, 16)
            else:
                value = int(name, 10)
            
            # Check for duplicates
            for entry in self.table:
                if entry["name"] == name and entry["type"] == lit_type:
                    return False  # Already exists
            
            self.table.append({
                "name": name,
                "type": lit_type,
                "value": value,
                "addr": self.address
            })
            self.address += 1
            return True
        except ValueError:
            return False
    
    def lookup(self, name):
        """Look up a literal in the symbol table"""
        for entry in self.table:
            if entry["name"] == name:
                return entry
        return None
    
    def display(self):
        """Display the symbol table in formatted output"""
        if not self.table:
            return "Symbol table is empty."
        
        output = []
        output.append(f"{'Name':<15}{'Type':<15}{'Value':<12}{'Address':<10}")
        output.append("-" * 52)
        for e in self.table:
            output.append(f"{e['name']:<15}{e['type']:<15}{e['value']:<12}{e['addr']:<10}")
        return "\n".join(output)
    
    def clear(self):
        """Clear the symbol table"""
        self.table = []
        self.address = 2000


if __name__ == "__main__":
    st = SymbolTable()
    st.insert("42", "INT")
    st.insert("0xFF", "INT_HEX")
    st.insert("007", "INT")
    st.insert("0x1A3F", "INT_HEX")
    print(st.display())
