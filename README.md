# python_midi_tools
suite of midi tools for python


This script first defines the command line arguments using argparse. If the --bpm and --key arguments are given, it calls the transpose_midi_file() function to transpose the MIDI file. Otherwise, it calls the get_midi_info() function to show information about the MIDI file, and the plot_midi_file() function to generate a visualization of the MIDI file.

If no command line arguments are given, it enters a loop that shows a menu with three choices: show MIDI file info, show MIDI file visualization, and transpose MIDI file. It uses the input() function to prompt the user for input and calls the appropriate function based on the user's choice. The loop continues until the user chooses to quit.

To run this command line tool, you can simply call python main.py with the appropriate arguments. For example, to show the info for a MIDI file called my_song.mid, you would run:

*python main.py my_song.mid my_song_info.txt

This would show the info for the MIDI file and save it to a text file called my_song_info.txt.

To transpose the same MIDI file to a target BPM of 120 and key of D, you would run:

*python main.py my_song.mid my_song_transposed.mid -b 120 -k D

This would transpose the MIDI file and save the output to a new MIDI file called my_song_transposed.mid.

And to show a visualization of the same MIDI file, you would run:

*python main.py my_song.mid my_song_visualization.png

This would generate a visualization of the MIDI file and save it to a PNG file called my_song_visualization.png.
