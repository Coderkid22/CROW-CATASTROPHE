import ast
import astunparse



tree = ast.parse(text)
argumentIndexNumber = 0
class ChangeImageFunctionCall(ast.NodeTransformer):
    def callFunctionForEachFunctionCallinTree(self, node):
        if 42 <= node.lineo <= 62:
            if isinstance(node.func, ast.Name) and node.func.id == 'image':
                # just for readiblity argumentIndexNumber = 0
                variableName = node.args[argumentIndexNumber].s
                secondArgument = node.args[argumentIndexNumber + 1]
                thirdArgument = node.args[argumentIndexNumber + 2]
                newFunctionCall = ast.parse(f'{variableName} = image({secondArgument}, {thirdArgument})')
                return newFunctionCall
            return node


with open('Code/first-game.py', 'r') as file:
    tree = ast.parse(file.read())

tree = ChangeImageFunctionCall().visit(tree)

with open('Code/first-game.py', 'w') as file:
    file.write(astunparse.unparse(tree))