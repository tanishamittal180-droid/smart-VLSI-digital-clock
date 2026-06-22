import datetime

class ClockData:

    def __init__(self):

        now=datetime.datetime.now()

        self.hour=now.hour
        self.minute=now.minute
        self.second=now.second

        self.day=now.day
        self.month=now.month

        self.stopwatch=0

        self.alarm_hour=7
        self.alarm_min=30

        self.alarm_enabled=True
        self.alarm=False

    def update(self):

        now=datetime.datetime.now()

        self.hour=now.hour
        self.minute=now.minute
        self.second=now.second

        self.day=now.day
        self.month=now.month

        if(
            self.alarm_enabled
            and
            self.hour==self.alarm_hour
            and
            self.minute==self.alarm_min
        ):
            self.alarm=True

        else:
            self.alarm=False


clock=ClockData()