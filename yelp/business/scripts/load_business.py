import json

from ..models import Business


def run():
    with open("business/scripts/business10k.json", "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            data = json.loads(line)
            Business.objects.create(**data)
