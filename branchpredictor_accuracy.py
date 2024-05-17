def one_bit_predictor(sequence):
    state = 'N'  # Initialize the predictor to Not Taken
    correct_predictions = 0

    for outcome in sequence:
        if state == outcome:
            correct_predictions += 1
        state = outcome  # Update the state to the last outcome

    accuracy = correct_predictions / len(sequence) * 100
    return accuracy

def two_bit_predictor(sequence):
    state = '00'  # Initialize the predictor to 00 (Not Taken)
    correct_predictions = 0
    state_map = {'00': 'N', '01': 'N', '10': 'T', '11': 'T'}

    for outcome in sequence:
        if state_map[state] == outcome:
            correct_predictions += 1

        # Update the state based on the outcome
        if outcome == 'T':
            if state == '00':
                state = '01'
            elif state == '01':
                state = '10'
            elif state == '10':
                state = '11'
            elif state == '11':
                state = '11'
        else:  # outcome == 'N'
            if state == '11':
                state = '10'
            elif state == '10':
                state = '01'
            elif state == '01':
                state = '00'
            elif state == '00':
                state = '00'

    accuracy = correct_predictions / len(sequence) * 100
    return accuracy

def main():
    # Take user input for the sequence
    input_sequence = input("Enter the sequence of branch outcomes (e.g., TTNNTTNNTTNN): ")
    sequence = input_sequence.upper()

    # Calculate accuracies
    one_bit_accuracy = one_bit_predictor(sequence)
    two_bit_accuracy = two_bit_predictor(sequence)

    # Output the results
    print(f"1-bit Predictor Accuracy: {one_bit_accuracy:.2f}%")
    print(f"2-bit Predictor Accuracy: {two_bit_accuracy:.2f}%")

if __name__ == "__main__":
    main()
