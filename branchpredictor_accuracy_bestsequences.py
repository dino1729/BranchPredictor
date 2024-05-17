import itertools
import matplotlib.pyplot as plt

def one_bit_predictor(sequence):
    state = 'N'
    correct_predictions = 0
    for outcome in sequence:
        if state == outcome:
            correct_predictions += 1
        state = outcome
    accuracy = correct_predictions / len(sequence) * 100
    return accuracy

def two_bit_predictor(sequence):
    state = '00'
    correct_predictions = 0
    state_map = {'00': 'N', '01': 'N', '10': 'T', '11': 'T'}
    for outcome in sequence:
        if state_map[state] == outcome:
            correct_predictions += 1
        if outcome == 'T':
            if state in ['00', '01']:
                state = '10' if state == '01' else '01'
            else:
                state = '11'
        else:
            if state in ['11', '10']:
                state = '01' if state == '10' else '10'
            else:
                state = '00'
    accuracy = correct_predictions / len(sequence) * 100
    return accuracy

def find_best_sequence_by_abshigh(length):
    outcomes = ['T', 'N']
    all_sequences = itertools.product(outcomes, repeat=length)
    favorable_sequences = []

    for sequence in all_sequences:
        sequence = ''.join(sequence)
        one_bit_accuracy = one_bit_predictor(sequence)
        two_bit_accuracy = two_bit_predictor(sequence)
        
        if one_bit_accuracy > two_bit_accuracy:
            favorable_sequences.append(sequence)

    return favorable_sequences

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
    final_sequences = [seq[0] for seq in best_sequences if seq[1] == max_one_bit_accuracy]

    return final_sequences

def plot_sequences(max_length):
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, max_length)
    ax.set_ylim(0.5, max_length + 0.5)
    
    ax.set_xticks(range(max_length + 1))
    ax.set_yticks(range(1, max_length + 1))
    
    for i, length in enumerate(range(1, max_length + 1), start=1):
        best_sequences = find_best_sequences_by_absdiff(length)
        for j, sequence in enumerate(best_sequences):
            colors = ['green' if x == 'T' else 'red' for x in sequence]
            ax.broken_barh([(k, 1) for k in range(len(sequence))], (i, 0.8), facecolors=colors)
            
            # Retrieve accuracies for the sequence
            one_bit_accuracy = one_bit_predictor(sequence)
            two_bit_accuracy = two_bit_predictor(sequence)
            
            # Add text annotation for accuracies
            accuracy_label = f"1-bit: {one_bit_accuracy:.2f}%, 2-bit: {two_bit_accuracy:.2f}%"
            ax.text(max_length + 0.25, i, accuracy_label, verticalalignment='center', fontsize=6)

    ax.set_yticklabels(range(1, max_length + 1))
    ax.set_title('Best Sequences for Each Length Where 1-bit > 2-bit')
    ax.set_xlabel('Position in Sequence')
    ax.set_ylabel('Sequence Length')
    ax.grid(True, which='both', linestyle='-', linewidth=0.5)

    plt.show()

if __name__ == "__main__":
    max_length = int(input("Enter the maximum sequence length: "))
    plot_sequences(max_length)
