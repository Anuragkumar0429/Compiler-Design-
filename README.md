*Type your source code into the provided editor within the UI, and the system will process the integer literals and display the resulting tokens.*

## 🗺️ Roadmap

- [x] Set up PySide6 UI Foundation
- [x] Implement Integer Literal Lexical Analysis
- [ ] Add support for Floating-Point Literals
- [ ] Implement Syntax Highlighting in the UI
- [ ] Build Abstract Syntax Tree (AST) Visualizer

## 🤝 Contributing

Contributions, issues, and feature requests areHere is a professional, attractive `README.md` template perfectly tailored for your PySide6 compiler project, specifically highlighting the integer literal functionality. 

You can create a new file named `README.md` in your project folder, copy and paste the block below into it, and then push it to GitHub.
```markdown
# ⚡ Compiler Design: Integer Literal Lexer & UI

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green?style=for-the-badge&logo=qt)
![Build](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A robust, interactive Compiler Development Environment built with Python and PySide6. This project serves as a visual and functional playground for compiler design concepts, currently focusing heavily on the accurate lexical analysis and tokenization of **Integer Literals**.

## ✨ Features

* **Advanced Lexical Analysis:** Precisely identifies, validates, and tokenizes integer literals from raw source code.
* **Graphical User Interface:** Features a clean, modern UI built with PySide6, allowing users to type code and instantly see the compilation phases.
* **Real-Time Tokenization:** Visually separates recognized tokens from errors or unrecognized syntax.
* **Cross-Platform:** Runs seamlessly on macOS, Windows, and Linux.

## 🛠️ Technology Stack

* **Language:** Python
* **GUI Framework:** PySide6 (Qt for Python)
* **Version Control:** Git & GitHub

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

Ensure you have Python installed on your system. It is highly recommended to use a virtual environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anuragkumar0429/Compiler-Design-.git
   cd Compiler-Design-
📌 Overview
This project implements a complete compiler pipeline broken into 7 modular phases — from lexical analysis all the way through to target assembly code generation. It processes decimal and hexadecimal integer literals through each classical compiler stage.

Built as an academic deep-dive into compiler construction theory, with clean, standalone modules for each phase.


🗂️ Pipeline Architecture
Source Text
    │
    ▼
┌─────────────────────────┐
│  Phase 1 · Lexer        │  Tokenizes input → INT, INT_HEX, INVALID
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 2 · Parser       │  Recursive descent grammar validation
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 3 · Symbol Table │  Stores name, type, value, memory address
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 4 · SLR Parser   │  DFA-based LR parse trace & validation
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 5 · TAC Gen      │  Three-Address Code intermediate generation
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 6 · Optimizer    │  Constant folding + DAG-based optimization
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Phase 7 · Code Gen     │  Target assembly (MOV / STORE / ADD / ...)
└─────────────────────────┘
             │
             ▼
         Assembly Output

📦 Modules at a Glance
FilePhaseResponsibilityphase1_lexer.pyLexical AnalysisTokenizes source text into INT, INT_HEX, INVALID tokensphase2_parser.pySyntax AnalysisRecursive descent parser validating integer-literal grammarphase3_symbol_table.pySymbol TableTracks literals with name, type, decimal value, and memory addressphase4_slr.pyLR ParsingDFA-based SLR simulator with full state-transition tracingphase5_tac.pyIntermediate CodeGenerates Three-Address Code (TAC) for literals and expressionsphase6_optimizer.pyOptimizationConstant folding and DAG-based basic block optimizationphase7_codegen.pyCode GenerationEmits pseudo-assembly (MOV, STORE, ADD, SUB, MUL, DIV)

🚀 Quick Start
Clone the repo
bashgit clone https://github.com/your-username/integer-literal-compiler.git
cd integer-literal-compiler
Run any phase independently
bash# Phase 1 — Lexer
python phase1_lexer.py
# > Enter integer literals: 42 0xFF 007 hello

# Phase 4 — SLR Parser
python phase4_slr.py
# > Enter token (e.g. 42 or 0xFF): 0x1A3F

# Phase 7 — Assembly Code Generator
python phase7_codegen.py
Use as a package
pythonfrom compiler import lexer, Parser, SymbolTable, slr_parse
from compiler import generate_tac, constant_fold, generate_assembly

# Tokenize
tokens = lexer("42 0xFF 007")

# Parse each token
for tok_type, tok_val in tokens:
    parser = Parser(tok_val)
    valid, msg = parser.parse()
    print(f"{tok_val}: {msg}")

# Build symbol table
st = SymbolTable(start_address=2000)
for tok_type, tok_val in tokens:
    st.insert(tok_val, tok_type)
print(st.display())

# Generate & optimize TAC
tac = generate_tac("result", ["0xFF", "42"])
optimized = constant_fold(tac)

# Emit assembly
asm = generate_assembly_operation([("0xFF", "INT_HEX"), ("42", "INT")], "+")
print("\n".join(asm))

🔍 Phase Walkthrough
Phase 1 — Lexer
Input: 42 0xFF abc 0x
TOKEN: INT          Value: 42
TOKEN: INT_HEX      Value: 0xFF
TOKEN: INVALID      Value: abc
TOKEN: INVALID      Value: 0x
Phase 3 — Symbol Table
Name           Type           Value       Address
----------------------------------------------------
42             INT            42          2000
0xFF           INT_HEX        255         2001
007            INT            7           2002
Phase 5 — Three-Address Code
; result = 0xFF + 42
t1 = 255
t2 = 42
t3 = t1 + t2
result = t3
Phase 6 — Constant Folding
; Before optimization
t1 = 255
t2 = 42
t3 = 255 + 42

; After constant folding
t3 = 297  # folded from t3 = 255 + 42
Phase 7 — Assembly Output
asm; ===== Integer Literal Operation Assembly Code =====

; Load operand 1: 0xFF
MOV R1, #0xFF
STORE R1, [2000]

; Load operand 2: 42
MOV R2, #42
STORE R2, [2001]

; Perform operation: 0xFF + 42
ADD R3, R1, R2
STORE R3, [2002]

; ===== End of Code =====

🧠 Key Concepts Demonstrated

Finite Automata — DFA state transitions in the SLR parser (Phase 4)
Recursive Descent Parsing — Hand-written grammar rules (Phase 2)
Symbol Table Management — Duplicate detection, address allocation (Phase 3)
Three-Address Code — Classic IR used in real compilers like GCC (Phase 5)
DAG Optimization — Directed Acyclic Graph for common subexpression elimination (Phase 6)
Constant Folding — Compile-time evaluation of constant expressions (Phase 6)
Register Allocation — Simple linear register mapping for assembly (Phase 7)


📋 Supported Integer Literal Formats
FormatExampleNotesDecimal42, 007, 1000Standard base-10 integerHexadecimal0xFF, 0x1A3F, 0X00Prefix 0x or 0X, case-insensitive digits

🤝 Contributing
Pull requests are welcome! If you'd like to extend the pipeline (e.g., add floating-point literals, support more operators, or add a real register allocator), feel free to open an issue first.

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

<div align="center">
Made with 🧩 and compiler theory
</div>
