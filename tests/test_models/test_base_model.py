import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os.path

objects = FileStorage._FileStorage__objects


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        model = BaseModel()
        x = model.updated_at
        model.save()
        y = model.updated_at
        self.assertNotEqual(x, y)
        os.remove("file.json")

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(len(model_dict), 4)

    def test_id(self):
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_created_at(self):
        model = BaseModel()
        created_date = model.created_at
        model.save()
        check_create_date = model.created_at
        self.assertEqual(created_date, check_create_date)

    def test_str(self):
        model = BaseModel()
        self.assertEqual(model.__str__(), f"[BaseModel] ({model.id}) {model.__dict__}")
        """ self.assertEqual(type(model.__str__()), str) """

    def test_save_with_reload(self):
        self.assertEqual(os.path.isfile("file.json"), False)
        obj = objects.copy()
        model = BaseModel()
        model.save()
        self.assertNotEqual(obj, objects)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")
