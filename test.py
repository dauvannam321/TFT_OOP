class Champion:
    def __init__(self, loai, attack, defend):
        self.loai = loai
        self.attack = attack
        self.defend = defend
        self.damage = 0

    def tinhSatThuong(self, luot):
        pass

class Jarvan(Champion):
    def __init__(self, attack, defend):
        super().__init__(1, attack, defend)

    def tinhSatThuong(self, luot):
        self.damage = self.defend * 2
        return self.damage

class Reksai(Champion):
    def __init__(self, attack, defend):
        super().__init__(2, attack, defend)

    def tinhSatThuong(self, luot):
        if luot % 4 == 0 and luot!=0:
            self.damage = self.attack * 2
            return self.damage
        else:
            self.damage = self.attack
            return self.damage

class Sivir(Champion):
    def __init__(self, attack, defend):
        super().__init__(3, attack, defend)

    def tinhSatThuong(self, luot):
        self.damage = self.attack * 2
        return self.damage

class Illaoi(Champion):
    def __init__(self, attack, defend):
        super().__init__(4, attack, defend)

    def tinhSatThuong(self, luot):
        if (self.attack + self.defend) % 2 == 0:
            self.damage = (self.attack + self.defend) // 2
            return self.damage
        else:
            self.damage = (float)((self.attack + self.defend) / 2)
            return self.damage

def main():
    n, m = map(int, input().split())
    champions = []

    # Nhap va tinh gia tien cua cac tuong
    total_price = 0
    for i in range(n):
        loai, attack, defend = map(int, input().split())
        if loai == 1:
            champion = Jarvan(attack, defend)
            champions.append(champion)
            total_price+=1
        elif loai == 2:
            champion = Reksai(attack, defend)
            champions.append(champion)
            total_price+=2
        elif loai ==3:
            champion = Sivir(attack, defend)
            champions.append(champion)
            total_price+=4            
        elif loai == 4:
            champion = Illaoi(attack, defend)
            champions.append(champion)
            total_price+=1


    DauSi = []
    TienCong = []
    CongNghe = []

    # kiem tra dieu kien chi so cong them
    for i in champions:
        if i.loai == 1 and (i.__class__.__name__ not in (CongNghe and DauSi)):
            CongNghe.append(i.__class__.__name__)
            DauSi.append(i.__class__.__name__)
        elif i.loai == 2 and (i.__class__.__name__ not in (TienCong and DauSi)):
            TienCong.append(i.__class__.__name__)
            DauSi.append(i.__class__.__name__)
        elif i.loai == 3 and i.__class__.__name__ not in CongNghe:
            CongNghe.append(i.__class__.__name__)
        elif i.loai == 4 and (i.__class__.__name__ not in (TienCong and DauSi)):
            TienCong.append(i.__class__.__name__)
            DauSi.append(i.__class__.__name__)
    # print("DauSi: ", DauSi, " - TienCong: ", TienCong, " - CongNghe: ", CongNghe)
    # tinh chi so cong them
    for i in champions:
        if len(DauSi) == 2 and (i.loai == 1 or i.loai == 2 or i.loai == 4):
            i.defend += 15
        if len(DauSi) == 3 and (i.loai == 1 or i.loai == 2 or i.loai == 4):
            i.defend += 30
        if len(TienCong) >=2 and (i.loai == 2 or i.loai == 4):
            i.attack += 30
        if len(CongNghe) >=2 and (i.loai == 1 or i.loai == 3):
            i.attack += 15
            i.defend += 15

    # in ra chi so sau khi cong
    # for i in champions:        
    #     print(f'{i.__class__.__name__} - attack: {i.attack} - defend: {i.defend}')

    # bat dau tinh sat thuong
    for luot in range(1, m + 1):
        # print("*"*10 + "Luot " + str(luot) + "*"*10)
        for i in champions:
            # print(f'{i.__class__.__name__} - attack: {i.attack} - defend: {i.defend}')
            i.damage+=i.tinhSatThuong(luot)
            # print("Sat thuong gay ra: ", i.damage)

   
    # in ra ket qua       
    for i in champions:        
        print(f'{i.__class__.__name__} - sat thuong gay ra: {i.damage}')
    print(f'Tong gia tri: {total_price}')
if __name__ == "__main__":
    main()
