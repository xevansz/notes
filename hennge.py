def main():
    import sys
    
    try:
        in_lines = sys.stdin.read().splitlines()

        def process(index, rem): # processing test cases
            if rem == 0:
                return []

            try:
                X = int(in_lines[index])
            except ValueError:
                raise ValueError(f"Expected int but got {in_lines[index]}.")

            try:
                Yn = list(map(int, in_lines[index+1].split()))
            except ValueError:
                raise ValueError(f"expected int but got {in_lines[index + 1]}.")

            if len(Yn) != X:
                result = "-1"
            else:
                total = sum(map(lambda y: y ** 4 if y<=0 else 0, Yn))
                result = str(total)
            return [result] + process(index + 2, rem - 1)

        N = int(in_lines[0]) # no of test cases

        if len(in_lines) != (2 * N) + 1: # to check if input has correct test cases
            raise IndexError("Input does not match the no of test cases")

        if N == 0: # if no test cases
            raise ValueError("No input provided")

        results = process(1, N)
        print("\n".join(results))

    except ValueError as e:
        print(f"Input error: {e}")
    except IndexError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    main()