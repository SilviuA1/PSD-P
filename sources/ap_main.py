import glob

# user lib
from util import *

path_to_audio = glob.glob('./../data/*')[0]

if __name__ == '__main__':
    print("The file we are working on is:" + str(path_to_audio))
    my_signal = Sound.read_file(path_to_audio)
    my_signal = my_signal[0]
    wav_rate_of_sound = Sound.get_wav_rate(path_to_audio)

    # SoundUtil.plot_sound(working_sound, "Original sound ...")
    my_signal = Sound.extract_util_part_of_signal(my_signal)
    # SoundUtil.plot_sound(working_sound, "Util sound ...")

    print(SignalProcess.get_mmm(my_signal))

    # SoundUtil.export_wav_file(working_sound, wav_rate_of_sound)

    fft_of_signal = SignalProcess.get_fft_entire_signal(my_signal)
    Sound.plot_signal(fft_of_signal, "FFT - Parte utila")

    signal_intervals = Sound.get_intervals(my_signal, 10)

    fft_of_intervals_signal = SignalProcess.get_fft_of_intervals(signal_intervals)
    # SoundUtil.plot_sound(fft_of_intervals_signal, "FFT on intervals")

    fft_of_signal_timeframe = SignalProcess.get_fft_of_timeframe(my_signal, 20, 80)
    # SoundUtil.plot_sound(fft_of_signal_timeframe, "FFT on 20% to 80%")

    hanning_window = SignalProcess.get_window_by_name('hanning', len(my_signal))
    Sound.plot_signal(hanning_window, "Fereastra Hanning")

    working_sound_filtred = my_signal * hanning_window
    fft_of_working_signal = SignalProcess.get_fft_entire_signal(working_sound_filtred)
    Sound.plot_signal(fft_of_working_signal, "FFT - Fereastra Hanning")

    to_filter_window = SignalProcess.get_window_by_name('blackmanharris', len(my_signal))
    Sound.plot_signal(to_filter_window, " Fereastra Blackmanharris ")

    working_sound_filtred = my_signal * to_filter_window
    fft_of_working_signal = SignalProcess.get_fft_entire_signal(working_sound_filtred)
    Sound.plot_signal(fft_of_working_signal, "FFT - Fereastra Blackmanharris")

    to_filter_window = SignalProcess.get_window_by_name('hamming', len(my_signal))
    Sound.plot_signal(to_filter_window, " Fereastra Hamming ")

    working_sound_filtred = my_signal * to_filter_window
    fft_of_working_signal = SignalProcess.get_fft_entire_signal(working_sound_filtred)
    Sound.plot_signal(fft_of_working_signal, "FFT - Fereastra Hamming")


Sound.show_plots()
