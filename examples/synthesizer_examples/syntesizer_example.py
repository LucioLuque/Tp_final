from synthesizer import synthesizer as s

def main():
    s=s.Synthesizer("queen.txt", "piano.txt")
    s.create_wav()


if __name__=="__main__":
    main()
    