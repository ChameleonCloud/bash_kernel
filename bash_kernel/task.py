import threading
import time

class PeriodicTask:
    """A simple periodic task runner that runs a function on some interval.

    Note: this does not calculate or compensate for drift over time. It is
          possible that a task running every 5 seconds might first execute
          at t=0, then t=5.01s, then t=10.02s, etc.
    """
    def __init__(self, task_fn, interval_s=300):
        if not (task_fn and callable(task_fn)):
            raise ValueError('A callable task function must be provided')
        if interval_s <= 0:
            raise ValueError('A positive interval is required')
        self.task_fn = task_fn
        self.interval_s = interval_s
        self._thread = threading.Thread(target=self.tick, daemon=True)

    def start(self):
        self._thread.start()

    def tick(self):
        self.task_fn()
        time.sleep(self.interval_s)
