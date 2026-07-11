from pathlib import Path

class Validator:

    REQUIRED = [
        "generator/manifests/project.yaml",
        "generator/builders/builder_registry.py",
        "generator/plugins/plugin_registry.py",
    ]

    def validate(self):

        missing = []

        for item in self.REQUIRED:
            if not Path(item).exists():
                missing.append(item)

        return missing
