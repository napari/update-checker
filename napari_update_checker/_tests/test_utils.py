from napari_update_checker.utils import (
    conda_forge_releases,
    get_latest_version,
    github_tags,
)


def test_github_tags():
    data = github_tags()
    assert data[0] == '0.5.0a1'
    assert len(data) >= 30  # Oldest version


def test_conda_forge_releases():
    data = conda_forge_releases()
    assert data[0] == '0.2.12'  # Oldest version
    assert len(data) >= 35


def test_get_latest_version():
    result = get_latest_version(github=None)
    assert result
    result = get_latest_version(github=True)
    assert result
    result = get_latest_version(github=False)
    assert result
