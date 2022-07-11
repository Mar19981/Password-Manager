import json, lzma, os, Cryptodome.Random as r
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
        return self._path == None


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
        keys = (os.getenv(self._file_key).encode(), os.getenv(self._decode_key).encode())
        out = json.dumps(self._data)
        cipherJson = AES.new(pad(keys[1], 16), AES.MODE_EAX)
        cipherFile = AES.new(pad(keys[0], 16), AES.MODE_EAX)
        cipheredJson, jsonTag = cipherJson.encrypt_and_digest(out.encode())
        compressed = lzma.compress(cipheredJson)
        cipheredArchive, archiveTag = cipherFile.encrypt_and_digest(compressed)
        with open(self._path, 'wb') as f:
            f.write(cipherJson.nonce)
            f.write(jsonTag)
            f.write(cipherFile.nonce)
            f.write(archiveTag)
            f.write(cipheredArchive)
        self.edited = False
    
    def decode(self) -> None:
        keys = (os.getenv(self._file_key).encode(), os.getenv(self._decode_key).encode())
        with open(self._path, "rb") as f:
            jsonNonce = f.read(16)
            jsonTag = f.read(16)
            fileNonce = f.read(16)
            fileTag = f.read(16)
            fileData = f.read()
        cipherJson = AES.new(pad(keys[1], 16), AES.MODE_EAX, jsonNonce)
        cipherFile = AES.new(pad(keys[0], 16), AES.MODE_EAX, fileNonce)
        archive = cipherFile.decrypt_and_verify(fileData, fileTag)
        cipheredJson = lzma.decompress(archive)
        jsonData = cipherJson.decrypt_and_verify(cipheredJson, jsonTag)

        self._data = json.loads(jsonData)


    
