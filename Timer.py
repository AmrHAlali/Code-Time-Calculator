from datetime import datetime


class Timer:
    def __init__(self):
        self.numberOfSeconds = 0
        self.startTime = None
        self.realStartTime = datetime.now().time()
        self.realStartTime = datetime.combine(datetime.today(), self.realStartTime)

    def start(self):
        if not self.startTime == None:
            pass
        else:
            self.startTime = datetime.now().time()

    def stop(self):
        if self.startTime == None:
            pass
        else:
            time2 = datetime.now().time()

            time1_datetime = datetime.combine(datetime.today(), self.startTime)
            time2_datetime = datetime.combine(datetime.today(), time2)
            time_difference = time2_datetime - time1_datetime
            seconds = time_difference.total_seconds()
            self.numberOfSeconds += seconds
            self.startTime = None

    def convert_seconds(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def printWholeTime(self):
        currentTime = datetime.combine(datetime.today(), datetime.now().time())
        currentTime = int((currentTime - self.realStartTime).total_seconds())
        return self.convert_seconds(currentTime)