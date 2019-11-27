import json
import os.path

from mhdata.util import joindicts, extract_fields, group_fields
from .datamap import DataMap
from .reader import DataReader

class DataStitcher:
    """Dynamically creates an object by attaching data to a base object
    Methods in this class chain to each other.

    Common concepts:
     - key - If given, the added data will be added as entry[keyname] = yourdata.

     - groups - If you have defense_base and defense_map, you can use group defense
                to join them together as defense: { base: val, max: val}.
                Not necessary if a schema is provided to get() that handles it.
    """

    def __init__(self, reader: DataReader, *, key_join='name_en', dir=''):
        self.reader = reader
        self.key_join = key_join
        self.dir = dir
        self._data_map = None

    def _get_filename(self, filename):
        "Gets a filename relative to the internal dir, if any."
        if self.dir:
            return os.path.join(self.dir, filename)
        return filename

    @property
    def languages(self):
        languages = []
        if self.key_join.startswith('name_'):
            languages.append(self.key_join[5:])
        return languages

    @property
    def data_map(self):
        if self._data_map is None:
            raise Exception("Data Map uninitialize, use a load datamap function first")
        return self._data_map

    def base_csv(self, data_file, *, groups=[]):
        """Sets the base map from a CSV file, and return self"""
        data_file = self._get_filename(data_file)
        self._data_map = self.reader.load_base_csv(data_file, groups=groups, languages=self.languages)
        return self

    def base_json(self, data_file):
        # NOTE: this will be removed in a later version
        data_file = self._get_filename(data_file)
        self._data_map = self.reader.load_base_json(data_file)
        return self

    def extend_base(self, filename, *, groups=[]):
        filename = self._get_filename(filename)
        dataitems = self.reader.load_list_csv(filename)
        if not dataitems:
            return self

        groups = set(['name'] + groups)
        
        # todo: have it check the first column name and allow joins on other languages
        
        # Get first column name, whose values will anchor the data to merge
        first_column_name = next(iter(dataitems[0].keys()))

        results = {}
        for item in dataitems:
            key = item[first_column_name]

            # Remove the join from the subdata
            item.pop(first_column_name) 
            
            results[key] = group_fields(item, groups=groups)

        self.data_map.merge(results)

        return self

    def add_json(self, data_file, *, key=None):
        """
        Loads a data map from a json file, adds it to the base map, and returns self.
        
        If a key is given, it will be added under key, 
        Otherwise it will be merged without overwrite.
        """

        self.reader.load_data_json(
            parent_map=self.data_map, 
            data_file=self._get_filename(data_file), 
            key_join=self.key_join, 
            key=key)

        return self

    def add_csv(self, data_file, *, key=None, groups=[]):
        """Loads a data map from a csv file, adds to the base map, and returns self.
        
        Data loaded through this method are joined and available as a list.

        If a key is given, it will be added under key, 
        Otherwise it will be merged without overwrite.
        """

        self.reader.load_data_csv(
            parent_map=self.data_map, 
            data_file=self._get_filename(data_file),
            key=key,
            groups=groups,
            leaftype="list")

        return self

    def add_csv_ext(self, data_file, *, key=None, groups=[]):
        """Loads a data map from a csv file, adds to the base map (1-1), and returns self.
        
        Data loaded through this method are joined one to one and available as a dictionary.

        If a key is given, it will be added under key, 
        Otherwise it will be merged without overwrite.
        """

        self.reader.load_data_csv(
            parent_map=self.data_map, 
            data_file=self._get_filename(data_file),
            key=key,
            groups=groups,
            leaftype="dict")

        return self
    
    def get(self, *, schema=None):
        """Returns the stiched result. 
        If schema is provided, returns the items run through the marshmallow schema
        """
        if schema:
            results = DataMap(languages=self.languages)
            for entry in self.data_map.values():
                data = entry.to_dict()
                (converted, errors) = schema.load(data, many=False) # converted

                if errors:
                    name = entry.name('en')
                    raise Exception(f"Error loading {name}: {str(errors)}")

                # id may have changed type or value:
                # get the converted id before the original,
                # but default to original if missing or falsey
                entry_id = converted.get('id', None) or entry.id

                results.add_entry(entry_id, converted)
                
            return results

        return self.data_map
