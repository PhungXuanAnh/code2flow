"""
python -m debugpy --listen 0.0.0.0:5678 --wait-for-client analytic.py
"""

import ast
import os


class CallableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.callables = set()
        self.instances = {}
        self.callable_calls = []

    def visit_ClassDef(self, node):
        # Check if the class defines a __call__ method
        for item in node.body:
            if isinstance(item, ast.FunctionDef) and item.name == "__call__":
                self.callables.add(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        # Track instances of classes with __call__ method
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            class_name = node.value.func.id
            if class_name in self.callables:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.instances[target.id] = class_name
        self.generic_visit(node)

    def visit_Call(self, node):
        # Check if the called function is an instance of a class with __call__
        if isinstance(node.func, ast.Name) and node.func.id in self.instances:
            self.callable_calls.append(node)
        elif isinstance(node.func, ast.Attribute):
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id in self.instances
            ):
                self.callable_calls.append(node)
        self.generic_visit(node)


def analyze_code(file_paths):
    callable_visitor = CallableVisitor()

    for file_path in file_paths:
        with open(file_path, "r") as file:
            code = file.read()
            tree = ast.parse(code)
            callable_visitor.visit(tree)

    if callable_visitor.callable_calls:
        print("Found calls to __call__ method:")
        for call in callable_visitor.callable_calls:
            args = [ast.dump(arg) for arg in call.args]
            print(f"Line {call.lineno}: {ast.dump(call)} with arguments {args}")
    else:
        print("No calls to __call__ method found.")


def main():
    # List of file paths to be analyzed
    file_paths = ["adder.py", "main.py"]
    analyze_code(file_paths)


if __name__ == "__main__":
    main()
