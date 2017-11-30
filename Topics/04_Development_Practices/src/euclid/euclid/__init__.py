__all__ = [ "GCD", "main" ] # names exported by module

from .gcd import GCD        # relative import within module
import sys

def main():
    try: # Take the two first command-line args, as integers.
        ax = int(sys.argv[1])
        bx = int(sys.argv[2])
        print(GCD(ax, bx))
    except IndexError:
        print("Euclid requires two arguments.")
    except ValueError:
        print("Euclid requires two integers.")
    except ArithmeticError:
        print("Euclid requires positive integers.")

if __name__ == "__main__":
    main()