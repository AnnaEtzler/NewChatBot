import time
from progress.bar import IncrementalBar


def showProgress(punkte):
    bar = IncrementalBar('Countdown', max=10)
    for item in range(punkte):
        bar.next()
        time.sleep(1)
    bar.finish()
