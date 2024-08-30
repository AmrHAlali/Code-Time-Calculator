from datetime import datetime
import pygetwindow as gw
import time
import re
from Codeforces import get_last_accepted_problem
from Timer import Timer


class Track:
    def isCompiler(self, filename):
        pattern = r'^(?!.*Codeforces).*\.(cpp|h|java|class|py|pyc)$'
        if re.search(pattern, filename):
            return True
        return False

    def get_active_window_title(self):
        try:
            active_window = gw.getActiveWindow()
            if active_window:
                return active_window.title
            else:
                return None
        except Exception as e:
            print(f"Error getting active window: {e}")
            return None

    def track_active_window(slef, user_handle, interval=0.1):
        last_window_title = None
        timer = Timer()
        while True:
            if get_last_accepted_problem(user_handle):
                timer.stop()
                print(f"Spent {timer.convert_seconds(timer.numberOfSeconds)} writing the code.")
                print(f"Spent {timer.printWholeTime()} solving the whole problem.")
                break

            current_window_title = slef.get_active_window_title()
            if slef.isCompiler(current_window_title):
                timer.start()
            else:
                timer.stop()
            if current_window_title and current_window_title != last_window_title:
                # print(f"Active window changed: {current_window_title}")
                last_window_title = current_window_title

            time.sleep(interval)

