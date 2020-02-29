import os
import image


def test_makeImages(capsys):
    if os.path.exists("keys"):
        image.makeImages("BleacherReport", "test_images", 3)
        assert len(os.listdir('test_images')) > 3
    else:
        assert True
