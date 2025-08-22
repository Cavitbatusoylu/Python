from abc import ABC, abstractmethod

class Makine(ABC):
    @abstractmethod
    def calis(self):
        pass

class CamasirMakinesi(Makine):
    def calis(self):
        print("Çamaşır makinesi çalıştı!")

class BulasikMakinesi(Makine):
    def calis(self):
        print("Bulaşık makinesi çalıştı!")

c1 = CamasirMakinesi()
b1 = BulasikMakinesi()

c1.calis()
b1.calis()

class Insan:
    def camasirYika(self, makine: CamasirMakinesi):
        if isinstance(makine, CamasirMakinesi):
            print("İnsan çamaşırları makineye attı!")
            makine.calis()
        else:
            print("Bu makinede çamaşır yıkayamazsın!")

i1 = Insan()
i1.camasirYika(c1)   # Çalışır
i1.camasirYika(b1)   # Uyarı verir