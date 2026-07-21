# ==========================================
# MarketVerse Lab - Smart Line & Auto-Fixer Engine (Auto-Correct Enabled)
# ==========================================
import ast
from pathlib import Path

class SmartFixerEngine:
    def __init__(self, max_lines=10000):
        self.max_lines = max_lines

    def scan_and_find_exact_errors(self, root_path=".", uploaded_code_content=None):
        patches = []
        
        # 1. Handle uploaded or pasted code snippet with auto-formatting
        if uploaded_code_content:
            try:
                snippet_lines = uploaded_code_content.splitlines()
                target_lines = snippet_lines[:self.max_lines]
                
                # Auto-correct lines (Tabs to spaces, strip trailing whitespaces)
                fixed_lines = [line.expandtabs(4).rstrip() for line in target_lines]
                formatted_code = "\n".join(fixed_lines) + "\n"

                ast.parse(formatted_code)
            except SyntaxError as syn:
                patches.append({
                    "target_file": "Pasted Code Snippet",
                    "line_number": syn.lineno if syn.lineno else 1,
                    "issue_type": "Python Syntax Error",
                    "description": syn.msg,
                    "faulty_code": syn.text if syn.text else "Check syntax",
                    "exact_line_to_replace": "# Correct syntax on this line"
                })
            except IndentationError as ind:
                patches.append({
                    "target_file": "Pasted Code Snippet",
                    "line_number": ind.lineno if ind.lineno else 1,
                    "issue_type": "Indentation Error",
                    "description": ind.msg,
                    "faulty_code": ind.text if ind.text else "Check indentation",
                    "exact_line_to_replace": "# Fix spacing/tabs alignment here"
                })

        # 2. Scan project python files safely and auto-correct formatting
        p = Path(root_path)
        for py_file in p.rglob("*.py"):
            if any(skip in py_file.parts for skip in [".git", "__pycache__", ".venv", ".guardian"]):
                continue

            try:
                content = py_file.read_text(encoding="utf-8", errors="ignore")
                lines = content.splitlines()
                
                target_lines = lines[:self.max_lines]
                
                # Auto-correct lines for the file
                fixed_lines = [line.expandtabs(4).rstrip() for line in target_lines]
                analyzed_content = "\n".join(fixed_lines) + "\n"

                # Overwrite file with aligned and cleaned lines
                py_file.write_text(analyzed_content, encoding="utf-8")

                tree = ast.parse(analyzed_content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        func_name = ""
                        if isinstance(node.func, ast.Name):
                            func_name = node.func.id
                        elif isinstance(node.func, ast.Attribute):
                            func_name = node.func.attr

                        if func_name == "create_patch" and len(node.args) < 2:
                            line_no = node.lineno
                            patches.append({
                                "target_file": str(py_file),
                                "line_number": line_no,
                                "issue_type": "Argument Mismatch",
                                "description": f"Line {line_no}: create_patch() requires content argument.",
                                "faulty_code": lines[line_no - 1] if line_no <= len(lines) else "",
                                "exact_line_to_replace": "self.guardian.auto_patch_engine.create_patch('target_file.py', '# Updated Content')"
                            })
            except SyntaxError as syn:
                patches.append({
                    "target_file": str(py_file),
                    "line_number": syn.lineno if syn.lineno else 1,
                    "issue_type": "Syntax Error",
                    "description": syn.msg,
                    "faulty_code": syn.text if syn.text else "",
                    "exact_line_to_replace": "# Fix syntax on this line"
                })
            except IndentationError as ind:
                patches.append({
                    "target_file": str(py_file),
                    "line_number": syn.lineno if syn.lineno else 1,
                    "issue_type": "Indentation Error",
                    "description": ind.msg,
                    "faulty_code": syn.text if syn.text else "",
                    "exact_line_to_replace": "# Fix indentation spacing"
                })
            except Exception:
                continue

        if not patches:
            patches.append({
                "target_file": "Project Files",
                "line_number": "N/A",
                "issue_type": "Clean",
                "description": "All files are syntactically clean and auto-aligned.",
                "faulty_code": "N/A",
                "exact_line_to_replace": "# Code is clean and valid."
            })

        return {
            "status": "success",
            "line_mismatches_found": len([p for p in patches if p["issue_type"] != "Clean"]),
            "exact_patches": patches
        }
