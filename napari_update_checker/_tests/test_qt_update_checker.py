from napari_update_checker.qt_update_checker import UpdateChecker


def test_widget(qtbot):
    w = UpdateChecker()
    w.show()
    w.close()
