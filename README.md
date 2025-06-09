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
- Each beat is represented by a single line inside the braces.
- Each line inside a pattern can contain multiple groups of letters separated by spaces. Each letter represents a drum instrument that is hit on that beat, and each group represents a bar in the pattern.

- The `-` character can be used to represent a rest or an empty beat within a bar.
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

## Example Program to play micheal jackson



```shell
# Set the tempo to 117 BPM
BPM 90

# Set the number of bars to 16
bars 16

# Define the 'Verse' patternfile
Verse {
  HK H HS H
  HK H HS H
}

# Define the 'Chorus' pattern
Chorus {
    HK HK HS H
    HK HK HS H
}

# Play the patterns in the following order
@Verse
@Verse
@Chorus
@Verse
@Chorus
```