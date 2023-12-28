import ast
import astunparse
import shutil

shutil.copy('source path', 'copy path')

with open('Code/first-game.py', 'r') as file:
    code = file.read()

tree = ast.parse(code)

class ChangeImageFunctionCall(ast.NodeTransformer):
    def visit_Call(self, node):
        if 42 <= node.lineno <= 62:
            if isinstance(node.func, ast.Name) and node.func.id == 'image':
                variableName = node.args[0].s
                secondArgument = node.args[1]
                thirdArgument = node.args[2]
                newFunctionCall = ast.parse(f'{variableName} = image({secondArgument}, {thirdArgument})')
                return newFunctionCall
            return node

tree = ChangeImageFunctionCall().visit(tree)

with open('Code/first-game.py', 'w') as file:
    file.write(astunparse.unparse(tree))