from datetime import datetime

class Album:
    def __init__(self, id, name, date, added_at):
        self.id       = id
        self.name     = name
        self.date     = date
        self.added_at = datetime.fromisoformat(added_at.replace('Z', '+00:00'))

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'date': self.date, 'added_at': str(self.added_at)}

    def __repr__(self):
        return f"Album(id={self.id}, name={self.name}, date={self.date}, added_at={self.added_at})"