"""
This script first defines the command line arguments using argparse. If the --bpm and --key arguments are given, it calls the transpose_midi_file() function to transpose the MIDI file. Otherwise, it calls the get_midi_info() function to show information about the MIDI file, and the plot_midi_file() function to generate a visualization of the MIDI file.

If no command line arguments are given, it enters a loop that shows a menu with three choices: show MIDI file info, show MIDI file visualization, and transpose MIDI file. It uses `
"""



import os
import sys
import argparse
import mido
from midi_info import get_midi_info
from midi_transpose import transpose_midi_file
from midi_visualization import plot_midi_file


def main():
    # Define the command line arguments
    parser = argparse.ArgumentParser(description='Process a MIDI file.')
    parser.add_argument('input_file', type=str, help='the input MIDI file')
    parser.add_argument('output_file', type=str, help='the output file')

    # Add an optional argument for the target BPM and key
    parser.add_argument('-b', '--bpm', type=int, help='the target BPM')
    parser.add_argument('-k', '--key', type=str, help='the target key')

    # Parse the command line arguments
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.exists(args.input_file):
        print(f'Error: {args.input_file} does not exist')
        sys.exit(1)

    # If the target BPM and key are specified, transpose the MIDI file
    if args.bpm is not None and args.key is not None:
        transpose_midi_file(args.input_file, args.output_file, args.bpm, args.key)

    # Otherwise, show the MIDI file info and visualization
    else:
        # Show the MIDI file info
        get_midi_info(args.input_file)

        # Plot the MIDI file visualization
        plot_midi_file(args.input_file, args.output_file)


if __name__ == '__main__':
    # If no command line arguments are given, show a menu with three choices
    if len(sys.argv) == 1:
        while True:
            print('Select an option:')
            print('1. Show MIDI file info')
            print('2. Show MIDI file visualization')
            print('3. Transpose MIDI file')
            print('4. Quit')
            choice = input('Enter your choice (1-4): ')

            if choice == '1':
                input_file = input('Enter the path to the input MIDI file: ')
                get_midi_info(input_file)
                break

            elif choice == '2':
                input_file = input('Enter the path to the input MIDI file: ')
                output_file = input('Enter the path to the output PNG file: ')
                plot_midi_file(input_file, output_file)
                break

            elif choice == '3':
                input_file = input('Enter the path to the input MIDI file: ')
                output_file = input('Enter the path to the output MIDI file: ')
                bpm = input('Enter the target BPM: ')
                key = input('Enter the target key: ')
                transpose_midi_file(input_file, output_file, int(bpm), key)
                break

            elif choice == '4':
                sys.exit(0)

            else:
                print('Invalid choice')

    # Otherwise, run the main function with the command line arguments
    else:
        main()