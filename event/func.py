from .models import Event
import names
import time

def create_event_schedule():
    event = Event(
        name=names.get_first_name(), description=names.get_last_name()
    )
    time.sleep(5)
    print("here")
    event.save()
