from nhanvien import NhanVien

class NhanVienVP(NhanVien):
    
    def __init__(self, ten='', so_nam_cong_tac=1 , muc_luong =0 , so_ngay_nghi = 0) -> None:
        super().__init__(ten, so_nam_cong_tac)
        self.__muc_luong = muc_luong
        self.__so_ngay_nghi = so_ngay_nghi

    def get_muc_luong(self):
        return self.__muc_luong

    def set_muc_luong(self, value):
        self.__muc_luong = value

    def get_so_ngay_nghi(self):
        return self.__so_ngay_nghi

    def set_so_ngay_nghi(self, value):
        self.__so_ngay_nghi = value

    def __str__(self) -> str:
        return super().__str__() + f" muc luong: {self.get_muc_luong()} so ngay nghi: {self.get_so_ngay_nghi()} + luong: {self.luong()}" 
    
    def luong(self):
        return self.get_muc_luong() - self.get_so_ngay_nghi() * 10
    