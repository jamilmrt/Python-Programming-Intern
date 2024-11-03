def countWords(text):
    """
    Counts the number of words in the given text.

    Parameters:
    text (str): The input text to count words from.

    Returns:
    int: The number of words in the text.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    return len(words)


def main():
    """
    Main function to execute the Word Counter program.
    """
    # Prompt the user for input
    userInput = input("Please enter a sentence or paragraph: ").strip()

    # Check for empty input
    if not userInput:
        print("Error: You entered an empty input. Please enter a valid sentence or paragraph.")
        return  # Exit the function if input is empty

    # Count the number of words using the count_words function
    wordCount = countWords(userInput)

    # Display the result
    print(f"The number of words in your input is: {wordCount}")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()