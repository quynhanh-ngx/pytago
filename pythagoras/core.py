import ast

from pythagoras import go_ast


def python_to_go(python: str) -> str:
    tree = ast.parse(python)
    go_code = go_ast.unparse(tree)
    return go_code


# Debugging
if __name__ == '__main__':
    print(python_to_go("""\
def main():
    a = [1, 2, 3]
    for v in a:
        print(v)

    for i, v in enumerate(a):
        print(i + v)

    for i in range(5):
        print(i)

    for i in range(10, 15):
        print(i)

    for i in range(10, 15, 2):
        print(i)

    for j in range(15, 10, -1):
        print(j)

    for j in range(15, 10, -2):
        print(j)

if __name__ == '__main__':
    main()

"""))
