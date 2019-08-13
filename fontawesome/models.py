
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^fontawesome\.fields\.IconField"])
except ImportError:
    pass