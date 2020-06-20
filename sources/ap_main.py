import glob

# user lib
from util import *

path_to_audio = glob.glob('./../data/*')[0]

if __name__ == '__main__':
    print("The file we are working on is:" + str(path_to_audio))
    working_sound = SoundUtil.read_wav_files(path_to_audio)
    working_sound = working_sound[0]
    wav_rate_of_sound = SoundUtil.get_wav_rate(path_to_audio)

    # SoundUtil.plot_sound(working_sound, "Original sound ...")
    working_sound = SoundUtil.get_util_part_of_sound(working_sound)
    # SoundUtil.plot_sound(working_sound, "Util sound ...")

    print(TimeSignal.get_mmm(working_sound))

    # SoundUtil.export_wav_file(working_sound, wav_rate_of_sound)

    fft_of_working_signal = TimeSignal.get_fft_entirely(working_sound)
    SoundUtil.plot_sound(fft_of_working_signal, "FFT of working sound")

    intervals_working_sound = SoundUtil.split_sound_in_intervals(working_sound, 10)

    fft_of_working_signal_intervals = TimeSignal.get_fft_of_intervals(intervals_working_sound)
    # SoundUtil.plot_sound(fft_of_working_signal_intervals, "FFT on intervals")

    fft_of_working_signal_timeframe = TimeSignal.get_fft_of_timeframe(working_sound, 20, 80)
    # SoundUtil.plot_sound(fft_of_working_signal_timeframe, "FFT on 20% to 80%")

    to_filter_window = TimeSignal.get_window_by_name('hanning', len(working_sound))
    SoundUtil.plot_sound(to_filter_window, "Hanning window")

    working_sound_filtred = working_sound * to_filter_window
    fft_of_working_signal = TimeSignal.get_fft_entirely(working_sound_filtred)
    SoundUtil.plot_sound(fft_of_working_signal, "FFT of working sound filtred hanning")

    to_filter_window = TimeSignal.get_window_by_name('blackmanharris', len(working_sound))
    SoundUtil.plot_sound(to_filter_window, "blackmanharris window")

    working_sound_filtred = working_sound * to_filter_window
    fft_of_working_signal = TimeSignal.get_fft_entirely(working_sound_filtred)
    SoundUtil.plot_sound(fft_of_working_signal, "FFT of working sound filtred blackmanharris")


SoundUtil.show_plots()
