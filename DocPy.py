#!/usr/bin/python3
import ast
import sys

def add_docstring(filename):
    with open(filename, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    class DocStringAdder(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if not node.body or not isinstance(node.body[0], ast.Expr) or not isinstance(node.body[0].value, ast.Str):
                # If function has no body or the first statement is not a docstring
                # Add a docstring with function name
                docstring_value = ast.Str(s=f'Documentation for {node.name}')
                new_docstring = ast.Expr(value=docstring_value)
                new_docstring.lineno = node.lineno
                new_docstring.col_offset = node.col_offset
                node.body = [new_docstring] + node.body
            return node

    transformer = DocStringAdder()
    tree = transformer.visit(tree)

    with open(filename, 'w') as file:
        file.write(ast.unparse(tree))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    add_docstring(filename)
