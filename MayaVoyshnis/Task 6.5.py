class Sun:
    __instance = None

    @classmethod
    def inst(cls):
        if cls.__instance is None:
            cls.__instance = Sun()
        return cls.__instance


p = Sun.inst()
f = Sun.inst()
k = Sun.inst()
print(k is f)
