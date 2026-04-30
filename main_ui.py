"""
PySide6 GUI for Integer Literal Compiler
Modern tab-based interface for all 7 phases
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QTabWidget, QMessageBox
)
from PySide6.QtCore import Qt

# Import your compiler
from app import Compiler


class CompilerUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.compiler = Compiler()

        self.setWindowTitle("Integer Literal Compiler - 7 Phase Visualizer")
        self.setGeometry(100, 100, 1000, 700)

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # 🔹 Title
        title = QLabel("INTEGER LITERAL COMPILER")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        # 🔹 Input Box
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Enter integer literals (e.g., 42 0xFF 007)")
        self.input_box.setFixedHeight(80)

        # 🔹 Buttons
        btn_layout = QHBoxLayout()

        self.run_btn = QPushButton("Run Compiler")
        self.run_btn.clicked.connect(self.run_compiler)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_all)

        btn_layout.addWidget(self.run_btn)
        btn_layout.addWidget(self.clear_btn)

        # 🔹 Tabs for phases
        self.tabs = QTabWidget()

        self.phase1_tab = QTextEdit()
        self.phase2_tab = QTextEdit()
        self.phase3_tab = QTextEdit()
        self.phase4_tab = QTextEdit()
        self.phase5_tab = QTextEdit()
        self.phase6_tab = QTextEdit()
        self.phase7_tab = QTextEdit()

        for tab in [
            self.phase1_tab, self.phase2_tab, self.phase3_tab,
            self.phase4_tab, self.phase5_tab, self.phase6_tab,
            self.phase7_tab
        ]:
            tab.setReadOnly(True)

        self.tabs.addTab(self.phase1_tab, "Phase 1: Lexer")
        self.tabs.addTab(self.phase2_tab, "Phase 2: Parser")
        self.tabs.addTab(self.phase3_tab, "Phase 3: Symbol Table")
        self.tabs.addTab(self.phase4_tab, "Phase 4: SLR Parser")
        self.tabs.addTab(self.phase5_tab, "Phase 5: TAC")
        self.tabs.addTab(self.phase6_tab, "Phase 6: Optimizer")
        self.tabs.addTab(self.phase7_tab, "Phase 7: CodeGen")

        # 🔹 Layout assembly
        main_layout.addWidget(title)
        main_layout.addWidget(self.input_box)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.tabs)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def clear_all(self):
        self.input_box.clear()
        for tab in [
            self.phase1_tab, self.phase2_tab, self.phase3_tab,
            self.phase4_tab, self.phase5_tab, self.phase6_tab,
            self.phase7_tab
        ]:
            tab.clear()

    def run_compiler(self):
        source = self.input_box.toPlainText().strip()

        if not source:
            QMessageBox.warning(self, "Error", "Please enter input.")
            return

        try:
            # Phase 1
            tokens = self.compiler.phase1_lexer(source)
            p1_text = "Token Type\tToken Value\n"
            for t in tokens:
                p1_text += f"{t[0]}\t\t{t[1]}\n"
            self.phase1_tab.setText(p1_text)

            if not self.compiler.valid_tokens:
                QMessageBox.warning(self, "Error", "No valid tokens found.")
                return

            # Phase 2
            results = self.compiler.phase2_parser()
            p2_text = ""
            for r in results:
                status = "VALID" if r["valid"] else "INVALID"
                p2_text += f"{r['token']} → {status}\n{r['message']}\n\n"
            self.phase2_tab.setText(p2_text)

            # Phase 3
            st = self.compiler.phase3_symbol_table()
            self.phase3_tab.setText(st.display())

            # Phase 4
            slr = self.compiler.phase4_slr_parser()
            p4_text = ""
            for r in slr:
                status = "ACCEPTED" if r["valid"] else "REJECTED"
                p4_text += f"{r['token']} → {status}\n"
                p4_text += f"Final State: {r['final_state']}\n"
                p4_text += "\n".join(r["trace"]) + "\n\n"
            self.phase4_tab.setText(p4_text)

            # Phase 5
            tac = self.compiler.phase5_tac()
            p5_text = "\n".join(tac)
            self.phase5_tab.setText(p5_text)

            # Phase 6
            opt = self.compiler.phase6_optimizer(tac)
            p6_text = "Original:\n"
            p6_text += "\n".join(opt["original"]) + "\n\n"
            p6_text += "Constant Folded:\n"
            p6_text += "\n".join(opt["constant_folded"]) + "\n\n"
            p6_text += "DAG Optimized:\n"
            p6_text += "\n".join(opt["dag_optimized"])
            self.phase6_tab.setText(p6_text)

            # Phase 7
            asm = self.compiler.phase7_codegen()
            p7_text = "\n".join(asm)
            self.phase7_tab.setText(p7_text)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


# Standalone run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompilerUI()
    window.show()
    sys.exit(app.exec())