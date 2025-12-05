import os
import importlib

repositories = {}

repositoriesPath = os.path.join(os.path.dirname(__file__), "..", "Repository")

for filename in os.listdir(repositoriesPath):
    if not filename.endswith(".py") or filename == "__init__.py":
        continue

    className = filename[:-3]
    module = importlib.import_module(f"Repository.{className}")

    repositoryClass = getattr(module, className)
    repositories[className] = repositoryClass()

def repository(repositoryName):
    return repositories.get(repositoryName)