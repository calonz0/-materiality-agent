import os
import ast
import sys
import re
from collections import defaultdict

# =========================
# HEADER
# =========================
def print_header():
    print("\n==============================")
    print(" DEV X-RAY — CODEBASE ANALYZER")
    print("==============================\n")


# =========================
# READ CONTEXT FILE
# =========================
def read_system_context(base_path):
    context_path = os.path.join(base_path, "SYSTEM_CONTEXT.md")

    if not os.path.exists(context_path):
        return None

    try:
        with open(context_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Error reading SYSTEM_CONTEXT.md"


# =========================
# DIRECTORY SCAN
# =========================
def scan_directory(base_path):
    structure = defaultdict(list)

    for root, dirs, files in os.walk(base_path):
        rel_path = os.path.relpath(root, base_path)
        structure[rel_path].extend(files)

    return structure


# =========================
# PYTHON ANALYSIS
# =========================
def analyze_python_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except:
        return None

    imports = []
    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return {
        "imports": sorted(set(imports)),
        "functions": functions,
        "classes": classes
    }


# =========================
# JS ANALYSIS
# =========================
def analyze_js_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return None

    functions = re.findall(r'function\s+(\w+)', content)
    arrow_functions = re.findall(r'(\w+)\s*=\s*\(?.*?\)?\s*=>', content)
    fetch_calls = re.findall(r'fetch\(["\'](.*?)["\']', content)

    return {
        "functions": list(set(functions + arrow_functions)),
        "fetch_calls": fetch_calls
    }


# =========================
# HTML ANALYSIS
# =========================
def analyze_html_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return None

    scripts = re.findall(r'<script.*?src=["\'](.*?)["\']', content)
    fetch_calls = re.findall(r'fetch\(["\'](.*?)["\']', content)

    return {
        "scripts": scripts,
        "fetch_calls": fetch_calls
    }


# =========================
# SCAN FILES
# =========================
def scan_files(base_path):
    results = {
        "python": {},
        "js": {},
        "html": {}
    }

    for root, dirs, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)

            if file.endswith(".py"):
                results["python"][full_path] = analyze_python_file(full_path)

            elif file.endswith(".js"):
                results["js"][full_path] = analyze_js_file(full_path)

            elif file.endswith(".html"):
                results["html"][full_path] = analyze_html_file(full_path)

    return results


# =========================
# PRINTING
# =========================
def print_structure(structure):
    print("📁 PROJECT STRUCTURE:\n")
    for path, files in structure.items():
        print(f"{path}/")
        for f in files:
            print(f"  - {f}")


def print_python_analysis(data):
    print("\n🐍 PYTHON ANALYSIS:\n")
    for file, info in data.items():
        if not info:
            continue
        print(f"{file}")
        print(f"  Imports: {info['imports']}")
        print(f"  Functions: {info['functions']}")
        print(f"  Classes: {info['classes']}\n")


def print_js_analysis(data):
    print("\n🟨 JS ANALYSIS:\n")
    for file, info in data.items():
        if not info:
            continue
        print(f"{file}")
        print(f"  Functions: {info['functions']}")
        print(f"  Fetch calls: {info['fetch_calls']}\n")


def print_html_analysis(data):
    print("\n🌐 HTML ANALYSIS:\n")
    for file, info in data.items():
        if not info:
            continue
        print(f"{file}")
        print(f"  Scripts: {info['scripts']}")
        print(f"  Fetch calls: {info['fetch_calls']}\n")


def print_context(context):
    print("\n🧠 SYSTEM CONTEXT:\n")

    if not context:
        print("No SYSTEM_CONTEXT.md found.\n")
        return

    print(context[:1500])  # muestra los primeros 1500 caracteres


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    print_header()

    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.getcwd()

    print(f"Analyzing: {base_path}\n")

    structure = scan_directory(base_path)
    analysis = scan_files(base_path)
    context = read_system_context(base_path)

    print_structure(structure)
    print_python_analysis(analysis["python"])
    print_js_analysis(analysis["js"])
    print_html_analysis(analysis["html"])
    print_context(context)

    print("\n==============================")
    print(" END OF REPORT")
    print("==============================\n")
