from nhanvien import NhanVien

class NhanVienSX(NhanVien):
    def __init__(self, ten='', so_nam_cong_tac=1 , so_sp = 0) -> None:
        super().__init__(ten, so_nam_cong_tac)
        self.__so_sp = so_sp

    def get_so_sp(self):
        return self.__so_sp

    def set_so_sp(self, value):
        self.__so_sp = value

    def __str__(self) -> str:
        return super().__str__() + f" so sp: {self.get_so_sp()} luong: {self.luong()}"   
    
    def luong(self):
        return self.get_so_sp() * 10
