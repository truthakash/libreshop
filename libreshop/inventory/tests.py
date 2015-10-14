import logging
from decimal import Decimal
from django.db.utils import IntegrityError
from django.test import TestCase
from shop.models import Address
from inventory.models import (Warehouse, Attribute, Inventory, Attribute_Value,
    Location)

# Initialize logger.
logger = logging.getLogger(__name__)

# Create your tests here.
class WarehouseModelTest(TestCase):

    def test_saving_to_and_retrieving_warehouses_from_the_database(self):
        '''
        Test that a Warehouse can be successfuly saved to the database.
        '''
        warehouse = Warehouse(name='foo', address=Address.objects.create())
        warehouse.save()

        num_warehouses = Warehouse.objects.all().count()
        self.assertEqual(num_warehouses, 1)


class AttributeModelTest(TestCase):

    def test_saving_to_and_retrieving_attributes_from_the_database(self):
        '''
        Test that an Attribute can be successfuly saved to the database.
        '''
        attribute = Attribute(name='foo')
        attribute.save()

        num_attributes = Attribute.objects.all().count()
        self.assertEqual(num_attributes, 1)


class AttributeValueModelTest(TestCase):

    def test_saving_to_and_retrieving_attribute_values_from_the_database(self):
        '''
        Test that an Attribute Value can be successfuly saved to the database.
        '''
        inventory = Inventory.objects.create(name='foo')
        attribute = Attribute.objects.create(name='bar')
        attribute_value = Attribute_Value(attribute=attribute,
            inventory=inventory, value='baz')
        attribute_value.save()

        num_attribute_values = Attribute_Value.objects.all().count()
        self.assertEqual(num_attribute_values, 1)


    def test_inventory_can_have_multiple_unique_attributes(self):
        '''
        Test that multiple distinct Attributes can be associated to an Inventory
        object.
        '''
        inventory = Inventory.objects.create(name='foo')
        attribute1 = Attribute.objects.create(name='bar')
        attribute2 = Attribute.objects.create(name='baz')
        attribute_value1 = Attribute_Value.objects.create(attribute=attribute1,
            inventory=inventory, value='qux')
        attribute_value2 = Attribute_Value.objects.create(attribute=attribute2,
            inventory=inventory, value='quux')

        num_associated_attributes = (Attribute_Value.objects.
            filter(inventory=inventory).count())

        self.assertEqual(num_associated_attributes, 2)


    def test_inventory_cannot_have_multiple_similar_attributes(self):
        '''
        Test that multiple similar Attributes cannot be associated to an
        Inventory object.
        '''
        inventory = Inventory.objects.create(name='foo')
        attribute = Attribute.objects.create(name='bar')
        attribute_value1 = Attribute_Value.objects.create(attribute=attribute,
            inventory=inventory, value='baz')

        func = Attribute_Value.objects.create

        self.assertRaises(IntegrityError, func, attribute=attribute,
            inventory=inventory, value='qux')


class LocationModelTest(TestCase):

    def test_saving_to_and_retrieving_locations_from_the_database(self):
        '''
        Test that a Location can be successfuly saved to the database.
        '''
        inventory = Inventory.objects.create(name='foo')
        warehouse = Warehouse.objects.create(name='bar',
            address=Address.objects.create())
        location = Location(warehouse=warehouse, inventory=inventory,
            quantity=Decimal(0.00))

        location.save()

        num_locations = Location.objects.all().count()
        self.assertEqual(num_locations, 1)


class InventoryModelTest(TestCase):

    def test_saving_to_and_retrieving_inventory_from_the_database(self):
        '''
        Test that an Inventory object can be successfuly saved to the database.
        '''
        inventory = Inventory(name='foo')
        inventory.save()

        num_inventory = Inventory.objects.all().count()
        self.assertEqual(num_inventory, 1)