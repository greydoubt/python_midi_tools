import mido

def transpose_midi_file(filename, target_bpm, target_key):
    midi_file = mido.MidiFile(filename)
    
    # Calculate the ratio between the original and target BPMs
    original_bpm = None
    for msg in midi_file:
        if msg.type == 'set_tempo':
            microseconds_per_beat = msg.tempo
            original_bpm = mido.tempo2bpm(microseconds_per_beat)
            break
    
    if original_bpm is None:
        raise ValueError('Could not find original BPM in MIDI file')
    
    bpm_ratio = target_bpm / original_bpm
    
    # Calculate the number of semitones to transpose based on the original and target keys
    if target_key == 'Unknown':
        target_key_num = None
    else:
        target_key_num = mido.key_name_to_value(target_key)
    
    current_key_num = None
    current_key_signature_msgs = [msg for msg in midi_file.tracks[0] if msg.type == 'key_signature']
    if current_key_signature_msgs:
        current_key_num = current_key_signature_msgs[-1].key
    
    if target_key_num is not None and current_key_num is not None:
        key_diff = target_key_num - current_key_num
    else:
        key_diff = 0
    
    # Transpose each note in each track by the appropriate amount
    for track in midi_file.tracks:
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                msg.note += key_diff
                msg.time = int(msg.time * bpm_ratio)
    
    # Save the transposed MIDI file to disk
    transposed_filename = filename[:-4] + '_transposed.mid'
    midi_file.save(transposed_filename)
    
    return transposed_filename
