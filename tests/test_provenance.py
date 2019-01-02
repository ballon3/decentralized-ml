# import numpy as np
# import pandas as pd
# import os
# import sys
# import inspect
# import tests.context
# import pytest
# import shutil

# import ipfsapi

# from core.blockchain.blockchain_utils import getter, setter
# from core.configuration import ConfigurationManager
# from core.dataset_manager import DatasetManager
# from core.db_client import DBClient

# TEST_NONEXISTENT_KEY = 'nonexistence'
# TEST_SINGLE_KEY = 'singleton'
# TEST_MULTIPLE_KEY = 'multiplicity'
# TEST_VALUE = 'World!'

# @pytest.fixture(scope='session')
# def ipfs_client(small_config_manager):
#     good_config_manager = small_config_manager.get_config()
#     return ipfsapi.connect(good_config_manager.get('BLOCKCHAIN', 'host'), 
#                             good_config_manager.getint('BLOCKCHAIN', 'ipfs_port'))

# @pytest.fixture
# def db_client():
#     """
#     Maintain instance of DB Client
#     """
#     config_manager = ConfigurationManager()
#     config_manager.bootstrap(
#         config_filepath='tests/artifacts/db_client/configuration.ini'
#     )
#     return DBClient(config_manager)

# @pytest.fixture(scope='session')
# def small_config_manager():
#     config_manager = ConfigurationManager()
#     config_manager.bootstrap(
#         config_filepath='tests/artifacts/dataset_manager/configuration.ini'
#     )
#     return config_manager

# @pytest.fixture(scope='session')
# def small_dataset_manager(small_config_manager):
#     return DatasetManager(small_config_manager)

# def test_post_ed_directory(small_dataset_manager, small_config_manager, ipfs_client, db_client):
#     # get_val_before = getter(
#     #     client=ipfs_client,
#     #     key=TEST_SINGLE_KEY,
#     #     local_state=[],
#     #     port=blockchain_config_manager.getint('BLOCKCHAIN', 'http_port'),
#     #     timeout=blockchain_config_manager.getint('BLOCKCHAIN', 'timeout')
#     # )
#     small_dataset_manager.bootstrap()
#     small_dataset_manager.configure(ipfs_client, db_client)
#     tx_receipt = small_dataset_manager.post_dataset("hello world")
#     assert tx_receipt, "Setting failed"
#     # small_config_manager = small_config_manager.get_config()
#     # get_val_after = getter(
#     #     client=ipfs_client,
#     #     key=TEST_SINGLE_KEY,
#     #     local_state=[],
#     #     port=small_config_manager.getint('BLOCKCHAIN', 'http_port'),
#     #     timeout=small_config_manager.getint('BLOCKCHAIN', 'timeout')
#     # )
#     # assert get_val_after == get_val_before + [TEST_VALUE], "Setter failed!"

# def test_get_ed(db_client):
#     actual = db_client._get_data_providers_with_category('default_category')
#     assert list(actual['category'])[-1] == 'default_category'
