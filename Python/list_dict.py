"""
Tools for working with dictionaries within lists
"""
# Standard Imports
from typing import Union


def index_by_value(list_of_dicts: list, key: str, value: Union[str, int]) -> int:
    """
    Get the index of a dictionary within a list with matching key value pair

    Parameters
    ----------
    list_of_dicts: list [{}, {}, ...]
        The list of dictionaries to index by key value
    key: str
        The key in the dictionaries to use for value matching
    value: Union[str, int]
        The value to match

    Returns
    -------
    int
        The index of dictionary within the list with matching key value pair
    """
    for list_index, dictionary in enumerate(list_of_dicts):
        if dictionary[key] == value:
            return list_index
    raise Exception("No dictionary has matching key value pair")


def difference(A: list, B: list) -> list:
    """
    Get the elements of A not in B

    Parameters
    ----------
    A, B: list
        List of dictionaries

    Returns
    -------
    list
        List of dictionaries from A that are not in B
    """
    output = []
    for item in A:
        if item not in B:
            output.append(item)
    return output


def remove_key(list_of_dicts: list, key: str) -> list:
    """
    Removes a key from all dictionaries

    Parameters
    ----------
    list_of_dicts: list
        List of dictionaries with keys to remove
    key: str
        The key to remove from each dictionary

    Returns
    -------
    list
        List of dictionaries after removing keys
    """
    output = []
    for record in list_of_dicts:
        temp = record.copy()
        del temp[key]
        output.append(temp)
    return output


def remove_key_if_in_key(list_of_dicts: list, value_in_key: str) -> list:
    """
    Remove key from all dictionaries if a value is in the key

    Parameters
    ----------
    list_of_dicts: list
        List of dictionaries with keys to remove
    value_in_key: str
        The value in the key to search for and remove

    Returns
    list
        List of dictionaries after removing keys
    """
    output = []
    for record in list_of_dicts:
        temp = {}
        for key in record.keys():
            if value_in_key not in key:
                temp[key] = record[key]
        output.append(temp)
    return output
