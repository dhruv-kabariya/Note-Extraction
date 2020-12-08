import argparse

from pydub import AudioSegment
import pydub.scipy_effects
import numpy as np
import scipy
import matplotlib.pyplot as plt

from note.utils import (
    frequency_spectrum,
    classify_note_attempt_3,
)


def main(file, note_file=None, note_starts_file=None, plot_starts=False, plot_fft_indices=[]):
    # If a note file and/or actual start times are supplied read them in
    actual_starts = []
    if note_starts_file:
        with open(note_starts_file) as f:
            for line in f:
                actual_starts.append(float(line.strip()))

    actual_notes = []
    if note_file:
        with open(note_file) as f:
            for line in f:
                actual_notes.append(line.strip())

    song = AudioSegment.from_file(file)
    song.export(file[0:-4] + ".mp3", format="mp3")
    song = song.high_pass_filter(80)

    starts, volumn, segment_ms = predict_note_starts(
        song, plot_starts, actual_starts)
    # print(starts)
    predicted_notes, predicted_time = predict_notes(
        song, starts, actual_notes, plot_fft_indices)

    return predicted_notes, starts, volumn, segment_ms


def predict_note_starts(song, plot, actual_starts):
    # Size of segments to break song into for volume calculations
    SEGMENT_MS = 50
    # Minimum volume necessary to be considered a note
    VOLUME_THRESHOLD = -35
    # The increase from one sample to the next required to be considered a note
    EDGE_THRESHOLD = 5
    # Throw out any additional notes found in this window
    MIN_MS_BETWEEN = 100

    # Filter out lower frequencies to reduce noise
    song = song.high_pass_filter(80, order=4)

    # dBFS is decibels relative to the maximum possible loudness
    volume = [segment.dBFS for segment in song[::SEGMENT_MS]]

    predicted_starts = []
    for i in range(1, len(volume)):
        if volume[i] > VOLUME_THRESHOLD and volume[i] - volume[i - 1] > EDGE_THRESHOLD:
            ms = i * SEGMENT_MS
            # Ignore any too close together
            if len(predicted_starts) == 0 or ms - predicted_starts[-1] >= MIN_MS_BETWEEN:
                predicted_starts.append(ms)
    # If actual note start times are provided print a comparison
    if len(actual_starts) > 0:
        print("Approximate actual note start times ({})".format(len(actual_starts)))
        print(" ".join(["{:5.2f}".format(s) for s in actual_starts]))
        print("Predicted note start times ({})".format(len(predicted_starts)))
        print(" ".join(["{:5.2f}".format(ms / 1000)
                        for ms in predicted_starts]))

    # Plot the volume over time (sec)
    if plot:
        x_axis = np.arange(len(volume)) * (SEGMENT_MS / 1000)
        plt.plot(x_axis, volume)

        # Add vertical lines for predicted note starts and actual note starts
        for s in actual_starts:
            plt.axvline(x=s, color="r", linewidth=0.5, linestyle="-")
        for ms in predicted_starts:
            plt.axvline(x=(ms / 1000), color="g", linewidth=0.5, linestyle=":")

        plt.show()

    return predicted_starts, volume, SEGMENT_MS


def predict_notes(song, starts, actual_notes, plot_fft_indices):
    predicted_notes = []
    prediction_time = []
    # print(starts)
    for i, start in enumerate(starts):
        sample_from = start + 50
        sample_to = start + 500
        if i < len(starts) - 1:
            sample_to = min(starts[i + 1], sample_to)
        segment = song[sample_from:sample_to]
        freqs, freq_magnitudes = frequency_spectrum(segment)

        predicted = classify_note_attempt_3(freqs, freq_magnitudes)
        predicted_notes.append(predicted or "U")
        prediction_time.append(sample_from)

        if i in plot_fft_indices:
            plt.plot(freqs, freq_magnitudes, "b")
            plt.xlabel("Freq (Hz)")
            plt.ylabel("|X(freq)|")
            plt.show()
    return predicted_notes, prediction_time
