import json
import lzma
import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad


class File:
    def __init__(self):
        self._file_key = ""
        self._decode_key = ""
        self._data = {}
        self._edited = False
        self._path = None

    def __bool__(self):
        return self._path is None

    @property
    def file_key(self) -> str:
        return self._file_key

    @file_key.setter
    def file_key(self, key: str) -> None:
        self._file_key = key

    @property
    def decode_key(self) -> str:
        return self._decode_key

    @decode_key.setter
    def decode_key(self, key: str) -> None:
        self._decode_key = key

    @property
    def data(self) -> dict:
        return self._data

    @property
    def edited(self) -> bool:
        return self._edited

    @edited.setter
    def edited(self, value: bool) -> None:
        self._edited = value

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value

    @property
    def edited(self) -> bool:
        return self._edited

    @edited.setter
    def edited(self, value: bool) -> None:
        self._edited = value

    def encode(self) -> None:
        keys = (os.getenv(self._file_key).encode(),
                os.getenv(self._decode_key).encode())
        out = json.dumps(self._data)
        cipher_json = AES.new(pad(keys[1], 16), AES.MODE_EAX)
        cipher_file = AES.new(pad(keys[0], 16), AES.MODE_EAX)
        ciphered_json, json_tag = cipher_json.encrypt_and_digest(out.encode())
        compressed = lzma.compress(ciphered_json)
        ciphered_archive, archive_tag = cipher_file.encrypt_and_digest(compressed)
        with open(self._path, 'wb') as f:
            f.write(cipher_json.nonce)
            f.write(json_tag)
            f.write(cipher_file.nonce)
            f.write(archive_tag)
            f.write(ciphered_archive)
        self.edited = False

    def decode(self) -> None:
        keys = (os.getenv(self._file_key).encode(),
                os.getenv(self._decode_key).encode())
        with open(self._path, "rb") as f:
            json_nonce = f.read(16)
            json_tag = f.read(16)
            file_nonce = f.read(16)
            file_tag = f.read(16)
            file_data = f.read()
        cipher_json = AES.new(pad(keys[1], 16), AES.MODE_EAX, json_nonce)
        cipher_file = AES.new(pad(keys[0], 16), AES.MODE_EAX, file_nonce)
        archive = cipher_file.decrypt_and_verify(file_data, file_tag)
        ciphered_json = lzma.decompress(archive)
        json_data = cipher_json.decrypt_and_verify(ciphered_json, json_tag)

        self._data = json.loads(json_data)
