import json
from functools import lru_cache
from urllib.request import urlopen


@lru_cache
def github_tags(url: str = 'https://api.github.com/repos/napari/napari/tags'):
    with urlopen(url) as r:
        data = json.load(r)

    versions = []
    for item in data:
        version = item.get('name', None)
        if version:
            if version.startswith('v'):
                version = version[1:]

            versions.append(version)

    return list(reversed(versions))


@lru_cache
def conda_forge_releases(
    url: str = 'https://api.anaconda.org/package/conda-forge/napari/',
):
    with urlopen(url) as r:
        data = json.load(r)
    versions = data.get('versions', [])
    return versions
