from apistar import schema

class TaskDefinition(schema.String):
    max_length = 128

class Task(schema.Object):
    properties = {
        'definition': TaskDefinition,
        'completed': schema.Boolean(default=False),
    }
