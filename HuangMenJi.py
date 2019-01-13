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
    huangmenji_chicken = input("输入鸡肉的克数: ")
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

    print('蚝油: ' +str(huangmenji_hy) +'g')
    print('海鲜酱: ' + str(huangmenji_hxj)+('g'))
    print('味极鲜: ' + str(huangmenji_wjx)+('g'))
    print('草茹老抽: ' +str(huangmenji_crlk)+('g'))
    print('鲍鱼汁: ' +str(huangmenji_byz)+('g'))
main()