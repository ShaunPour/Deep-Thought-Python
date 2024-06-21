def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.lower().lstrip().rstrip() == "42"  or answer.lower().lstrip().rstrip() == "forty-two" or answer.lower().lstrip().rstrip() == "forty two":
        print("Yes")
    else:
        print("No")

main()
