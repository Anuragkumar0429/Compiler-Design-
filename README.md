# Integer Literal Compiler

A complete 7-phase compiler for integer literal recognition. Recognizes decimal and hexadecimal integer literals and compiles them through a full compilation pipeline.

## Project Structure

```
compiler_pyside6/
├── app.py                 # Mini-Compiler (Integration) - RUN THIS!
├── README.md              # This file
└── phases/                # Core compiler phases
    ├── __init__.py
    ├── phase1_lexer.py           # Phase 1: Token Recognition
    ├── phase2_parser.py          # Phase 2: Recursive Descent Parser
    ├── phase3_symbol_table.py    # Phase 3: Symbol Table
    ├── phase4_slr.py             # Phase 4: SLR/LALR Parser
    ├── phase5_tac.py             # Phase 5: Three-Address Code
    ├── phase6_optimizer.py       # Phase 6: Code Optimizer (DAG)
    └── phase7_codegen.py         # Phase 7: Assembly Generation
```

## The 6 Required Components

1. **Lexical Analyzer Build** (`phases/phase1_lexer.py`) - Token Recognition
2. **Syntax Parser Implementation** (`phases/phase2_parser.py`) - Recursive Descent
3. **LR Parsing Table Generator** (`phases/phase4_slr.py`) - SLR/LALR Simulator
4. **Intermediate Code Translator** (`phases/phase5_tac.py`) - Three-Address Code
5. **Code Optimizer Prototype** (`phases/phase6_optimizer.py`) - DAG Basic Block Opt
6. **Mini-Compiler Project** (`app.py`) - Full Phase Integration

## Quick Start

### Run with Example
```bash
python app.py --example
```

### Run with Custom Input
```bash
python app.py --compile "42 0xFF 007 0x1A3F"
```

### Interactive Mode
```bash
python app.py
```

## Grammar

```
<integer-literal> ::= digit+ | "0x" hex-digit+
digit             ::= [0-9]
hex-digit         ::= [0-9a-fA-F]
```

**Valid Inputs**:
- Decimal: `42`, `007`, `123`
- Hexadecimal: `0xFF`, `0x1A3F`, `0xDEADBEEF`

**Invalid Inputs**:
- `0x` (hex prefix without digits)
- `12abc` (letters after digits)
- `abc` (starts with letter)

## The 7 Compilation Phases

### Phase 1: Lexical Analysis
**Input**: Source code  
**Output**: List of tokens

```
Input:  "42 0xFF invalid"
Output: [("INT", "42"), ("INT_HEX", "0xFF"), ("INVALID", "invalid")]
```

### Phase 2: Syntax Analysis
**Input**: Single literal  
**Output**: Valid/Invalid status

```
Input:  "0xFF"
Output: ✓ Valid Integer Literal
```

### Phase 3: Symbol Table
**Input**: Literal and type  
**Output**: Symbol table with addresses

```
Name    Type        Value   Address
42      INT         42      2000
0xFF    INT_HEX     255     2001
```

### Phase 4: SLR Parser
**Input**: Token  
**Output**: Parse result with state transitions

```
Input:  "0xFF"
Output: ✓ Accepted
        States: HEX_PREFIX → HEX → HEX → ACCEPT
```

### Phase 5: TAC Generation
**Input**: Operands and operator  
**Output**: Three-Address Code

```
Input:  result = 0xFF + 42
TAC:    t1 = 255
        t2 = 42
        t3 = t1 + t2
        result = t3
```

### Phase 6: Code Optimization
**Input**: TAC instructions  
**Output**: Optimized TAC

- Constant folding: `t = 255 + 42` → `t = 297`
- DAG optimization: Eliminate redundant computations

### Phase 7: Assembly Generation
**Input**: Literals  
**Output**: Assembly code

```
MOV R1, #42
STORE R1, [2000]
MOV R2, #0xFF
STORE R2, [2001]
ADD R3, R1, R2
STORE R3, [2002]
```

## Using the Phases in Your Code

```python
from phases import lexer, Parser, SymbolTable, slr_parse, generate_tac, constant_fold, generate_assembly

# Phase 1: Tokenize
tokens = lexer("42 0xFF")

# Phase 2: Parse
parser = Parser("0xFF")
valid, msg = parser.parse()

# Phase 3: Symbol table
st = SymbolTable()
st.insert("42", "INT")

# Phase 4: SLR parse
valid, state, trace = slr_parse("0xFF")

# Phase 5: TAC
tac = generate_tac("result", ["42", "0xFF"], "+")

# Phase 6: Optimize
optimized = constant_fold(tac)

# Phase 7: Assembly
asm = generate_assembly([("42", "INT"), ("0xFF", "INT_HEX")])
```

## Complete Compilation Flow

```
Source Input
  ↓
[1] Lexical Analysis → Tokens
  ↓
[2] Syntax Analysis → Validation
  ↓
[3] Symbol Table → Storage
  ↓
[4] SLR Parser → State Transitions
  ↓
[5] TAC Generation → Intermediate Code
  ↓
[6] Optimization → Constant Folding + DAG
  ↓
[7] Code Generation → Assembly
  ↓
Compiled Output
```

## Features

✓ Complete 7-phase compiler
✓ Lexical analysis with token recognition
✓ Recursive descent parser
✓ SLR/LALR parsing simulator
✓ Three-address code generation
✓ Constant folding & DAG optimization
✓ Assembly code generation
✓ Symbol table management
✓ Multiple execution modes
✓ Clean, modular architecture

## Installation

```bash
pip install PySide6
```

## Example Output

```bash
$ python app.py --compile "42 0xFF"

================================================================================
PHASE 1: LEXICAL ANALYSIS (Token Recognition)
================================================================================
Token Type      Token Value
INT             42
INT_HEX         0xFF

================================================================================
PHASE 2: SYNTAX ANALYSIS (Recursive Descent Parser)
================================================================================
42: ✓ VALID
0xFF: ✓ VALID

... (phases 3-7 output) ...

================================================================================
COMPILATION COMPLETE
================================================================================
Compilation Statistics:
  Total tokens: 2
  Symbol table entries: 2
  TAC instructions: 4
  Assembly instructions: 8
```

## Notes

- Each phase can be used independently by importing from `phases`
- Symbol table starts at address 2000
- Assembly code supports MOV, STORE, ADD, SUB, MUL, DIV instructions
- Hex values are automatically converted to decimal
- TAC generation uses temporary variables (t1, t2, ...)
