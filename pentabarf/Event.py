
class Event:

    id = None
    date = None
    start = None
    duration = None
    track = None
    abstract = None
    title = None
    type = None
    description = None
    conf_url = None
    full_conf_url = None
    released = None

    person_objects = []

    def __init__(self, id=None, date=None, start=None, duration=None, track=None, abstract=None,
                 title=None, type=None, description=None, conf_url=None, full_conf_url=None, released=None):
        self.id = id
        self.date = date
        self.start = start
        self.duration = duration
        self.track = track
        self.abstract = abstract
        self.title = title
        self.type = type
        self.description = description
        self.conf_url = conf_url
        self.full_conf_url = full_conf_url
        self.released = released

    def add_person(self, person):
        self.person_objects.append(person)

