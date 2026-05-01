<div align="center">

```
██████╗ ██████╗ ███╗   ███╗██████╗ ██╗██╗     ███████╗██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗
██║     ██║   ██║██╔████╔██║██████╔╝██║██║     █████╗  ██████╔╝
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║██║     ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║███████╗███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
```

# 🔢 Integer Literal Compiler

**A complete 7-phase compiler pipeline for integer literal recognition**  
*Decimal & Hexadecimal · Lexer to Assembly · Full Educational Pipeline*

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Phases](https://img.shields.io/badge/Phases-7-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

<br>

```
Source Code → Lexer → Parser → Symbol Table → SLR → TAC → Optimizer → Assembly
```

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Pipeline Architecture](#-pipeline-architecture)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Grammar](#-grammar)
- [Phase Breakdown](#-phase-breakdown)
- [Usage in Code](#-usage-in-code)
- [Example Output](#-example-output)
- [Installation](#-installation)

---

## 🧠 Overview

This project implements a **complete 7-phase compiler** for recognizing and compiling integer literals — both decimal and hexadecimal. Built with modularity in mind, each phase is independently importable and reusable.

| Feature | Support |
|---|---|
| Decimal Integers | ✅ `42`, `007`, `123` |
| Hexadecimal Integers | ✅ `0xFF`, `0x1A3F`, `0xDEADBEEF` |
| Invalid Input Detection | ✅ `0x`, `12abc`, `abc` |
| Assembly Code Generation | ✅ MOV, STORE, ADD, SUB, MUL, DIV |
| Constant Folding | ✅ DAG-based optimization |

---

## 🏗️ Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        SOURCE INPUT                             │
│                    e.g.  "42 0xFF 007"                          │
└──────────────────────────────┬──────────────────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 1 ⚡ Lexical Analysis               │
         │  Tokenizes source → INT / INT_HEX / INVALID│
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 2 🌳 Syntax Analysis                │
         │  Recursive descent parser → Valid/Invalid  │
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 3 📦 Symbol Table                   │
         │  Stores literals with type & address       │
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 4 🔄 SLR/LALR Parser                │
         │  State machine transitions → Accept/Reject │
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 5 📝 Three-Address Code (TAC)       │
         │  Generates intermediate IR instructions    │
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 6 ⚙️ Code Optimizer                 │
         │  Constant folding + DAG elimination        │
         └─────────────────────┬─────────────────────┘
                               │
         ┌─────────────────────▼─────────────────────┐
         │  PHASE 7 💾 Assembly Generation            │
         │  Outputs MOV / STORE / ADD instructions   │
         └─────────────────────┬─────────────────────┘
                               │
                      ✅ COMPILED OUTPUT
```

---

## 📁 Project Structure

```
compiler_pyside6/
│
├── 🚀 app.py                        # Mini-Compiler (Integration) — RUN THIS!
├── 📖 README.md
│
└── phases/                          # Core compiler phases
    ├── __init__.py
    ├── phase1_lexer.py              # Phase 1 · Token Recognition
    ├── phase2_parser.py             # Phase 2 · Recursive Descent Parser
    ├── phase3_symbol_table.py       # Phase 3 · Symbol Table
    ├── phase4_slr.py                # Phase 4 · SLR/LALR Parser
    ├── phase5_tac.py                # Phase 5 · Three-Address Code
    ├── phase6_optimizer.py          # Phase 6 · Code Optimizer (DAG)
    └── phase7_codegen.py            # Phase 7 · Assembly Generation
```

---

## ⚡ Quick Start

### Run with built-in example
```bash
python app.py --example
```

### Compile custom input
```bash
python app.py --compile "42 0xFF 007 0x1A3F"
```

### Interactive mode
```bash
python app.py
```

---

## 📐 Grammar

```ebnf
<integer-literal> ::= digit+ | "0x" hex-digit+
digit             ::= [0-9]
hex-digit         ::= [0-9a-fA-F]
```

| Input | Status | Reason |
|---|---|---|
| `42` | ✅ Valid | Decimal literal |
| `0xFF` | ✅ Valid | Hexadecimal literal |
| `007` | ✅ Valid | Decimal with leading zero |
| `0xDEADBEEF` | ✅ Valid | Large hex literal |
| `0x` | ❌ Invalid | Hex prefix without digits |
| `12abc` | ❌ Invalid | Letters after digits |
| `abc` | ❌ Invalid | Starts with letter |

---

## 🔍 Phase Breakdown

<details>
<summary><b>Phase 1 · Lexical Analysis</b></summary>

**Input:** Raw source code string  
**Output:** List of classified tokens

```
Input:  "42 0xFF invalid"
Output: [("INT", "42"), ("INT_HEX", "0xFF"), ("INVALID", "invalid")]
```
</details>

<details>
<summary><b>Phase 2 · Syntax Analysis</b></summary>

**Input:** Single literal string  
**Output:** Valid/Invalid status with message

```
Input:  "0xFF"
Output: ✓ Valid Integer Literal
```
</details>

<details>
<summary><b>Phase 3 · Symbol Table</b></summary>

**Input:** Literal and type  
**Output:** Symbol table entry with memory address

```
Name    Type        Value   Address
42      INT         42      2000
0xFF    INT_HEX     255     2001
```
</details>

<details>
<summary><b>Phase 4 · SLR Parser</b></summary>

**Input:** Token  
**Output:** Parse result with state transitions

```
Input:  "0xFF"
States: HEX_PREFIX → HEX → HEX → ACCEPT ✓
```
</details>

<details>
<summary><b>Phase 5 · Three-Address Code</b></summary>

**Input:** Operands + operator  
**Output:** TAC intermediate representation

```
result = 0xFF + 42
─────────────────────
t1 = 255
t2 = 42
t3 = t1 + t2
result = t3
```
</details>

<details>
<summary><b>Phase 6 · Code Optimizer</b></summary>

**Input:** TAC instructions  
**Output:** Optimized TAC

```
Before:  t3 = t1 + t2   (where t1=255, t2=42)
After:   t3 = 297        ← constant folding ✓
```

Optimizations applied:
- ♻️ **Constant Folding** — evaluates expressions at compile time
- 🔗 **DAG Optimization** — eliminates redundant computations
</details>

<details>
<summary><b>Phase 7 · Assembly Generation</b></summary>

**Input:** Literals from symbol table  
**Output:** Low-level assembly instructions

```asm
MOV   R1, #42
STORE R1, [2000]
MOV   R2, #0xFF
STORE R2, [2001]
ADD   R3, R1, R2
STORE R3, [2002]
```
</details>

---

## 🧩 Usage in Code

```python
from phases import (
    lexer, Parser, SymbolTable,
    slr_parse, generate_tac,
    constant_fold, generate_assembly
)

# Phase 1 — Tokenize
tokens = lexer("42 0xFF")
# → [("INT", "42"), ("INT_HEX", "0xFF")]

# Phase 2 — Validate syntax
parser = Parser("0xFF")
valid, msg = parser.parse()

# Phase 3 — Symbol table
st = SymbolTable()
st.insert("42", "INT")

# Phase 4 — SLR parse
valid, state, trace = slr_parse("0xFF")

# Phase 5 — TAC generation
tac = generate_tac("result", ["42", "0xFF"], "+")

# Phase 6 — Optimize
optimized = constant_fold(tac)

# Phase 7 — Assembly output
asm = generate_assembly([("42", "INT"), ("0xFF", "INT_HEX")])
```

---

## 📊 Example Output

```
================================================================================
 PHASE 1: LEXICAL ANALYSIS — Token Recognition
================================================================================
  Token Type      Token Value
  INT             42
  INT_HEX         0xFF

================================================================================
 PHASE 2: SYNTAX ANALYSIS — Recursive Descent Parser
================================================================================
  42    →  ✓ VALID
  0xFF  →  ✓ VALID

================================================================================
 COMPILATION COMPLETE
================================================================================
  ✔  Total tokens         : 2
  ✔  Symbol table entries : 2
  ✔  TAC instructions     : 4
  ✔  Assembly instructions: 8
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Anuragkumar0429/integer-literal-compiler.git
cd integer-literal-compiler

# Install dependency
pip install PySide6

# Run
python app.py --example
```

---

## 📦 The 6 Core Components

| # | Component | File | Description |
|---|---|---|---|
| 1 | Lexical Analyzer | `phase1_lexer.py` | Token recognition |
| 2 | Syntax Parser | `phase2_parser.py` | Recursive descent |
| 3 | LR Table Generator | `phase4_slr.py` | SLR/LALR simulator |
| 4 | IR Translator | `phase5_tac.py` | Three-address code |
| 5 | Code Optimizer | `phase6_optimizer.py` | DAG + constant folding |
| 6 | Mini-Compiler | `app.py` | Full phase integration |

---

<div align="center">

**Built with ❤️ by [Anurag Kumar Upadhyay](https://github.com/Anuragkumar0429)**

*Symbol table starts at address `2000` · Assembly supports MOV, STORE, ADD, SUB, MUL, DIV*

</div>
