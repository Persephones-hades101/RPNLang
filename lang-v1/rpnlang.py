import sys
import operator


class RPN_Lang():
    def __init__(self):
        self.vars = {}
        self.ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division by zero is not allowed!"))
        }

    def RPN_Lang(self, s):

        lines = [x for x in s.split("\n") if x.strip() != ""]
        pc = 0
        # print(lines)
        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case 'while':
                    if self.rpn_lang_expr(line.split(maxsplit=1)[1]) == 1:
                        pc += 1
                    else:
                        while lines[pc].split(maxsplit=1)[0] != 'end':
                            pc += 1
                        pc += 1
                case 'end':
                    while lines[pc].split(maxsplit=1)[0] != 'while':
                        pc -= 1
                case _:
                    (name, _, expr) = line .split(maxsplit=2)
                    self.vars[name] = self.rpn_lang_expr(expr)
                    pc += 1

        print(self.vars)

    def rpn_lang_expr(self, s):
        tokens = s.split()
        stack = []
        for tok in tokens:
            # print(tok)
            if tok.isdigit():
                stack.append(int(tok))
            elif tok in self.vars:
                stack.append(self.vars[tok])
            elif tok in self.ops:
                if (len(stack) < 2):
                    raise ValueError(f"Not enough operands for '{tok}'")
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(self.ops[tok](lhs, rhs))
            elif tok == ">=":
                rhs = stack.pop()
                lhs = stack.pop()
                if lhs >= rhs:
                    stack.append(1)
                else:
                    stack.append(0)

            else:
                raise ValueError(f"Unknown token: {tok}")

        return stack[0]


RPN_Lang().RPN_Lang(open(sys.argv[1]).read())
