import itertools

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

def find_best_sequences_by_absdiff(length):
    
    # Generate all possible sequences of the given length
    outcomes = ['T', 'N']
    all_sequences = itertools.product(outcomes, repeat=length)
    best_diff = 0
    best_sequences = []

    for sequence in all_sequences:
        sequence = ''.join(sequence)
        one_bit_accuracy = one_bit_predictor(sequence)
        two_bit_accuracy = two_bit_predictor(sequence)
        
        # Calculate the difference in accuracies
        accuracy_diff = one_bit_accuracy - two_bit_accuracy

        # Check if this sequence has a better accuracy difference
        if accuracy_diff > best_diff:
            best_diff = accuracy_diff
            best_sequences = [(sequence, one_bit_accuracy, two_bit_accuracy)]
        elif accuracy_diff == best_diff:
            best_sequences.append((sequence, one_bit_accuracy, two_bit_accuracy))

    # Filter to keep only those with the highest 1-bit accuracy
    max_one_bit_accuracy = max(seq[1] for seq in best_sequences)
    final_sequences = [seq for seq in best_sequences if seq[1] == max_one_bit_accuracy]

    return final_sequences, best_diff

def main():
    # Take user input for the sequence length
    length = int(input("Enter the length of the sequence: "))
    
    final_sequences, best_diff = find_best_sequences_by_absdiff(length)

    # Output the best sequences
    print("Best sequences where the 1-bit predictor has the highest accuracy advantage and maximum individual accuracy:")
    for seq, one_acc, two_acc in final_sequences:
        print(f"Sequence: {seq}, 1-bit Accuracy: {one_acc:.2f}%, 2-bit Accuracy: {two_acc:.2f}%, Accuracy Difference: {best_diff:.2f}%")

if __name__ == "__main__":
    main()
