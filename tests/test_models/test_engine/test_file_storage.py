import unittest
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

# model = BaseModel()
# model.save()


file = FileStorage._FileStorage__file_path


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        model = BaseModel()
        model.save()
        """ self.assertEquals(os.path.isfile("file.json"), True) """
        self.assertEquals(file, "file.json")
        os.remove("file.json")

    def test_objects(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        self.assertEqual(type(objects), dict)
        os.remove("file.json")

    def test_all(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        all_objs = storage.all()
        self.assertEquals(objects, all_objs)
        os.remove("file.json")

    def test_new(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEquals(objects[f"{model.__class__.__name__}.{model.id}"], None)
        """ os.remove("file.json") """

    def test_reload(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        obj = objects.copy()
        model = BaseModel()
        FileStorage.reload(FileStorage)
        self.assertNotEqual(obj, objects)
        """ os.remove("file.json") """

    def test_save_storage(self):
        self.assertEqual(os.path.isfile("file.json"), False)
        model = BaseModel()
        FileStorage.save(FileStorage)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")
