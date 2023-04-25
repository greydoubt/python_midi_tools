'''
This script generates a new MIDI file with a random sequence of notes, based on the specified parameters. The notes are chosen from a given key and instrument, and include chords played at the beginning of each bar. The generated MIDI file is saved with a name that includes a timestamp based on the length of the file in seconds. You can modify the default parameters and the available keys, chords, and instruments as needed.
'''

#example usage:
# generate_midi_file(bpm=140, length=8, time_sig=(4, 4), key='C', instrument='piano', velocity=80)


import mido
from mido import MidiFile, MidiTrack, Message
import random

# Define the default values for the parameters
DEFAULT_BPM = 120
DEFAULT_LENGTH = 8  # in bars
DEFAULT_TIME_SIG = (4, 4)  # common time
DEFAULT_KEY = 'C'
DEFAULT_INSTRUMENT = 'piano'
DEFAULT_VELOCITY = 64

# Define the available keys and chords for generating MIDI notes
# Each key is a tuple of the MIDI note numbers for the root note of each scale degree
KEYS = {
    'C': (60, 62, 64, 65, 67, 69, 71),
    'D': (62, 64, 66, 67, 69, 71, 73),
    'E': (64, 66, 68, 69, 71, 73, 75),
    'F': (65, 67, 69, 70, 72, 74, 76),
    'G': (67, 69, 71, 72, 74, 76, 78),
    'A': (69, 71, 73, 74, 76, 78, 80),
    'B': (71, 73, 75, 76, 78, 80, 82),
}

CHORDS = {
    'maj': (0, 4, 7),
    'min': (0, 3, 7),
    '7': (0, 4, 7, 10),
    'm7': (0, 3, 7, 10),
}

# Define the available instruments for generating MIDI notes
# Each instrument is a tuple of the MIDI program number and name
INSTRUMENTS = {
    'piano': (0, 'Acoustic Grand Piano'),
    'organ': (16, 'Drawbar Organ'),
    'guitar': (24, 'Acoustic Guitar (nylon)'),
    'bass': (32, 'Acoustic Bass'),
    'strings': (48, 'Strings'),
    'brass': (64, 'Trumpet'),
    'reed': (80, 'Clarinet'),
    'synth_lead': (88, 'Lead 1 (square)'),
    'synth_pad': (96, 'Pad 1 (new age)'),
    'fx': (128, 'FX (rain)'),
}

def generate_midi_file(bpm=DEFAULT_BPM, length=DEFAULT_LENGTH, time_sig=DEFAULT_TIME_SIG, key=DEFAULT_KEY, 
                       instrument=DEFAULT_INSTRUMENT, velocity=DEFAULT_VELOCITY):
    # Calculate the number of ticks per beat based on the BPM and time signature
    ticks_per_beat = mido.bpm2tempo(bpm) // 4
    ticks_per_bar = ticks_per_beat * time_sig[0]
    
    # Generate a random sequence of notes based on the specified length and key
    # Each note is a tuple of the MIDI note number and duration in ticks
    notes = []
    scale_degrees = random.choices(range(7), k=length * time_sig[0])  # choose a random sequence of scale degrees
    root_note = KEYS[key][0]
    for i, degree in enumerate(scale_degrees):
        note_num = KEYS[key][degree] + ((i // time_sig[0]) * 12)  # shift the note up an octave for each new bar
        duration = ticks

    if i % time_sig[0] == 0:  # play a chord at the beginning of each bar
        chord_degrees = random.sample(range(7), 3)  # choose 3 random scale degrees for the chord
        chord_notes = [KEYS[key][d] + ((i // time_sig[0]) * 12) for d in chord_degrees]
        chord_duration = ticks_per_bar
        notes.extend([(n, chord_duration) for n in chord_notes])
        
# Create a new MIDI file and track
filename = f"{key}_{length}bar_{instrument}_{int(mido.tick2second(sum(notes), ticks_per_beat, bpm))}s.mid"
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set the time signature and tempo for the MIDI file
track.append(Message('time_signature', numerator=time_sig[0], denominator=time_sig[1]))
track.append(Message('set_tempo', tempo=mido.bpm2tempo(bpm)))

# Set the instrument for the track
program, program_name = INSTRUMENTS[instrument]
track.append(Message('program_change', program=program))

# Generate the MIDI notes and add them to the track
time = 0
for note, duration in notes:
    track.append(Message('note_on', note=note, velocity=velocity, time=time))
    track.append(Message('note_off', note=note, velocity=velocity, time=duration))
    time = 0

# Save the MIDI file
mid.save(filename)
print(f"Generated {filename}")


