import os
if __name__ == '__main__':
    print("RoboSpeak 2.0 created by Maruf Raihan")
    while True:
        x = input("Pronounce words: ")
        if x == "q":
            os.system("say 'good bye babe'")
            break

        command = f"say {x}"
        os.system(command)
