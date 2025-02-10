# RPNLang

RPNLang is a simple stack-based programming language inspired by **Reverse Polish Notation (RPN)**. It supports arithmetic operations, variable assignments, and basic control flow using `while` loops.

## Features

- Supports basic arithmetic operations (`+`, `-`, `*`, `/`).
- Uses **RPN-style expressions**, where operators follow their operands.
- Allows variable assignments.
- Implements `while` loops for control flow.
- Handles division by zero with appropriate error messages.

## Syntax Overview

### Variable Assignment

```rpn
x = 5 1 2 + 4 * + 3 -
```

This assigns `x` the result of the expression: `5 + ((1 + 2) * 4) - 3`.

### Using Variables in Expressions

```rpn
y = x 3 * 10 2 / +
```

Here, `y` is assigned the result of: `(x * 3) + (10 / 2)`.

### Conditional and Loops

```rpn
while x 10 >=
  x = x 1 -
end
```

This loop decrements `x` by 1 until `x < 10`.

## Implementation Details

- **Stack-based execution**: Operands are pushed onto a stack, and operators pop values from the stack to compute results.
- **Variable storage**: Variables are stored in a dictionary (`self.vars`).
- **Operator handling**: Arithmetic operations use Python’s `operator` module.
- **Error handling**: Detects division by zero and missing operands.
- **Control flow**: Implements a `while` loop using program counter tracking.

## Running RPNLang Code

To execute an RPNLang script:

```sh
python rpnlang.py script.txt
```

where `script.txt` contains RPNLang code.

## Example Script (`example.txt`)

```
x = 20
while x 10 >=
  x = x 2 -
end
y = x 5 +
```

Running this script will result in:

```sh
{'x': 8, 'y': 13}
```

## Future Enhancements

- Implement functions and user-defined procedures.
- Add support for logical operators (`AND`, `OR`, `NOT`).
- Expand control flow with `if-else` statements.

---

RPNLang is a simple yet powerful language for learning stack-based evaluation and control flow! 🚀
