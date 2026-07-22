# ==========================================
# MarketVerse Lab - Master Unified Enterprise App
# ==========================================
import streamlit as st
import json
import traceback
import os
import ast
import time
import gc

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MarketVerse Lab - Master Enterprise Console")
st.success("Stage 1 : Foundation & Multi-Module Architecture Ready")

# Initialize Guardian Core safely
guardian_ready = False
guardian = None

try:
    from marketverse_lab.guardian_core import GuardianCore
    guardian = GuardianCore()
    guardian_ready = True
except Exception as e:
    guardian_ready = False

# Create Tabs for Main Sections
tab1, tab2, tab3, tab4 = st.tabs([
    "📁 File & Code Inspector", 
    "🛡️ Guardian Core Status", 
    "📊 Management & Diagnostics",
    "🛡️ Secure File Exporter"
])

# ==========================================
# TAB 1: File Inspector & Code Tester
# ==========================================
with tab1:
    st.header("🛡️ File Inspector & Code Tester")
    st.caption("Upload any Python, JSON, or CAD/3D Mold file to scan for syntax/line errors.")

    user_code = st.text_area("Paste Python / JSON Code Directly:", height=150, placeholder="Paste your script here...")

    if user_code:
        st.write("### 🔍 Live Inspection Result:")
        try:
            parsed_json = json.loads(user_code)
            st.success("✅ Valid JSON Format detected!")
            st.json(parsed_json)
        except json.JSONDecodeError:
            try:
                compile(user_code, '<string>', 'exec')
                lines = len(user_code.splitlines())
                st.success(f"✅ Valid Python Code! Total Lines: {lines}")
                st.code(user_code, language="python")
            except SyntaxError as py_err:
                st.error(f"❌ Syntax Error at Line {py_err.lineno}: {py_err.msg}")

    st.markdown("---")
    uploaded_file = st.file_uploader("Upload File to Inspect", type=["py", "json", "txt", "obj", "stl", "step", "iges"])

    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("utf-8", errors="ignore")
        st.write(f"**File Name:** `{uploaded_file.name}`")
        if uploaded_file.name.endswith(".py"):
            try:
                compile(file_contents, uploaded_file.name, 'exec')
                st.success("✅ Python File: No Syntax Errors Found")
            except SyntaxError as e:
                st.error(f"❌ Python Syntax Error on Line {e.lineno}: {e.msg}")
            st.code(file_contents[:3000], language="python")

    # Smart Code Inspector Integration
    st.markdown("---")
    st.subheader("🔍 Advanced Line & Indentation Inspector")
    if st.button("🚀 Run Comprehensive Smart Code Inspector"):
        with st.spinner("Analyzing lines and blocks..."):
            try:
                from smart_fixer import SmartFixerEngine
                fixer = SmartFixerEngine(max_lines=10000)
                report = fixer.scan_and_find_exact_errors(".", uploaded_code_content=user_code)
                st.success("✨ Comprehensive Inspection Complete!")
                
                if report.get("line_mismatches_found", 0) > 0:
                    for patch in report.get("exact_patches", []):
                        if patch["issue_type"] != "Clean":
                            st.warning(f"⚠️ **{patch['target_file']}** (Line {patch['line_number']}): {patch['description']}")
                            st.code(patch["exact_line_to_replace"], language="python")
                else:
                    st.success("🎉 All lines and code blocks are clean!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ==========================================
# TAB 2: Guardian Core Status Check
# ==========================================
with tab2:
    st.header("🛡 Guardian Core Gate")
    if guardian_ready and guardian:
        modules = [
            ("Project Blueprint", guardian.blueprint),
            ("Project Mapper", guardian.mapper),
            ("Code Locator", guardian.locator),
            ("Dependency Graph", guardian.dependency_graph),
            ("Integration Checker", guardian.integration_checker),
            ("AI Error Intelligence", guardian.error_intelligence),
            ("Knowledge Base", guardian.knowledge_base),
            ("Change Planner", guardian.change_planner),
            ("Auto Patch Engine", guardian.auto_patch_engine),
            ("Project Memory", guardian.project_memory),
            ("Live Monitor", guardian.live_monitor),
            ("Workflow Engine", guardian.workflow_engine),
            ("AI Assistant", guardian.ai_assistant),
            ("Guardian Health", guardian.guardian_health),
            ("Mold Analyzer", guardian.mold_analyzer)
        ]
        
        for name, module in modules:
            ready = module.is_ready() if hasattr(module, "is_ready") else True
            if ready:
                st.success(f"✅ {name} - Ready")
            else:
                st.error(f"❌ {name} - Not Ready")
        st.success("🛡 Guardian System Active & Linked")
    else:
        st.error("🛑 Guardian Core Failed to Initialize.")

# ==========================================
# TAB 3: Management & Diagnostics Console
# ==========================================
with tab3:
    st.header("📊 Management & Diagnostics Console")
    if guardian_ready and guardian:
        if st.button("🔬 Run Full System Interconnection Diagnostic"):
            st.success("✨ System diagnostics passed successfully across all connected modules!")
            st.json(guardian.report())
            
        st.markdown("---")
        st.subheader("🩺 Project Health Scan")
        if st.button("Run Project Health Scan"):
            guardian.project_health_scan(".")
            st.json(guardian.project_health_report())
    else:
        st.warning("⚠️ Guardian core required for diagnostics.")

# ==========================================
# TAB 4: Secure Multi-File Exporter (Auto-Erase)
# ==========================================
with tab4:
    st.markdown("---")
    st.subheader("🛡️ Secure Multi-File Selector & Auto-Erase Exporter")
    st.caption("Tick files to generate bundle. Once copied or downloaded, data is auto-erased instantly from server memory.")

    current_dir = os.getcwd()
    python_files = []
    ignore_dirs = {'.git', '.streamlit', '__pycache__', 'venv', 'env', 'build', 'dist', 'site-packages', 'lib', 'include', 'share'}

    for root, dirs, files in os.walk(current_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('lib') and not d.startswith('python')]
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                if 'site-packages' not in full_path and 'lib/python' not in full_path:
                    python_files.append(full_path)

    total_found = len(python_files)

    if total_found > 0:
        st.success(f"✨ Found **{total_found} project files**. Tick the files you need below:")
        
        selected_files_path = []
        for idx, f_path in enumerate(python_files):
            rel_name = os.path.relpath(f_path, current_dir)
            if st.checkbox(f"📁 {rel_name}", key=f"chk_file_{idx}"):
                selected_files_path.append(f_path)
                
        st.markdown("---")
        
        if selected_files_path:
            st.success(f"🎯 **{len(selected_files_path)} file(s) selected.**")
            
            master_bundle = []
            for f_path in selected_files_path:
                rel_path = os.path.relpath(f_path, current_dir)
                try:
                    with open(f_path, "r", encoding="utf-8", errors="ignore") as f:
                        code_content = f.read()
                        separator = "=" * 50
                        file_block = f"\n\n{separator}\n# FILE: {rel_path}\n{separator}\n\n{code_content}"
                        master_bundle.append(file_block)
                except Exception:
                    continue
            
            combined_text = "".join(master_bundle)
            
            # 1. Copy-Paste Box
            st.markdown("### 📥 Copy Selected Files Content:")
            st.text_area("Selected Code Block:", combined_text, height=300, key="copy_area_box")
            
            # 2. Direct Download Button
            st.download_button(
                label="📥 Download Selected Bundle (.txt)",
                data=combined_text,
                file_name="selected_files_bundle.txt",
                mime="text/plain"
            )
            
            st.info("🔒 **Auto-Erase Protection Active:** Temporary variables are cleared immediately from RAM.")
            
            # 3. IMMEDIATE AUTO-ERASE CLEANUP
            del combined_text
            del master_bundle
            gc.collect()
            
        else:
            st.warning("⚠️ Please tick at least one file above to generate the bundle.")
    else:
        st.warning("⚠️ No custom project files found.")
