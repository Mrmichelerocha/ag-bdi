import json
import os
from typing import Any, Optional
from typing import Tuple
from cosmpy.aerial.wallet import PrivateKey
from uagents.crypto import Identity
import pandas as pd


class KeyValueStore:
    def __init__(self, name: str, cwd: str = None):
        self._data = {}
        self._data_belief = {}
        self._name = name or "my"

        cwd = cwd or os.getcwd()
        self._path = os.path.join(cwd, f"{self._name}_data.json")

        if os.path.isfile(self._path):
            self._load()

    def get(self, key: str) -> Optional[Any]:
        return self._data.get(key)
    
    def get_belief(self, key: str) -> Optional[Any]:
        belief_data = self._load_belief()
        return belief_data.get(key)
    
    def all_belief(self) -> Optional[Any]:
        return self._load_belief()

    def has(self, key: str) -> bool:
        return key in self._data

    def set(self, key: str, value: Any):
        self._data[key] = value
        self._save()

    def remove(self, key: str):
        if key in self._data:
            del self._data[key]
            self._save()

    def clear(self):
        self._data.clear()
        self._save()

    def _load(self):
        with open(self._path, "r", encoding="utf-8") as file:
            self._data = json.load(file)

    def _load_belief(self):
        belief_dir = os.path.join(os.getcwd(), "belief")
        belief_file_path = os.path.join(belief_dir, f"{self._name}_belief.json")

        if os.path.isfile(belief_file_path):
            with open(belief_file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return None

    def _save(self):
        with open(self._path, "w", encoding="utf-8") as file:
            json.dump(self._data, file, ensure_ascii=False, indent=4)
            
    def set_belief(self, key: str, value: Any):
        self._data_belief[key] = value
        self._save_belief()
    
    def _save_belief(self):
        belief_dir = os.path.join(os.getcwd(), "belief")
        
        os.makedirs(belief_dir, exist_ok=True)
        
        belief_file_path = os.path.join(belief_dir, f"{self._name}_belief.json")
        
        with open(belief_file_path, "w", encoding="utf-8") as file:
            json.dump(self._data_belief, file, ensure_ascii=False, indent=4)
            

def load_all_keys() -> dict:
    private_keys_path = os.path.join(os.getcwd(), "private_keys.json")
    if os.path.exists(private_keys_path):
        with open(private_keys_path, encoding="utf-8") as load_file:
            return json.load(load_file)
    return {}


def save_private_keys(name: str, identity_key: str, wallet_key: str):
    private_keys = load_all_keys()
    private_keys[name] = {"identity_key": identity_key, "wallet_key": wallet_key}

    private_keys_path = os.path.join(os.getcwd(), "private_keys.json")
    with open(private_keys_path, "w", encoding="utf-8") as write_file:
        json.dump(private_keys, write_file, indent=4)


def get_or_create_private_keys(name: str) -> Tuple[str, str]:
    keys = load_all_keys()
    if name in keys.keys():
        private_keys = keys.get(name)
        return private_keys["identity_key"], private_keys["wallet_key"]

    identity_key = Identity.generate().private_key
    wallet_key = PrivateKey().private_key

    save_private_keys(name, identity_key, PrivateKey().private_key)
    return identity_key, wallet_key
