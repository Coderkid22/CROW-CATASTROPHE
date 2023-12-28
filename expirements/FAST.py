import ast
import astunparse
import shutil
import sys

source_file = 'expirements/testFile_for_automationScripts.py'
target_file = 'expirements/testFile_for_automationScripts.py'

class ImageFunctionTransformer(ast.NodeTransformer):
    """AST transformer that changes image function calls."""
    def visit_Call(self, node):
        if 42 <= node.lineno <= 62 and isinstance(node.func, ast.Name) and node.func.id == 'image':
            variable_name = node.args[0].s
            second_argument = node.args[1].s
            third_argument = node.args[2].s
            new_function_call = ast.parse(f'{variable_name} = image({second_argument}, {third_argument})').body[0].value
            return new_function_call
        return node

def transform_code(source_file, target_file):
    """
    Transforms the code in the source file and writes the result to the target file.
    """
    try:
        with open(source_file, 'r') as file:
            code = file.read()

        tree = ast.parse(code)
        tree = ImageFunctionTransformer().visit(tree)

        with open(target_file, 'w') as file:
            file.write(astunparse.unparse(tree))
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        sys.exit(1)
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
        transform_code(source_file, target_file)
        sys.exit(1)

    try:
        # some code here
    except Exception as e:
        # handle the exception here

if __name__ == "__main__":
    transform_code(source_file, target_file)
transform_code(source_file, target_file)
transform_code(source_file, target_file)