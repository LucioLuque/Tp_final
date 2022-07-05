import ...synthesizer.synthesizer as Synthesizer

def main():
    s=Synthesizer("queen.txt", "piano.txt")
    s.create_wav()


if __name__=="__main__":
    main()
    