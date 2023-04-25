import mido

def get_midi_info(filename):
    midi_file = mido.MidiFile(filename)
    
    # Get the BPM of the MIDI file
    for msg in midi_file:
        if msg.type == 'set_tempo':
            microseconds_per_beat = msg.tempo
            bpm = mido.tempo2bpm(microseconds_per_beat)
            break
    
    # Get the key of the MIDI file
    # (Note: This assumes that the MIDI file only has one track)
    key_signature_msgs = [msg for msg in midi_file.tracks[0] if msg.type == 'key_signature']
    if key_signature_msgs:
        key = key_signature_msgs[-1].key
    else:
        key = 'Unknown'
    
    # Get the number of tracks in the MIDI file
    num_tracks = len(midi_file.tracks)
    
    return bpm, key, num_tracks
