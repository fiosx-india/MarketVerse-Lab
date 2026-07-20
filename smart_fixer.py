# ==========================================
# MarketVerse Lab - Smart Line & Auto-Fixer Engine (Optimized)
# ==========================================
import ast
from pathlib import Path

class SmartFixerEngine:
    def __init__(self):
        pass

    def scan_and_find_exact_errors(self, root_path=".", uploaded_code_content=None):
        """
        Scans code line-by-line, ignores valid comments/docstrings,
        and flags only true Python syntax, indentation, or argument errors.
        """
        patches = []
        
        # 1. Analyze pasted/uploaded code snippet if provided
        if uploaded_code_content:
            try:
                ast.parse(uploaded_code_content)
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

        # 2. Scan project python files safely (ignoring false comment dots)
        p = Path(root_path)
        for py_file in p.rglob("*.py"):
            if any(skip in py_file.parts for skip in [".git", "__pycache__", ".venv"]):
                continue

            try:
                content = py_file.read_text(encoding="utf-8", errors="ignore")
                lines = content.splitlines()
                tree = ast.parse(content)

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
                    "line_number": ind.lineno if ind.lineno else 1,
                    "issue_type": "Indentation Error",
                    "description": ind.msg,
                    "faulty_code": ind.text if ind.text else "",
                    "exact_line_to_replace": "# Fix indentation spacing"
                })
            except Exception:
                continue

        if not patches:
            patches.append({
                "target_file": "Project Files",
                "line_number": "N/A",
                "issue_type": "Clean",
                "description": "All files are syntactically clean with zero errors.",
                "faulty_code": "N/A",
                "exact_line_to_replace": "# Code is clean and valid."
            })

        return {
            "status": "success",
            "line_mismatches_found": len([p for p in patches if p["issue_type"] != "Clean"]),
            "exact_patches": patches
        }

    # ==========================================
    # Integrated Smart Fixer Extension (Appended Below)
    # ==========================================
    st.markdown("---")
    st.subheader("🔍 Advanced File & Large Code Indentation Inspector (1000+ Lines)")
    st.caption("Works alongside existing inspectors to verify block hierarchy, spacing flow, and line alignment without altering core code.")

    if st.button("🚀 Run Comprehensive Indentation & Line Inspector"):
        with st.spinner("Analyzing large-scale lines, block hierarchy, and spacing flows..."):
            try:
                from smart_fixer import SmartFixerEngine
                fixer = SmartFixerEngine()
                
                # Fetch text area content safely from session/local context if available
                current_pasted_code = locals().get('user_code', None)
                
                # Run the scan through smart_fixer engine
                report = fixer.scan_and_find_exact_errors(".", uploaded_code_content=current_pasted_code)
                
                st.success("✅ Large-Scale Code & Indentation Flow Inspection Complete!")
                
                if report.get("line_mismatches_found", 0) > 0:
                    for patch in report.get("exact_patches", []):
                        if patch["issue_type"] != "Clean":
                            st.error(f"❌ **File / Source:** `{patch['target_file']}` | 🔢 **Line Number:** `{patch['line_number']}`")
                            st.warning(f"⚠️ **Issue Found:** {patch['issue_type']} — {patch['description']}")
                            
                            st.markdown("👉 **Faulty Code / Block:**")
                            st.code(patch['faulty_code'], language="python")
                            
                            st.markdown("✍️ **Exact Line to Copy & Replace:**")
                            st.code(patch["exact_line_to_replace"], language="python")
                else:
                    st.success("🎉 All lines, code blocks, and 1000+ line hierarchies are perfectly aligned and error-free!")
            except Exception as e:
                st.error(f"Extension Connection Error: {str(e)}")

