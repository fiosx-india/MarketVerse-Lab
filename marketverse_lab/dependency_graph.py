"""
MarketVerse Lab
dependency_graph.py

Purpose:
Build and manage dependency relationships
between project modules.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set
from .project_blueprint import ProjectBlueprint
from .project_mapper import ProjectMapper

@dataclass
class DependencyNode:

    file: str
    imports: List[str] = field(default_factory=list)
    imported_by: List[str] = field(default_factory=list)


class DependencyGraph:

    def __init__(self):

        self.nodes: Dict[str, DependencyNode] = {}

        # Future Connections
        self.blueprint = None
        self.mapper = None
        self.code_locator = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None
        self.test_runner = None
        self.release_checker = None

    # ----------------------------------------

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    # ----------------------------------------

    def connect_mapper(self, mapper):

        self.mapper = mapper

    # ----------------------------------------

    def connect_locator(self, locator):

        self.code_locator = locator

    # ----------------------------------------

    def register_file(self, file_path):

        if file_path not in self.nodes:

            self.nodes[file_path] = DependencyNode(
                file=file_path
            )

        return self.nodes[file_path]

    # ----------------------------------------
    # Add Dependency
    # ----------------------------------------

    def add_dependency(self, file_path, imported_module):

        node = self.register_file(file_path)

        if imported_module not in node.imports:
            node.imports.append(imported_module)

    # ----------------------------------------
    # Build Reverse Dependencies
    # ----------------------------------------

    def build_reverse_dependencies(self):

        for node in self.nodes.values():
            node.imported_by.clear()

        for file_path, node in self.nodes.items():

            for imported in node.imports:

                if imported in self.nodes:
                    self.nodes[imported].imported_by.append(file_path)

        return True
    # ----------------------------------------
    # Build Dependency Graph
    # ----------------------------------------

    def build(self):

        if self.mapper is None:
            return False

        self.nodes.clear()

        for file_path in self.mapper.files.keys():
            self.register_file(file_path)

        self.build_reverse_dependencies()

        return True
    # ----------------------------------------
    # Scan Project Imports
    # ----------------------------------------

    def scan_imports(self, analyzer):

        if self.mapper is None:
            return False

        self.nodes.clear()

        for file_path in self.mapper.files.keys():

            imports = analyzer.analyze(
                Path(self.mapper.root) / file_path
            )

            self.register_file(file_path)

            for module in imports:
                self.add_dependency(file_path, module)

        self.build_reverse_dependencies()

        return True

    # ----------------------------------------
    # Get Dependencies
    # ----------------------------------------

    def dependencies_of(self, file_path):

        if file_path not in self.nodes:
            return []

        return self.nodes[file_path].imports

    # ----------------------------------------
    # Get Reverse Dependencies
    # ----------------------------------------

    def used_by(self, file_path):

        if file_path not in self.nodes:
            return []

        return self.nodes[file_path].imported_by

    # ----------------------------------------
    # Detect Missing Dependencies
    # ----------------------------------------

    def missing_dependencies(self):

        missing = {}

        for file_path, node in self.nodes.items():

            not_found = []

            for module in node.imports:

                if module not in self.nodes:
                    not_found.append(module)

            if not_found:
                missing[file_path] = not_found

        return missing

    # ----------------------------------------
    # Detect Circular Dependencies
    # ----------------------------------------

    def circular_dependencies(self):

        visited = set()
        stack = set()
        cycles = []

        def visit(file_name):

            if file_name in stack:
                cycles.append(file_name)
                return

            if file_name in visited:
                return

            visited.add(file_name)
            stack.add(file_name)

            node = self.nodes.get(file_name)

            if node:

                for dep in node.imports:

                    if dep in self.nodes:
                        visit(dep)

            stack.remove(file_name)

        for file_name in self.nodes.keys():
            visit(file_name)

        return list(set(cycles))

    # ----------------------------------------
    # Impact Analysis
    # ----------------------------------------

    def impact(self, file_path):

        affected = set()

        def collect(target):

            if target not in self.nodes:
                return

            for file in self.nodes[target].imported_by:

                if file not in affected:
                    affected.add(file)
                    collect(file)

        collect(file_path)

        return sorted(affected)

    # ----------------------------------------
    # Broken Connections
    # ----------------------------------------

    def broken_connections(self):

        report = {}

        for file_path, node in self.nodes.items():

            broken = []

            for dep in node.imports:

                if dep not in self.nodes:
                    broken.append(dep)

            if broken:
                report[file_path] = broken

        return report

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "registered_files": len(self.nodes),
            "missing_dependencies": len(self.missing_dependencies()),
            "circular_dependencies": len(self.circular_dependencies())
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "statistics": self.statistics(),
            "broken_connections": self.broken_connections(),
            "missing_dependencies": self.missing_dependencies(),
            "circular_dependencies": self.circular_dependencies()
        }

    # ----------------------------------------
    # Export Graph
    # ----------------------------------------

    def export(self):

        graph = {}

        for file_name, node in self.nodes.items():

            graph[file_name] = {
                "imports": node.imports,
                "imported_by": node.imported_by
            }

        return graph

    # ----------------------------------------
    # Complete Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "graph": self.export()
        }

    # ----------------------------------------
    # Reset Graph
    # ----------------------------------------

    def reset(self):

        self.nodes.clear()

        return True

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return (
            self.blueprint is not None and
            self.mapper is not None and
            len(self.nodes) > 0
        )

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"DependencyGraph("
            f"Files={len(self.nodes)}, "
            f"Missing={len(self.missing_dependencies())}, "
            f"Circular={len(self.circular_dependencies())})"
        )

    __repr__ = __str__
