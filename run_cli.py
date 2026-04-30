from app import Compiler

def main():
    print("INTEGER LITERAL COMPILER (CLI MODE)")
    print("=" * 50)
    print("Type 'exit' to quit\n")

    compiler = Compiler()

    while True:
        try:
            source = input("Enter input: ").strip()

            if source.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not source:
                continue

            compiler.compile(source)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()