"""
INTEGER LITERAL COMPILER - Complete Integration
Full compiler with all 7 phases integrated
Can be run as CLI or GUI
"""

import sys
import argparse
from pathlib import Path

# Add phases directory to path
sys.path.insert(0, str(Path(__file__).parent))

from phases import (
    lexer,
    Parser,
    SymbolTable,
    slr_parse,
    generate_tac,
    generate_tac_assignment,
    constant_fold,
    generate_assembly,
    generate_assembly_operation,
)
from phases.phase6_optimizer import DAGOptimizer


class Compiler:
    """Complete integer literal compiler with all 7 phases"""
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.source_code = ""
        self.tokens = []
        self.valid_tokens = []
    
    def phase1_lexer(self, source):
        """PHASE 1: Lexical Analysis"""
        self.source_code = source
        self.tokens = lexer(source)
        self.valid_tokens = [t for t in self.tokens if t[0] != "INVALID"]
        return self.tokens
    
    def phase2_parser(self):
        """PHASE 2: Syntax Analysis"""
        results = []
        for token_type, token_value in self.valid_tokens:
            parser = Parser(token_value)
            is_valid, message = parser.parse()
            results.append({
                "token": token_value,
                "type": token_type,
                "valid": is_valid,
                "message": message
            })
        return results
    
    def phase3_symbol_table(self):
        """PHASE 3: Symbol Table"""
        self.symbol_table.clear()
        for token_type, token_value in self.valid_tokens:
            lit_type = "INT" if token_type == "INT" else "INT_HEX"
            self.symbol_table.insert(token_value, lit_type)
        return self.symbol_table
    
    def phase4_slr_parser(self):
        """PHASE 4: SLR Parser"""
        results = []
        for token_type, token_value in self.valid_tokens:
            is_valid, final_state, trace = slr_parse(token_value)
            results.append({
                "token": token_value,
                "valid": is_valid,
                "final_state": final_state,
                "trace": trace
            })
        return results
    
    def phase5_tac(self):
        """PHASE 5: TAC Generation"""
        if len(self.valid_tokens) < 2:
            return generate_tac_assignment("result", self.valid_tokens[0][1]) if self.valid_tokens else []
        
        operands = [t[1] for t in self.valid_tokens[:2]]
        return generate_tac("result", operands, "+")
    
    def phase6_optimizer(self, tac):
        """PHASE 6: Code Optimization"""
        # Constant folding
        folded = constant_fold(tac)
        
        # DAG optimization
        dag = DAGOptimizer()
        dag_optimized = dag.optimize(folded)
        
        return {
            "original": tac,
            "constant_folded": folded,
            "dag_optimized": dag_optimized
        }
    
    def phase7_codegen(self):
        """PHASE 7: Code Generation"""
        if not self.valid_tokens:
            return []
        
        # Convert tokens to proper format: (literal_value, literal_type)
        literals = [(value, "INT_HEX" if token_type == "INT_HEX" else "INT") 
                    for token_type, value in self.valid_tokens[:3]]
        
        if len(literals) >= 2:
            return generate_assembly_operation(literals, "+")
        else:
            return generate_assembly(literals)
    
    def compile(self, source):
        """Execute complete compilation flow"""
        print("=" * 80)
        print("INTEGER LITERAL COMPILER - COMPLETE FLOW")
        print("=" * 80)
        print(f"\nSource Input: {source}\n")
        
        # Phase 1: Lexical Analysis
        print("\n" + "=" * 80)
        print("PHASE 1: LEXICAL ANALYSIS (Token Recognition)")
        print("=" * 80)
        tokens = self.phase1_lexer(source)
        print(f"\nInput: {source}")
        print(f"\n{'Token Type':<15} {'Token Value':<20}")
        print("-" * 35)
        for token_type, token_value in tokens:
            status = "✓" if token_type != "INVALID" else "✗"
            print(f"{token_type:<15} {token_value:<20} {status}")
        
        print(f"\nSummary: {len(self.valid_tokens)} valid, {len(tokens) - len(self.valid_tokens)} invalid")
        
        if not self.valid_tokens:
            print("\nNo valid tokens to continue compilation.")
            return
        
        # Phase 2: Syntax Analysis
        print("\n" + "=" * 80)
        print("PHASE 2: SYNTAX ANALYSIS (Recursive Descent Parser)")
        print("=" * 80)
        parse_results = self.phase2_parser()
        for result in parse_results:
            status = "✓ VALID" if result["valid"] else "✗ INVALID"
            print(f"\n{result['token']}: {status}")
            print(f"  Type: {result['type']}")
            print(f"  Message: {result['message']}")
        
        # Phase 3: Symbol Table
        print("\n" + "=" * 80)
        print("PHASE 3: SYMBOL TABLE (Storage Management)")
        print("=" * 80)
        st = self.phase3_symbol_table()
        print("\n" + st.display())
        
        # Phase 4: SLR Parser
        print("\n" + "=" * 80)
        print("PHASE 4: LR PARSING TABLE GENERATOR (SLR/LALR Simulator)")
        print("=" * 80)
        slr_results = self.phase4_slr_parser()
        for result in slr_results:
            status = "✓ ACCEPTED" if result["valid"] else "✗ REJECTED"
            print(f"\nToken: {result['token']} → {status}")
            print(f"Final State: {result['final_state']}")
            print("Parse Trace:")
            for line in result["trace"]:
                print(f"  {line}")
        
        # Phase 5: TAC Generation
        print("\n" + "=" * 80)
        print("PHASE 5: INTERMEDIATE CODE TRANSLATOR (Three-Address Code)")
        print("=" * 80)
        tac = self.phase5_tac()
        print("\nGenerated TAC:")
        for i, instr in enumerate(tac, 1):
            print(f"  {i}. {instr}")
        
        # Phase 6: Optimization
        print("\n" + "=" * 80)
        print("PHASE 6: CODE OPTIMIZER (Constant Folding & DAG Basic Block Opt)")
        print("=" * 80)
        opt_results = self.phase6_optimizer(tac)
        
        print("\nOriginal TAC:")
        for instr in opt_results["original"]:
            print(f"  {instr}")
        
        print("\nAfter Constant Folding:")
        for instr in opt_results["constant_folded"]:
            print(f"  {instr}")
        
        print("\nAfter DAG Optimization:")
        for instr in opt_results["dag_optimized"]:
            print(f"  {instr}")
        
        # Phase 7: Code Generation
        print("\n" + "=" * 80)
        print("PHASE 7: TARGET CODE GENERATOR (Assembly Code Generation)")
        print("=" * 80)
        asm = self.phase7_codegen()
        print("\nGenerated Assembly Code:")
        for line in asm:
            print(f"  {line}")
        
        # Summary
        print("\n" + "=" * 80)
        print("COMPILATION COMPLETE")
        print("=" * 80)
        print("\nCompilation Statistics:")
        print(f"  Total tokens generated: {len(tokens)}")
        print(f"  Valid tokens: {len(self.valid_tokens)}")
        print(f"  Invalid tokens: {len(tokens) - len(self.valid_tokens)}")
        print(f"  Symbol table entries: {len(st.table)}")
        print(f"  TAC instructions: {len(tac)}")
        print(f"  Assembly instructions: {len(asm)}")


def run_cli():
    """Run compiler in CLI mode"""
    parser = argparse.ArgumentParser(
        description="Integer Literal Compiler - Complete 7-Phase Compiler",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py --compile "42 0xFF"
  python app.py --compile "007 0x1A3F 0xDEADBEEF"
  python app.py --gui
        """
    )
    
    parser.add_argument(
        "--compile", "-c",
        type=str,
        help="Source code to compile"
    )
    
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch GUI application"
    )
    
    parser.add_argument(
        "--example", "-e",
        action="store_true",
        help="Run with example input"
    )
    
    args = parser.parse_args()
    
    # Run GUI if requested
    if args.gui:
        from main_ui import CompilerUI
        from PySide6.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = CompilerUI()
        window.show()
        sys.exit(app.exec())
    
    # Run with example input
    if args.example:
        compiler = Compiler()
        compiler.compile("42 0xFF 007 0x1A3F")
        return
    
    # Run with provided input
    if args.compile:
        compiler = Compiler()
        compiler.compile(args.compile)
        return
    
    # Interactive mode
    print("Integer Literal Compiler - Interactive Mode")
    print("=" * 50)
    print("Enter 'quit' to exit, 'gui' to launch GUI\n")
    
    compiler = Compiler()
    
    while True:
        try:
            source = input("Enter integer literals (space-separated): ").strip()
            
            if source.lower() == "quit":
                print("Exiting...")
                break
            
            if source.lower() == "gui":
                from main_ui import CompilerUI
                from PySide6.QtWidgets import QApplication
                app = QApplication(sys.argv)
                window = CompilerUI()
                window.show()
                sys.exit(app.exec())
            
            if source:
                compiler.compile(source)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run_cli()
