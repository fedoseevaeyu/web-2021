from smt.rectangle import Rectangle
from smt.circle import Circle
from smt.square import Square


def main():
    r = Rectangle("синего", 19, 19)
    c = Circle("зеленого", 19)
    s = Square("красного", 19)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()