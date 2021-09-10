
class Cache:
    # private with __
    __store = {}

    # THIS BLOCK demo for PROTECTED if required - Single _
    # _protected_store = {}
    #
    # @property
    # def protected_store(self):
    #     return self._protected_store

    def get(self, key):
        if key:
            try:
                value_for_key = self.__store[key]
            except KeyError:
                return "NOT_FOUND"
            else:
                return f"Get for {key}={value_for_key}"
        else:
            return "INVALID_KEY"

    def set(self, key, value):
        if key:
            self.__store[key] = value
            return f"VALUE SET {key}={value}"
        else:
            return "INVALID_KEY"


cache = Cache()
print(cache.get(1))
print(cache.set(1, "This is the first data inserted"))
print(cache.set(2, 567))
print(cache.get(1))
print(cache.get(2))
print(cache.set(1, None))
print(cache.get(1))

# print(cache.__store) # AttributeError: 'Cache' object has no attribute '__store'
# print(cache._protected_store) # Warning to convert to property. After PyCharm add property:
# print(cache.protected_store) # Now works because of the property
