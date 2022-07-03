from synthesizer.synthesizer import Synthesizer

if __name__=="__main__":
    s=Synthesizer("queen.txt", "piano.txt")
    s.create_wav()