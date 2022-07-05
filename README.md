# Musicalizador

This repository contains the final practical work of the "Pensamiento Computacional" subject of the Artificial Intelligence Engineering degree at the University of San Andres. The work is composed of 2 main parts:

- A program that allows, from a music sheet, to synthesize the predefined notes and generate a wave file which contains all these notes ordered and modularized. 
- A program that, starting from a music sheet, sends the notes that you want to play to a real instrument. In this case, the instrument is a metallophone.

## Installation

To be able to use all the functionalities of both programs, it is necessary to carry out an installation. Execute the following steps:

1. Clone the repository.
```shell
$ git clone https://github.com/LucioLuque/Tp_final.git
```
2. Get in the local repository.
```shell
$ cd /path/to/Tp_final
```
3. Install the dependencies.
```shell
$ pip install -r requirements.txt
```
> Note: Install it with pip

## Usage

### Synthesizer
First of all, you need the midi file of the song you want to generate. Maybe you can find the song you want to use [here](http://www.piano-midi.de/). To transform the midi file into a music sheet compatible with the program, we have to use the "midi2score" file. Calling it in the following way, we will get the score of the desired song: 
```shell
$ python3 midi2score.py -i <MIDI File> -o <Output File> -t <Tracks(CSV)>
```
> Note: -t is not generally used

When the requested score has already been created, you will be able to create the wave file. To achieve this, it is necessary to perform the following actions: 

```shell
$ python3 prog.py -f <Frequency> -i <Instrument> -p <Music sheet> -o <Audio.wav>
```
> Note: The wave file will be generated in the folder "synthesizer".
### Metallophono 
First of all, in order to communicate with the metallophone, it is necessary to download the files from the following [repository](https://github.com/udesa-ai/xylophone).
> Note: Al the information about how to the clone the repository and install all the dependencies is in the README file of the repository.

After downloading all required files, by invoking the "metallophone" file, it will be possible to communicate with the instrument in the following way:
```shell
$ python3 metallophone.py -i <Music sheet name> -o <Instrument IP>
```
> Note: Put the "metallophone.py" file and the music sheet in the same folder into the folder "xylophone". 

The program does not support certain musical notes. "metallophone.py" is able to raise and lower the octaves of the notes so that they are compatible, but it is recommended to use a song that is within the appropriate range. The supported notes are:

 | #  | Note | #   | b   |
 |----|------|-----|-----|
 | 1  | C7   | C#7 | Cb7 |
 | 2  | B6   | -   | Bb6 |
 | 3  | A6   | A#6 | Ab6 |
 | 4  | G6   | G#6 | Gb6 |
 | 5  | F6   | F#6 | -   |
 | 6  | E6   | -   | Eb6 |
 | 7  | D6   | D#6 | Db6 |
 | 8  | C6   | C#6 | -   |
 | 9  | B5   | -   | Bb5 |
 | 10 | A5   | A#5 | Ab5 |
 | 11 | G5   | -   | -   |
 | 12 | F5   | -   | -   |
 | 13 | E5   | -   | Eb5 |
 | 14 | D5   | D#5 | Db5 |
 | 15 | C5   | C#5 | -   |
 | 16 | B4   |  -  | Bb4 |
 | 17 | A4   | A#4 | Ab4 |
 | 18 | G4   | G#4 | -   |
 
 ## Contributors 
- [Lucio Luque Materazzi](https://github.com/LucioLuque)
- [Schuemer Ignacio](https://github.com/ignaschuemer7)
- [Santiago Torres](https://github.com/storres0514)
- [Mateo Giacometti](https://github.com/Mateo-Giacometti)
