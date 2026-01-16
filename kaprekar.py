# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 12:47:19 2025

@author: maita
"""

def kaprekar_step(n, width):
    """Perform one Kaprekar step for a number of given width."""
    s = f"{n:0{width}d}"  # zero‑pad to width
    asc = int("".join(sorted(s)))
    desc = int("".join(sorted(s, reverse=True)))
    return desc - asc, desc, asc

def run_kaprekar(n):
    """Run Kaprekar's routine for 3‑ or 4‑digit numbers."""
    s = str(n)

    if len(s) not in (3, 4):
        raise ValueError("Number must be 3 or 4 digits.")

    if len(set(s)) == 1:
        raise ValueError("Digits must not all be identical.")

    width = len(s)
    kaprekar_constant = 495 if width == 3 else 6174

    print(f"\nKaprekar routine for {width}-digit number {n}:\n")

    seen = set()
    current = n

    while True:
        result, desc, asc = kaprekar_step(current, width)
        print(f"{desc} - {asc} = {result}")

        if result == kaprekar_constant:
            print(f"\nReached Kaprekar constant: {kaprekar_constant}")
            break

        if result in seen:
            print("\nEntered a loop (unexpected for valid input).")
            break

        seen.add(result)
        current = result

# --- Main program ---
if __name__ == "__main__":
    user_input = input("Enter a 3- or 4-digit number: ").strip()

    if not user_input.isdigit():
        print("Input must be numeric.")
    else:
        run_kaprekar(int(user_input))
        
        
        
"""ti-version"""

# Kaprekar routine for 3- and 4-digit numbers
# TI‑Nspire‑compatible version (no f-strings, no zfill, no sets)

def kaprekar_step(n, width):
    # Zero-pad using TI-safe formatting
    s = ("%0" + str(width) + "d") % n

    # TI requires list() around sorted() to avoid NoneType issues
    asc_str = "".join(list(sorted(s)))
    desc_str = "".join(list(sorted(s, reverse=True)))

    asc = int(asc_str)
    desc = int(desc_str)

    return desc - asc, desc, asc


def run_kaprekar(n):
    s = str(n)
    width = len(s)

    if width not in (3, 4):
        print("Number must be 3 or 4 digits.")
        return

    if len(set(s)) == 1:
        print("Digits must not all be identical.")
        return

    # Kaprekar constants
    if width == 3:
        constant = 495
    else:
        constant = 6174

    print("")
    print("Kaprekar routine for " + str(width) + "-digit number " + str(n) + ":")
    print("")

    seen = []   # TI-safe replacement for set()

    current = n

    while True:
        result, desc, asc = kaprekar_step(current, width)

        # Explicit str() casts for TI concatenation
        print(str(desc) + " - " + str(asc) + " = " + str(result))

        if result == constant:
            print("")
            print("Reached Kaprekar constant: " + str(constant))
            break

        if result in seen:
            print("")
            print("Entered a loop (unexpected for valid input).")
            break

        seen.append(result)
        current = result


# --- Auto-run on TI-Nspire (no __main__) ---
try:
    user_input = input("Enter a 3- or 4-digit number: ").strip()
    run_kaprekar(int(user_input))
except:
    pass