"""
PHASE 2: Syntax Analyzer (Recursive Descent Parser)
Verifies that each token matches the integer-literal grammar
"""


class Parser:
    """Recursive descent parser for integer literals"""
    
    def __init__(self, text):
        self.text = text
        self.pos = 0
    
    def current(self):
        """Get current character"""
        return self.text[self.pos] if self.pos < len(self.text) else None
    
    def is_hex_digit(self, ch):
        """Check if character is a hex digit"""
        return ch and ch in "0123456789abcdefABCDEF"
    
    def integer_literal(self):
        """Parse integer-literal: digit+ | "0x" hex-digit+"""
        # Try hex branch: "0x" hex-digit+
        if self.text[self.pos:self.pos+2].lower() == "0x":
            self.pos += 2  # consume "0x"
            if not self.is_hex_digit(self.current()):
                raise SyntaxError("Expected hex-digit after 0x")
            while self.is_hex_digit(self.current()):
                self.pos += 1
        # Decimal branch: digit+
        elif self.current() and self.current().isdigit():
            while self.current() and self.current().isdigit():
                self.pos += 1
        else:
            raise SyntaxError("Expected digit or 0x prefix")
    
    def parse(self):
        """Parse and validate the input"""
        try:
            self.integer_literal()
            if self.pos == len(self.text):
                return True, "Valid Integer Literal"
            else:
                return False, f'Invalid: unexpected char "{self.current()}" at pos {self.pos}'
        except SyntaxError as e:
            return False, f"Syntax Error: {e}"


if __name__ == "__main__":
    token = input("Enter integer literal: ")
    parser = Parser(token)
    is_valid, message = parser.parse()
    print(message)
