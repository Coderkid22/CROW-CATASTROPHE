import ast

with open(filePath, 'f') as file:
    text = file.readlines()

tree = ast.parse(text)

class functionCallEachTime(ast.NodeVisitor):
    def callFunctionForEachFunctionCallinTree(self, node):
        if 42 <= node.lineo <= 62:
            if node.args:
                firstArgument = node.args[0]
                if isinstance(firstArgument, ast.Name):
                    node.args[0] = ast.Str(firstArgument.id)
        self.generic_visit(node)
call = functionCallEachTime()
call.visit(tree)
