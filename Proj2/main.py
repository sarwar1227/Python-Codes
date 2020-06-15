'''Health Programer
9am - 5pm
water - water.mp3 (3.5 litres) - drank - log - every 40 min
eyes - eyes.mp3 - every 30 min - eydone - log every 30 min
physical activity - physical.mp3 every - 45 min - exdone - log
#Rules
Pygame module to play music
'''
from pygame import mixer
from datetime import  datetime
from time import time
def music_on_loop(file,stoppner):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("my_logs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    #music_on_loop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_secs=10
    eye_secs=40
    exercise_secs=60
    while True:
        if time()-init_water>water_secs:
            print("Water Drinking time.Enter 'drank' to stop the alarm : ")
            music_on_loop("water.mp3",'drank')
            init_water=time()
            log_now("Drank Water at : ")
        if time()-init_eyes>eye_secs:
            print("Eye Exercising time.Enter 'eydone' to stop the alarm : ")
            music_on_loop("eyes.mp3",'eydone')
            init_eyes=time()
            log_now("Eye Exercising Done at : ")
        if time()-init_exercise>exercise_secs:
            print("Exercise time.Enter 'exdone' to stop the alarm : ")
            music_on_loop("exercise.mp3",'exdone')
            init_exercise=time()
            log_now("Exercising done at : ")
