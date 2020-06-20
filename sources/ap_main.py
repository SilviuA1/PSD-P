import glob

# user lib
from util import *

path_to_audio = glob.glob('./../data/*')[0]

if __name__ == '__main__':
    print("The file we are working on is:" + str(path_to_audio))
    working_sound = SoundUtil.read_wav_files(path_to_audio)
    working_sound = working_sound[0]
    wav_rate_of_sound = SoundUtil.get_wav_rate(path_to_audio)

    SoundUtil.plot_sound(working_sound, "Original sound ...")
    working_sound = SoundUtil.get_util_part_of_sound(working_sound)
    SoundUtil.plot_sound(working_sound, "Util sound ...")

    print(TimeSignal.get_mmm(working_sound))

    # SoundUtil.export_wav_file(working_sound, wav_rate_of_sound)

    fft_of_working_signal = TimeSignal.get_fft_entirely(working_sound)
    SoundUtil.plot_sound(fft_of_working_signal, "FFT of working sound")

    intervals_working_sound = SoundUtil.split_sound_in_intervals(working_sound, 10)

    fft_of_working_signal_intervals = TimeSignal.get_fft_of_intervals(intervals_working_sound)
    SoundUtil.plot_sound(fft_of_working_signal_intervals, "FFT on intervals")


SoundUtil.show_plots()
