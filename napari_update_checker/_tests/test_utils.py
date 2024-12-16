from napari_update_checker.utils import conda_forge_releases, github_tags


def test_github_tags():
    data = github_tags()
    assert '0.5.0a1' in data


def test_conda_forge_releases():
    data = conda_forge_releases()
    assert '0.4.19.post1' in data
