init -1 python:
    for i in range(1, 10):
        setattr(store.audio, f"bgm0{i}", f"audio/bgm0{i}.opus")
