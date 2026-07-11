class GeneratorError(Exception):
    pass

class ValidationError(GeneratorError):
    pass

class BuilderError(GeneratorError):
    pass
