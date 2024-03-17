## Music-Driven Art Visualizer

This Python script utilizes Pygame and librosa libraries to create a real-time music visualization. It takes a music file as input and generates a dynamic visual representation based on the audio's spectrogram.

### Functionality

1. **Load Music:** The script utilizes `librosa.load` to read the music file and convert it into usable data formats.
2. **Spectrogram Generation:** It calculates the Short-Time Fourier Transform (STFT) of the audio using `librosa.stft`. The STFT represents the frequency content of the music over time.
3. **Random Colormap Selection:** The script employs `matplotlib.cm` to choose a random colormap for visualizing the spectrogram.
4. **Colormap Application:** The chosen colormap is applied to the spectrogram using custom functions to transform the data into RGB values suitable for Pygame.
5. **Music Playback:** Pygame's `mixer` module plays the music file in a loop.
6. **Visualization Loop:** 
    - The script continuously reads events to check for the quit event.
    - It iterates through the spectrogram data in slices, creating a surface for each slice.
    - Each surface represents a portion of the visualized spectrogram.
    - The surface is scaled to fit the screen resolution and then blitted onto the main screen.
    - The visualized window traverses the spectrogram data, creating a moving effect.
7. **Error Handling:** The script includes a `try-except` block to catch potential exceptions during execution and prints an informative error message.
8. **Cleanup:** A `finally` block ensures proper termination by quitting Pygame.

### Usage

1. Save the script as a Python file (e.g., `music_visualizer.py`).
2. Place your music file (e.g., `Sample_Song.mp3`) in the same directory as the script.
3. Run the script from the command line using `python music_visualizer.py`.
#
   ![image](https://github.com/SingKlayer/Music-Driven-Art-Visualizer/assets/72658973/11ea4f4e-4eaf-4f9b-a236-9360d3ab35c4)

#
   ![image](https://github.com/SingKlayer/Music-Driven-Art-Visualizer/assets/72658973/dcd52cbb-08c6-44ae-8edc-c2df46f1d470)


**Note:** Replace "Sample_Song.mp3" with the actual filename of your music file.

### Dependencies

* Pygame: [https://www.pygame.org/](https://www.pygame.org/)
* NumPy: [https://numpy.org/](https://numpy.org/)
* librosa: [https://librosa.org/doc/](https://librosa.org/doc/)
* Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)

This README provides a basic understanding of the script's functionality and usage. You can further enhance it by adding details about:

* Customization options (e.g., changing colormap selection logic)
* Performance considerations
* Potential future improvements
