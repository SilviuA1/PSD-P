import librosa
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np


class TimeSignal:
    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def get_mmm(time_signal):
        maximum = max(time_signal)
        minimum = min(time_signal)
        mean_val = sum(time_signal)/len(time_signal)

        return [maximum, minimum, mean_val]

    @staticmethod
    def get_fft_entirely(signal):
        return abs(np.fft.fft(signal))

    @staticmethod
    def get_fft_of_intervals(signal_intervals):
        temporary_fft = None
        num_of_intervals = len(signal_intervals)

        for interval_idx in range(0, num_of_intervals-1):
            interval_curr= np.concatenate([signal_intervals[interval_idx], signal_intervals[interval_idx+1]])
            curr_interval_len = len(interval_curr)
            start_idx = int(curr_interval_len/6)
            end_idx = int(curr_interval_len/6*4)

            interval_curr_trimmed = interval_curr[start_idx:end_idx]

            if temporary_fft is None:
                temporary_fft = abs(np.fft.fft(interval_curr_trimmed))
            else:
                temporary_fft = temporary_fft + abs(np.fft.fft(interval_curr_trimmed))

        return temporary_fft


class SoundUtil:
    num_plot = 0

    def __init__(self):
        SoundUtil.num_plot = 0

    def __del__(self):
        SoundUtil.num_plot = 0

    @staticmethod
    def export_wav_file(wav_signal, sr):
        sf.write('../data/stereo_util.wav', wav_signal, sr[0])

    @staticmethod
    def read_wav_files(wav_files):
        if not isinstance(wav_files, list):
            wav_files = [wav_files]
        return [librosa.load(f)[0] for f in wav_files]

    @staticmethod
    def get_wav_rate(wav_files):
        if not isinstance(wav_files, list):
            wav_files = [wav_files]
        return [librosa.load(f)[1] for f in wav_files]

    @staticmethod
    def plot_sound(sound_to_plot, plot_title):
        SoundUtil.num_plot = SoundUtil.num_plot + 1
        plt.figure(SoundUtil.num_plot)
        plt.title(plot_title)
        plt.plot(sound_to_plot)

    @staticmethod
    def split_sound_in_intervals(working_sound, num_of_intervals):
        max_len = len(working_sound)
        interval_len = int(max_len / num_of_intervals)

        sound_intervals = []

        for i in range(1, num_of_intervals+1):
            temporary_interval = working_sound[interval_len*(i-1):interval_len*i]
            sound_intervals.append(temporary_interval)

        return sound_intervals

    @staticmethod
    def show_plots():
        plt.show()

    @staticmethod
    def get_util_part_of_sound(wav_sound):
        full_content = sum(abs(wav_sound))
        sound_len = len(wav_sound)
        step = int(sound_len / 40)

        print("Full content has " + str(full_content) + " of data.")
        index = 0
        for index in range(0, sound_len, step):
            if wav_sound[index] != 0:
                break

        start = index
        stop = index + step
        util_content = 0

        while util_content < full_content*85/100:
            util_content = sum(abs(wav_sound[start:stop]))
            if stop >= sound_len:
                break

            stop = min(stop + step, sound_len)

        print("Util calculated has " + str(util_content) + " of data!")
        print("Reduced to " + str(start) + " - " + str(stop) + " !")
        return wav_sound[start:stop]
