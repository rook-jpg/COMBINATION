import itertools


def get_options(category_number):
    """Ask the user for options for one category."""
    while True:
        user_input = input(
            f"Enter options for Category {category_number}, separated by commas: "
        ).strip()

        # Handle empty input
        if not user_input:
            print("Please enter at least one option.")
            continue

        # Split by commas and remove extra spaces
        options = [option.strip() for option in user_input.split(",")]

        # Remove empty options
        options = [option for option in options if option]

        if options:
            return options

        print("Please enter at least one valid option.")


def main():
    categories = []
    category_number = 1

    print("=== Combination Generator ===")
    print("Enter your options for each category.")
    print("Example: Ali, Ahmed, Hassan\n")

    # Collect categories from the user
    while True:
        options = get_options(category_number)
        categories.append(options)

        while True:
            answer = input("Add another category? y/n: ").strip().lower()

            if answer in ("y", "n"):
                break

            print("Please enter 'y' or 'n'.")

        if answer == "n":
            break

        category_number += 1

    # Generate all possible combinations
    combinations = itertools.product(*categories)

    # Save combinations to the file
    count = 0

    with open("combinations.txt", "w", encoding="utf-8") as file:
        for combination in combinations:
            file.write(" - ".join(combination) + "\n")
            count += 1

    print(f"\nDone! {count} combinations saved to combinations.txt")


if __name__ == "__main__":
    main()
