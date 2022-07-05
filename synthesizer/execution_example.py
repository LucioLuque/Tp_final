from synthesizer import *
def main():
    s1=Synthesizer("BlackBird.txt", "flauta.txt").create_wav("BlackBird", 44100)
    s2=Synthesizer("queen.txt", "piano.txt").create_wav("BohemianRhapsody", 44100)
    s3=Synthesizer("Rocket-Man.txt", "piano.txt").create_wav("RocketMan", 44100)

if __name__=="__main__":
    main()
