import pytest

from mhdata.io import DataMap, merge_list

def create_test_entry(name_map, extradata={}):
    return { 'name': name_map, **extradata }

def create_test_entry_en(name, extradata={}):
    return create_test_entry({ 'en': name }, extradata)


def test_starts_with_zero_length():
    map = DataMap()
    assert not len(map), "Expected empty map"

def test_add_entries_adds_length():
    map = DataMap()
    map.insert(create_test_entry_en("test1"))
    map.insert(create_test_entry_en("test2"))
    assert len(map) == 2, "expected 2 entries to exist"

def test_nonmatching_id_throws():
    map = DataMap()
    with pytest.raises(ValueError):
        test_entry = create_test_entry_en("test1")
        map.add_entry(1, { **test_entry, 'id': 25})

def test_uses_provided_id():
    map = DataMap()
    map.insert({ 'id': 3, **create_test_entry_en("test1") })

    assert 3 in map.keys(), "entry should have used id 3"

def test_can_lookup_by_id():
    map = DataMap()
    map.add_entry(55, create_test_entry_en("test1"))
    map.add_entry(1, create_test_entry_en("test2"))
    map.add_entry(8, create_test_entry_en("test3"))

    found = map[1] # note: id order is not sequential
    assert found.name('en') == "test2", "found name should match"

def test_can_lookup_id_by_name():
    map = DataMap()
    map.add_entry(1, create_test_entry_en("test1"))
    map.add_entry(2, create_test_entry_en("test2"))
    map.add_entry(3, create_test_entry_en("test3"))

    idval = map.id_of("en", "test2")
    assert idval == 2, "expected test 2 to have id 1"

def test_can_lookup_entry_by_name():
    map = DataMap()
    map.insert(create_test_entry_en("test1"))
    map.insert(create_test_entry_en("test2"))
    map.insert(create_test_entry_en("test3"))

    entry = map.entry_of("en", "test2")
    assert entry.name('en') == 'test2', "expected entry name to match"

def test_can_iterate_values_in_order():
    expected_names = ['test1', 'test2', 'test3']
    
    map = DataMap()
    for (id, name) in enumerate(expected_names):
        map.add_entry(id, create_test_entry_en(name))
    
    found = [entry['name']['en'] for entry in map.values()]
    assert found == expected_names, "Expected map entries to match"

def test_row_add_value_in_middle():
    test_keys = [ 'id', 'test1', 'test2', 'test3']
    test_dict = { k:1 for k in test_keys }
    test_dict['name'] = { 'en': 'a test' } # required field

    datamap = DataMap()
    entry = datamap.insert(test_dict)

    entry.set_value('NEW', 1, after='test2')

    # note: name exists because it was manually added to test_dict
    expected_keys = ['id', 'test1', 'test2', 'NEW', 'test3', 'name']
    entry_keys = list(entry.keys())
    assert entry_keys == expected_keys, "Expected new to be after test2"

def test_manual_id_resets_sequence():
    datamap = DataMap()

    datamap.add_entry(25, create_test_entry_en('test1'))
    new_entry = datamap.insert(create_test_entry_en('test2'))

    assert new_entry.id > 25, "new id should have been higher"

def test_to_dict_correct_data():
    data = {
        25: create_test_entry_en('test1', { 'id': 25, 'somedata': {'nested': 5}}),
        28: create_test_entry_en('test2', { 'id': 28, 'somedata': {'alsonested': 'hey'}})
    }

    datamap = DataMap()
    for row in data.values():
        datamap.insert(row)

    serialized = datamap.to_dict()
    assert serialized == data, "expected serialized data to match original data"

def test_clone_returns_equal_map():
    data = {
        25: create_test_entry_en('test1', { 'somedata': {'nested': 5}}),
        28: create_test_entry_en('test2', { 'somedata': {'alsonested': 'hey'}})
    }

    datamap = DataMap(data)
    cloned_datamap = datamap.copy()

    assert datamap.to_dict() == cloned_datamap.to_dict(), "expected clone to match"
    assert id(datamap) != id(cloned_datamap), "expecting clone to be a different object"

def test_merge_on_multikey_single():
    data = {
        1: create_test_entry_en("test", { 'type': 'great-sword' }),
        2: create_test_entry_en("test", { 'type': 'bow' })
    }

    datamap = DataMap(data, keys_ex=["type"])

    merge_data = [
        { 'name_en': 'test', 'type': 'great-sword', 'attack': 25 },
        { 'name_en': 'test',  'type': 'bow', 'attack': 10 }
    ]
    merge_list(datamap, merge_data, many=False)

    assert datamap.entry_of("en", "test", "great-sword")['attack'] == 25
    assert datamap.entry_of("en", "test", "bow")['attack'] == 10