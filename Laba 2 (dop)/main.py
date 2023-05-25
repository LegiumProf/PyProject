from pydub import AudioSegment
def change_speed(path, speed):
    music = AudioSegment.from_wav("Queen-Princes-Of-The-Universe.wav")

    sound_rate = music._spawn(music.raw_data, overrides={"frame_rate": int(music.frame_rate * speed)})

    new_path = f"{path}"
    sound_rate.export(new_path, format="wav")
change_speed("123.wav", 2)