import numpy as np
import pandas as pd
import os
import sys
import inspect
import tests.context
import pytest
import shutil

import ipfsapi

from core.blockchain.blockchain_utils import getter, setter
from core.configuration import ConfigurationManager
from core.dataset_manager import DatasetManager
from core.db_client import DBClient

@pytest.fixture(scope='session')
def ipfs_client(good_config_manager):
    good_config_manager = good_config_manager.get_config()
    return ipfsapi.connect(good_config_manager.get('BLOCKCHAIN', 'host'), 
                            good_config_manager.getint('BLOCKCHAIN', 'ipfs_port'))

@pytest.fixture(scope='session')
def good_config_manager():
    config_manager = ConfigurationManager()
    config_manager.bootstrap(
        config_filepath='tests/artifacts/provenance/configuration.ini'
    )
    return config_manager

@pytest.fixture(scope='session')
def good_dataset_manager(good_config_manager, ipfs_client, db_client):
    dsm = DatasetManager(good_config_manager)
    dsm.configure(ipfs_client, db_client)
    return dsm

@pytest.fixture(scope='session')
def db_client():
    """
    Maintain instance of DB Client
    """
    config_manager = ConfigurationManager()
    config_manager.bootstrap(
        config_filepath='tests/artifacts/db_client/configuration.ini'
    )
    return DBClient(config_manager)

def reset(db_client, data_provider_list):
    """
    Clean up before and after tests.
    """
    classifications = db_client._get_classifications()
    for data_provider in data_provider_list:
        classifications = classifications[classifications['data_provider'] != data_provider]
    classifications.to_sql(
        name=db_client.table_name, 
        con=db_client.db.engine, 
        if_exists='replace', 
        index=False
    )

def test_post_ed(good_dataset_manager, db_client):
    key = "hello world"
    good_dataset_manager.bootstrap()
    receipt = good_dataset_manager.post_directories_and_category_labels(key)
    assert receipt
    # reset(db_client, [key])