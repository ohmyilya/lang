import csv
import os
import shutil
from gtts import gTTS
from pydub import AudioSegment

def text_to_audio(text, output_file, language, speed=1.0):
    tts = gTTS(text=text, lang=language, slow=(speed == 0.75))
    tts.save(output_file)

def merge_audio_files(audio_files, output_file):
    combined_audio = AudioSegment.empty()
    for index, audio_file in enumerate(audio_files):
        audio = AudioSegment.from_file(audio_file, format="mp3")
        combined_audio += audio
        # Add 2-second pause between each recording (except the last one)
        if index < len(audio_files) - 1:
            pause = AudioSegment.silent(duration=2000)
            combined_audio += pause
    combined_audio.export(output_file, format="wav")

def main():
    input_file = "phrases.csv"
    english_language = "en"
    russian_language = "ru"
    output_folder = "output_phrases"
    temp_folder = "temp_audio"

    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(temp_folder, exist_ok=True)

    with open(input_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            number, english_phrase, russian_phrase = row
            english_file_normal = os.path.join(temp_folder, f"{number}_english_normal.mp3")
            english_file_slow_1 = os.path.join(temp_folder, f"{number}_english_slow_1.mp3")
            english_file_slow_2 = os.path.join(temp_folder, f"{number}_english_slow_2.mp3")
            russian_file_normal = os.path.join(temp_folder, f"{number}_russian_normal.mp3")

            # Record the English phrase with normal speed
            text_to_audio(english_phrase, english_file_normal, english_language)

            # Record the English phrase with 0.75x speed (first time)
            text_to_audio(english_phrase, english_file_slow_1, english_language, speed=0.75)

            # Record the English phrase with 0.75x speed (second time)
            text_to_audio(english_phrase, english_file_slow_2, english_language, speed=0.75)

            # Record the Russian phrase with normal speed
            text_to_audio(russian_phrase, russian_file_normal, russian_language)

            merge_audio_files([english_file_normal, english_file_slow_1, english_file_slow_2, russian_file_normal],
                              os.path.join(output_folder, f"{number}.wav"))

            os.remove(english_file_normal)
            os.remove(english_file_slow_1)
            os.remove(english_file_slow_2)
            os.remove(russian_file_normal)

    # Remove the temporary audio folder after merging
    shutil.rmtree(temp_folder)

if __name__ == "__main__":
    main()
