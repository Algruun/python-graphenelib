import unittest
from graphenebase.objects import Operation, GrapheneObject
from graphenebase.operations import Newdemooepration, Newdemooepration2


class Testcases(unittest.TestCase):

    def test_init_name(self):
        op = Operation("demooepration")
        self.assertEqual(op.name, "demooepration")
        self.assertEqual(op.id, 0)
        self.assertEqual(op.klass_name, "Demooepration")
        self.assertEqual(bytes(op), b"\x00")
        self.assertEqual(op.json(), op.toJson())

    def test_init_int(self):
        op = Operation(0)
        self.assertEqual(op.name, "demooepration")
        self.assertEqual(op.id, 0)
        self.assertEqual(op.klass_name, "Demooepration")
        self.assertEqual(bytes(op), b"\x00")
        self.assertEqual(op.json(), op.toJson())

    def test_init_data(self):
        op = Operation([0, dict(string="1.2.0")])
        self.assertEqual(op.name, "demooepration")
        self.assertEqual(op.id, 0)
        self.assertEqual(op.klass_name, "Demooepration")
        self.assertEqual(
            str(op), '[0, {"string": "1.2.0", "extensions": []}]')
        self.assertEqual(op.json(), op.toJson())
        self.assertEqual(len(op.json()), 2)
        self.assertEqual(len(op.json()[1]), 2)
        self.assertIn("string", op.json()[1])
        self.assertIn("extensions", op.json()[1])
        self.assertEqual(bytes(op), b"\x00\x051.2.0\x00")

    def test_init_data_afterwards(self):
        op = Operation("demooepration", string="1.2.0")
        self.assertEqual(op.name, "demooepration")
        self.assertEqual(op.id, 0)
        self.assertEqual(op.klass_name, "Demooepration")
        self.assertEqual(
            str(op), '[0, {"string": "1.2.0", "extensions": []}]')
        self.assertEqual(op.json(), op.toJson())
        self.assertEqual(len(op.json()), 2)
        self.assertEqual(len(op.json()[1]), 2)
        self.assertIn("string", op.json()[1])
        self.assertIn("extensions", op.json()[1])
        self.assertEqual(bytes(op), b"\x00\x051.2.0\x00")

    def test_init_go(self):
        o = GrapheneObject()
        self.assertEqual(bytes(o), b"")
        self.assertEqual(dict(o), {})

        o = GrapheneObject({"string": "demooepration"})
        self.assertEqual(bytes(o), b"demooepration")
        self.assertEqual(dict(o), {"string": "demooepration"})
        self.assertEqual(o.json(), {"string": "demooepration"})
        self.assertEqual(o.toJson(), {"string": "demooepration"})
        self.assertEqual(o.data, o)

    def test_newdemo_op(self):
        for op in [
            Newdemooepration(**dict(string="1.2.0")),
            Newdemooepration(dict(string="1.2.0"))
        ]:
            self.assertEqual(op.json()["string"], "1.2.0")
            self.assertIn("string", op.json())
            self.assertIn("extensions", op.json())
            # Test order of attributes
            self.assertEqual(list(op.items())[0][0], "string")
            self.assertEqual(list(op.items())[1][0], "optional")
            self.assertEqual(list(op.items())[2][0], "extensions")

        op = Newdemooepration(dict(string="1.2.0", optional="foobar"))
        self.assertEqual(op.json()["string"], "1.2.0")
        self.assertIn("string", op.json())
        self.assertIn("optional", op.json())
        self.assertIn("extensions", op.json())
        self.assertEqual(list(op.items())[0][0], "string")
        self.assertEqual(list(op.items())[1][0], "optional")
        self.assertEqual(list(op.items())[2][0], "extensions")

    def test_loadingofGrapheneObject(self):
        op = Newdemooepration(dict(string="1.2.0", optional="foobar"))
        op2 = Operation(op)
        self.assertEqual(op.json()["string"], "1.2.0")

        self.assertEqual(op2.json()[0], 1)
        self.assertEqual(list(op2[1].items())[1][0], "optional")
        self.assertEqual(list(op2[1].items())[2][0], "extensions")

    def test_order(self):
        op1 = Newdemooepration(string="1.2.0", optional="foobar")
        op2 = Newdemooepration2(string="1.2.0", optional="foobar")

        self.assertEqual(list(op1.items())[0][0], "string")
        self.assertEqual(list(op1.items())[1][0], "optional")
        self.assertEqual(list(op1.items())[2][0], "extensions")

        self.assertEqual(list(op2.items())[0][0], "optional")
        self.assertEqual(list(op2.items())[1][0], "string")
        self.assertEqual(list(op2.items())[2][0], "extensions")