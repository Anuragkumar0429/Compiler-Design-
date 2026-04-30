"""
Compiler phases package
"""

from .phase1_lexer import lexer
from .phase2_parser import Parser
from .phase3_symbol_table import SymbolTable
from .phase4_slr import slr_parse
from .phase5_tac import generate_tac, generate_tac_assignment
from .phase6_optimizer import constant_fold
from .phase7_codegen import generate_assembly, generate_assembly_operation

__all__ = [
    'lexer',
    'Parser',
    'SymbolTable',
    'slr_parse',
    'generate_tac',
    'generate_tac_assignment',
    'constant_fold',
    'generate_assembly',
    'generate_assembly_operation',
]
