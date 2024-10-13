
from nhanviensx import NhanVienSX
from nhanvienvp import NhanVienVP
mangNV = []
while True:
    
    print('1. doc danh sach nhan vien')
    print('2. tong tien cong ty tra cho nhan vien')
    print('3. dua ra ds nhan vien co so nam cong tac tren 7 nam')
    print('4. xuat thong tin tat ca nhan vien ra man hinh')
    print('5. thoat')
    chon = int(input('nhap lua chon cua ban: '))
    
    if(chon == 1):
        print("1. nhan vien sx")
        print("2. nhan vien vp")
        tmp = int(input('nhap lua chon cua ban: '))
        if(tmp == 1):
            file = open("./demo3/nhanviensx.txt", "r")
            nv = file.readlines()
            for i in nv:
                data = i.split("~")
                nvsx = NhanVienSX(data[0] , int(data[1]) , int(data[2]))
                mangNV.append(nvsx)
        else:
            file = open("./demo3/nhanvienvp.txt", "r")
            nv = file.readlines()
            for i in nv:
                data = i.split("~")
                nvvp = NhanVienVP( data[0] , int(data[1]) , int(data[2]), int(data[3]))
                mangNV.append(nvvp)
    elif (chon == 2):
        tongTien = 0
        for i in mangNV:
            tongTien += i.luong() + i.get_phu_cap()
            
        print(f"tong luong cty tra: {tongTien}")
    elif (chon == 3):
        for i in mangNV:
            if(i.get_so_nam_cong_tac() >= 7):
                print(i)
    elif (chon == 4):
        for i in mangNV:
            print(i)
    elif (chon == 5):
        break