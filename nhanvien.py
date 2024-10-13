from abc import ABC , abstractmethod

class NhanVien(ABC):
    
    def __init__(self , ten = '' , so_nam_cong_tac = 1) -> None:
        self.__ten = ten
        if(so_nam_cong_tac <= 0):
            self.__so_nam_cong_tac = 1
        else:
            self.__so_nam_cong_tac = so_nam_cong_tac
        if(so_nam_cong_tac == 1):
            self.__phu_cap = 100
        else:
            self.__phu_cap = 100 + ((self.__so_nam_cong_tac - 1) * 20)
            

    def get_ten(self):
        return self.__ten

    def set_ten(self, ten):
        self.__ten = ten

    def get_so_nam_cong_tac(self):
        return self.__so_nam_cong_tac

    def set_so_nam_cong_tac(self, so_nam_cong_tac):
        if(so_nam_cong_tac <= 0):
            self.__so_nam_cong_tac = 1
        else:
            self.__so_nam_cong_tac = so_nam_cong_tac
        if(so_nam_cong_tac == 1):
            self.__phu_cap = 100
        else:
            self.__phu_cap = 100 + ((self.__so_nam_cong_tac - 1) * 20)

    def get_phu_cap(self):
        return self.__phu_cap

    @abstractmethod
    def luong(self):
        pass

    def __str__(self) -> str:
        return f"ten nv: {self.get_ten()} nam cong tac: {self.get_so_nam_cong_tac()} phu cap: {self.get_phu_cap()}"
    