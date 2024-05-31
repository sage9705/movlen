# Video Length Calculator

## Overview

The Video Length Calculator is a simple graphical user interface (GUI) application I built with PyQt5. It allows users to select a folder containing video files and calculates the total duration of all the video files in that folder. The application supports various video formats and provides a progress bar to track the progress of the calculation.

## Features

- Select a folder containing video files.
- Calculate the total duration of all video files in the selected folder.
- Display the total duration in hours, minutes, and seconds.
- Supports multiple video formats: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.mpeg`, `.mpg`.
- Displays a progress bar to indicate the calculation progress.
- Skips files that are not of the specified video types.
- Error handling and user-friendly messages for unsupported files or issues.

## Motivation

The motivation behind creating this application was to provide an easy-to-use tool for users who need to quickly calculate the total length of multiple video files without manually adding up individual durations. This can be particularly useful for content creators, educators, or anyone managing a collection of videos. I got the idea to do this when I wanted to find out the total length of different tutorial videos I have in a folder. I didn't want to do the donkey work and this is the result. The GUI ensures that even users without technical expertise can efficiently use the tool. There's not much to it.

## Installation

To run the Video Length Calculator, you need to have Python installed on your system along with the following libraries:

- PyQt5
- moviepy

You can install these libraries using the requirements.txt file:

```sh
pip install -r requirements.txt
```
## Usage
Clone the repository or download the script.

Run the script:
```sh
python movlen.py
```

The GUI window will appear. Click on the "Select Folder" button to open a file dialog.

Choose the folder containing your video files.

The application will start processing the video files and display the total length in hours, minutes, and seconds once the calculation is complete. The progress bar will show the progress of the calculation.

# Code Explanation

## Main Components

### VideoLengthCalculator (QWidget)

- This is the main GUI class that initializes the user interface.
- It contains a label for instructions, a button to select a folder, a label to display the result, and a progress bar.
- It handles the folder selection and triggers the video length calculation.

### VideoLengthThread (QThread)

- This is a separate thread class to handle the video length calculation without freezing the GUI(Learnt from my youtube downloader app).
- It iterates through the video files in the selected folder, calculates the total duration, and updates the progress bar.
- It uses `pyqtSignal` to communicate with the main GUI thread.

## Signals and Slots

### Signals

- `progress_update`: Emitted to update the progress bar.
- `result_ready`: Emitted when the total length calculation is complete.
- `error_occurred`: Emitted when an error occurs during file processing.

### Slots

- `updateProgressBar`: Updates the progress bar value.
- `displayResult`: Displays the total video length.
- `displayError`: Shows an error message box.

## Error Handling

- The code includes error handling to manage issues such as unsupported files or problems reading video files. Errors are displayed to the user through message boxes.
- The program skips over files that are not of the specified video types or cause errors during processing, ensuring uninterrupted calculation.

## Conclusion

I designed the app to provide a simple yet efficient solution for calculating the total duration of multiple video files. Its user-friendly GUI and support for various video formats make it a valuable tool for a wide range of users. By running the calculation in a separate thread, the application ensures a responsive and smooth user experience.

I hope you find this tool useful and welcome any feedback or suggestions for improvements. You're welcome to make use and modify it as well.
