"""
# Rockbeat Language Compiler

## Description

A simple music programming language for defining drum patterns and structures.

## Version

0.1

## Author

[Eliezer Solinger]

## Properties

### Syntax

- The language uses English alphabets as symbolic representations of drum kit components.
- Special characters are used to control the flow of the program and to provide additional functionalities.

### Comments

- # or // can be used to add comments to the program.

### Tempo and Bars

- The BPM keyword followed by a number is used to set the tempo of the song.
- The bars keyword followed by a number is used to set the number of bars the song will have.

### Patterns

- Patterns are defined with a name followed by a set of beats inside braces {}.
- Each bar is represented by a single line inside the braces.
- Each line can contain multiple groups of letters separated by spaces, each LETTER representing a different drum instrument that is hit on that beat and each group representing a bar.
- The - character can be used to represent an empty beat.
- A pattern can call other patterns, allowing for the creation of complex rhythms.

### Playing Patterns

- The @ symbol followed by a pattern name is used to play that pattern.
- There is no specific 'main' function or pattern. The program will start playing the first pattern it encounters.

## Symbol Table

- K - Kick Drum
- S - Snare Drum
- H - Hi-Hat (closed)
- O - Hi-Hat (open)
- T - High Tom
- M - Mid Tom
- L - Low Tom (or Floor Tom)
- C - Crash Cymbal
- R - Ride Cymbal
- B - Bell of the Ride Cymbal 

"""

 
def parse_program(program): 
    beats=4
    bars=4
    BPM=120
    # Initialize the patterns dictionary
    # and the stack for nested patterns
    patterns=[] 
    patterns_dict = {}
    patterns_stack = [
        "main"
    ]
    current_pattern = "main" 
    for line in program.splitlines():
        line = line.strip()
        line = ' '.join(line.split())
        # Ignore comments after '#' or '//'

        if '#' in line:
            line = line.split('#', 1)[0].strip()
        if '//' in line:
            line = line.split('//', 1)[0].strip()

        # Ignore empty  
        if not line: continue

        parts= line.split()
    
        if parts[0] == 'BPM':
            BPM = int(parts[1])
            continue
        if parts[0] == 'bars':
            bars = int(parts[1])
            continue

        if parts[0] == 'beats':
            beats = int(parts[1])
            continue

        if parts[0] == 'tempo' and line.has('/'):
            # tempo is in the format "beats/bars"
            # e.g., "4/4" or "3/4"
            tempo_parts= parts[1].split('/') 
            beats = int(tempo_parts[0])
            bars = int(tempo_parts[1])
            continue

        if line.endswith('{'):
            pattern_name = line.rstrip('{').strip()
            patterns_stack.append(pattern_name)
            current_pattern = pattern_name
            patterns_dict[current_pattern] = []
            continue

        if line == '}' and patterns_stack:
            patterns_stack.pop()
            if patterns_stack:
                current_pattern = patterns_stack[-1]
            continue

        if current_pattern not in patterns_dict:
            patterns_dict[current_pattern] = []
         
        # Add the line to the current pattern
        for beat in line.strip().split(' '):
            patterns_dict[current_pattern].append(beat)
    return {
        'BPM': BPM,
        'bars': bars,
        'beats': beats,
        'patterns': patterns_dict,
    }

        
