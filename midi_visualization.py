import mido
import matplotlib.pyplot as plt
import numpy as np

def visualize_midi_file(filename):
    midi_file = mido.MidiFile(filename)
    
    # Create a list of lists, where each sub-list represents a track
    # Each sub-list contains tuples of (time, note, velocity)
    tracks = []
    for track in midi_file.tracks:
        track_data = []
        time = 0
        for msg in track:
            time += msg.time
            if msg.type == 'note_on':
                track_data.append((time, msg.note, msg.velocity))
        tracks.append(track_data)
    
    # Plot each track as a separate subplot
    fig, axes = plt.subplots(len(tracks), 1, figsize=(8, 6), sharex=True)
    fig.subplots_adjust(hspace=0.4)
    for i, track_data in enumerate(tracks):
        ax = axes[i] if len(tracks) > 1 else axes
        ax.set_title(f'Track {i+1}')
        ax.set_ylabel('Note')
        ax.set_ylim(0, 127)
        ax.yaxis.set_ticks(np.arange(0, 128, 12))
        
        for note_data in track_data:
            # Add a rectangle for each note
            rect = plt.Rectangle((note_data[0], note_data[1]), 1, 1, color='black')
            ax.add_patch(rect)
        
        # Add labels for octave numbers
        for octave in range(11):
            y = octave * 12
            ax.text(0, y, f'{octave}')
    
    # Set the x-axis limits to match the length of the longest track
    max_time = max([max(track_data, default=(0, 0, 0))[0] for track_data in tracks])
    plt.xlim(0, max_time)
    
    # Add an x-axis label for time in seconds
    plt.xlabel('Time (s)')
    
    # Save the plot to a PNG file
    png_filename = filename[:-4] + '.png'
    plt.savefig(png_filename)
    
    return png_filename
