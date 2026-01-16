# -*- coding: utf-8 -*-
"""
A simple CLI tool for base-20 ↔ base-10 arithmetic (TI-Nspire friendly: no f-strings).
"""

DIGITS_BASE20 = "0123456789ABCDEFGHIJ"

# Prefer an escape so the source stays robust if the editor is picky.
# If your Python can display it, this prints as "≡≡".
TRIPLE_BAR = "\u2261"
BAR_15 = TRIPLE_BAR + TRIPLE_BAR


def base20_to_decimal(s):
    """Convert a base-20 (vegisemal) string to decimal (supports leading '-')."""
    s = s.strip().upper()
    neg = False
    if s.startswith("-"):
        neg = True
        s = s[1:]

    result = 0
    for ch in s:
        if ch not in DIGITS_BASE20:
            raise ValueError("Invalid digit '{0}' for base-20".format(ch))
        result = result * 20 + DIGITS_BASE20.index(ch)

    return -result if neg else result


def decimal_to_base20(n):
    """Convert a decimal (base-10) integer to base-20."""
    if n == 0:
        return "0"

    neg = n < 0
    n = abs(n)

    out = ""
    while n > 0:
        out = DIGITS_BASE20[n % 20] + out
        n //= 20

    return "-" + out if neg else out


def mayan_digit_lines_compact(d):
    """
    Compact Mayan-ish digit for base-20:
      dots: 1 '.'  2 ':'  3 ':.'  4 '::'
      bars: 1 '__' 2 '==' 3 '≡≡'  (represents 5,10,15)
      zero: '0'
    Layout:
      [dots line (optional)]
      [bar line (optional)]
    """
    if not (0 <= d <= 19):
        raise ValueError("Digit out of range for base-20 (0..19)")

    dot_glyph = {0: "", 1: ".", 2: ":", 3: ":.", 4: "::"}
    bar_glyph = {0: "", 1: "__", 2: "==", 3: BAR_15}

    if d == 0:
        return ["0"]

    bars = d // 5          # 0..3
    dots = d % 5           # 0..4

    lines = []
    if dots:
        lines.append(dot_glyph[dots])
    if bars:
        lines.append(bar_glyph[bars])
    return lines


def decimal_to_base20_digits(n):
    """Return base-20 digits (most significant first) for abs(n)."""
    n = abs(n)
    if n == 0:
        return [0]
    ds = []
    while n > 0:
        ds.append(n % 20)
        n //= 20
    ds.reverse()
    return ds


def mayan_number(n):
    """
    Stack base-20 digits (most significant on top), with a blank line between digits.
    """
    neg = n < 0
    digits = decimal_to_base20_digits(n)

    blocks = []
    for d in digits:
        blocks.append("\n".join(mayan_digit_lines_compact(d)))

    out = "\n\n".join(blocks)
    return ("NEGATIVE\n" + out) if neg else out


def calculate(a, b, operator, base):
    """Perform arithmetic on two numbers in base-20 or base-10, return result string."""
    # Convert inputs to decimal first
    if base == "20":
        da = base20_to_decimal(a)
        db = base20_to_decimal(b)
    else:
        da = int(a)
        db = int(b)

    # Perform arithmetic
    if operator == "+":
        res = da + db
    elif operator == "-":
        res = da - db
    elif operator == "*":
        res = da * db
    elif operator == "/":
        if db == 0:
            raise ZeroDivisionError("division by zero")
        res = da // db  # integer division
    else:
        raise ValueError("Unsupported operator")

    # Print Mayan representation every time
    print("\nMAYAN (compact):")
    print(mayan_number(res))

    # Return result in both
    return "Decimal: {0}, Base-20: {1}".format(res, decimal_to_base20(res))


def main():
    print("Base-20 ↔ Base-10 Calculator")
    base = input("Enter base of input numbers (10 or 20): ").strip()
    a = input("First number: ").strip()
    op = input("Operator (+ - * /): ").strip()
    b = input("Second number: ").strip()

    try:
        out = calculate(a, b, op, base)
        print("\nRESULT →", out)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

