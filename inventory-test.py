import unittest
import re
import taipan.inventory as inv

class InventoryDisplay(unittest.TestCase):
    def testVacancy(self):
        ship = inv.inventory()
        self.assertEqual(False, ship.overloaded())
        self.assertEqual(ship.size, ship.vacant())
        ship.opium = ship.size
        self.assertEqual(0, ship.vacant())
        self.assertEqual(False, ship.overloaded())
        ship.opium *= 2;
        self.assertEqual(-50, ship.vacant())
        self.assertEqual(True, ship.overloaded())

    def testCommodities(self):
        inventory = inv.inventory()

        self.assertEqual(0, inventory.opium)
        self.assertEqual(0, inventory.silk)
        self.assertEqual(0, inventory.general)
        self.assertEqual(0, inventory.arms)
        self.assertEqual(50, inventory.size)
        self.assertEqual(False, inventory.overloaded())

        # test opium addition
        inventory.opium = 10
        self.assertEqual(10, inventory.opium)
        inventory.opium += 15
        self.assertEqual(25, inventory.opium)

        # test silk addition
        inventory.silk = 10
        self.assertEqual(10, inventory.silk)
        inventory.silk += 15
        self.assertEqual(25, inventory.silk)

        # test general addition
        inventory.general = 10
        self.assertEqual(10, inventory.general)
        inventory.general += 15
        self.assertEqual(25, inventory.general)

        # test arms addition
        inventory.arms = 10
        self.assertEqual(10, inventory.arms)
        inventory.arms += 15
        self.assertEqual(25, inventory.arms)

        # inventory.setDefaults()
        # output = inventory.display()
        # self.assertRegexpMatches(output, "^Cargo\s+In Hold\s+Warehouse")
        # self.assertRegexpMatches(output, "^\sOpium")
        # self.assertRegexpMatches(output, "^\sSilk")
        # self.assertRegexpMatches(output, "^\sArms")
        # self.assertRegexpMatches(output, "^\sGeneral")
        # self.assertRegexpMatches(output, "^\sVacant")


if __name__ == "__main__":
    unittest.main()
