# The save methods are not part of the build process
# They are used whenever I am pulling new data from other sources.

import json
import csv
import collections
import os
import os.path

from .datamap import DataMap
from .reader import DataReader

from .functions import flatten, determine_fields, extract_sub_data

class DataReaderWriter(DataReader):
    "A data reader that can also be used to create and update data"

    def save_base_map(self, location, base_map):
        "Writes a data map to a location in the data directory"
        location = self.get_data_path(location)
        result = base_map.to_list()

        with open(location, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

    def save_base_map_csv(self, location, base_map, *, groups=['name']):
        location = self.get_data_path(location)
        if 'name' not in groups:
            raise Exception("Name is a required group for base maps")

        results = []
        for base_obj in base_map.to_list():
            for row in flatten(base_obj, groups=groups):
                results.append(row)

        fields = determine_fields(results)
        with open(location, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fields, lineterminator='\n')
            writer.writeheader()
            writer.writerows(results)

    def save_data_json(self, location, data_map, *, root=None, fields=None, lang='en'):
        """Write a DataMap to a location in the data directory.

        If root is a string, then the saving is restricted to what's inside that key.
        The result is flattened such that the root field doesn't exist in the output.

        If root is a data map, then fields also within the base map are omitted

        If fields are given, only fields within the list are exported
        """
        location = self.get_data_path(location)
        result = extract_sub_data(data_map, root=root, fields=fields, lang=lang)
        with open(location, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

    def save_data_csv(
            self,
            location,
            data_map,
            *,
            lang='en',
            nest_additional=[],
            groups=[],
            root=None,
            fields=None):
        """Write a DataMap to a location in the data directory.

        If root is a string, then the saving is restricted to what's inside that key.
        The result is flattened such that the root field doesn't exist in the output.

        If root is a data map, then fields also within the base map are omitted

        If fields are given, only fields within the list are exported.

        TODO: Write about nest_additional and groups
        """
        location = self.get_data_path(location)
        extracted = extract_sub_data(data_map, root=root, fields=fields, lang=lang)
        result = flatten(extracted, nest=['name_'+lang] + nest_additional, groups=groups)

        fields = determine_fields(result)
        with open(location, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fields, lineterminator='\n')
            writer.writeheader()
            writer.writerows(result)

    def save_split_data_map(self, location, base_map, data_map, key_field, lang='en'):
        """Writes a DataMap to a folder as separated json files.
        The split occurs on the value of key_field.
        Fields that exist in the base map are not copied to the data maps
        """
        location = self.get_data_path(location)

        # Split items into buckets separated by the key field
        split_data = collections.OrderedDict()
        for entry in data_map.values():
            base_entry = base_map[entry.id]

            # Create the result entry. Fields are copied EXCEPT for base ones
            result_entry = {}
            for key, value in entry.items():
                if key not in base_entry:
                    result_entry[key] = value

            # Add to result, key'd by the key field
            split_key = entry[key_field]
            split_data[split_key] = split_data.get(split_key, {})
            split_data[split_key][entry.name(lang)] = result_entry

        os.makedirs(location, exist_ok=True)
        # todo: should we delete what's inside?

        # Write out the buckets into separate json files
        for key, items in split_data.items():
            file_location = os.path.join(location, f"{key}.json")

            # Validation to make sure there's no backpathing
            if not os.path.commonprefix([location, file_location]):
                raise Exception(f"Invalid Key Location {file_location}")

            with open(file_location, 'w', encoding='utf-8') as f:
                json.dump(items, f, indent=4, ensure_ascii=False)
