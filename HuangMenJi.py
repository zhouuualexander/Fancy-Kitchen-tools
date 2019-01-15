def main():
    hy = 6000
    hxj = 900
    wjx = 1200
    crlk = 800
    byz = 1000
    tl = hy+hxj+wjx+crlk+byz
    water = (hy+hxj+wjx+crlk+byz)*3.5
    chicken = 2000
    ginger = 60
    mushroom = 60
    new_water = 1000
    ratio_water_tl = 3.5
    ratio_water = new_water/water
    ratio_chicken_water = new_water/chicken
    huangmenji_chicken = input("输入🍗的克数: ")
    huangmenji_water = ratio_chicken_water* int(huangmenji_chicken)
    huangmenji_original_water = huangmenji_water / ratio_water
    huangmenji_tl = huangmenji_original_water/ ratio_water_tl
    ratio_hy = hy/tl
    ratio_hxj = hxj/tl
    ratio_wjx = wjx/tl
    ratio_crlk = crlk/tl
    ratio_byz = byz/tl
    huangmenji_hy = huangmenji_tl * ratio_hy
    huangmenji_hxj = huangmenji_tl *ratio_hxj
    huangmenji_wjx = huangmenji_tl * ratio_wjx
    huangmenji_crlk = huangmenji_tl * ratio_crlk
    huangmenji_byz = huangmenji_tl* ratio_byz
    tl_new = huangmenji_water/4.5
    hy_new = tl_new* ratio_hy
    hxj_new = tl_new* ratio_hxj
    wjx_new = tl_new* ratio_wjx
    crlk_new = tl_new* ratio_crlk
    byz_new = tl_new* ratio_byz
    tl_new1 = (hy_new + hxj_new+wjx_new +crlk_new+byz_new)
    shui = tl_new1*3.5
    tiaoliaoshui = tl_new1 + shui
    ratio_ginger = 2000/60
    ginger = int(huangmenji_chicken) / ratio_ginger
    dic = {hy_new:'蚝油: ',hxj_new:'海鲜酱: ',wjx_new:'味极鲜: ',crlk_new:'🍄老抽: ',byz_new:'鲍🐟汁: ',ginger:'姜: ',tl_new1:'调料一共放了: ',tiaoliaoshui:'调料水一共: '}
    for key, value in dic.items():
        print(value,str(int(key))+'g')
    
main()