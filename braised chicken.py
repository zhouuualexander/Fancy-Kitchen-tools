def main():
    #Got the ingredient information from Baidu
    raw_material = {"oyster_sauce":6000,"hoisin_sauce":900,"taste_fresh":1200,"dark_soy_sauce":800,"abalone_sauce":1000}
    total = 0
    for items in raw_material:
        total = total+raw_material[items]
    ratio_water_tl = 3.5
    ratio_water_chicken = 0.5
    water = total * ratio_water_tl
    chicken = 2000
    ginger = 60
    mushroom = 60
    new_water = chicken * ratio_water_chicken
    ratio_water = new_water/water
    chicken_legs = input("Enter the weight of chicken legs: ")
    huangmenji_water = ratio_water_chicken* int(chicken_legs)
    huangmenji_original_water = huangmenji_water / ratio_water
    huangmenji_tl = huangmenji_original_water/ ratio_water_tl
    ratio_oyster_sauce = raw_material["oyster_sauce"]/total
    ratio_hoisin_sauce = raw_material["hoisin_sauce"]/total
    ratio_taste_fresh = raw_material["taste_fresh"]/total
    ratio_dark_soy_sauce = raw_material["dark_soy_sauce"]/total
    ratio_abalone_sauce = raw_material["abalone_sauce"]/total
    huangmenji_hy = huangmenji_tl * ratio_oyster_sauce
    huangmenji_hxj = huangmenji_tl *ratio_hoisin_sauce
    huangmenji_wjx = huangmenji_tl * ratio_taste_fresh
    huangmenji_crlk = huangmenji_tl * ratio_dark_soy_sauce
    huangmenji_byz = huangmenji_tl* ratio_abalone_sauce
    tl_new = huangmenji_water/4.5
    hy_new = tl_new* ratio_oyster_sauce 
    hxj_new = tl_new* ratio_hoisin_sauce
    wjx_new = tl_new* ratio_taste_fresh
    crlk_new = tl_new* ratio_dark_soy_sauce
    byz_new = tl_new* ratio_abalone_sauce
    tl_new1 = (hy_new + hxj_new+wjx_new +crlk_new+byz_new)
    shui = tl_new1*3.5
    tiaoliaoshui = tl_new1 + shui
    ratio_ginger = 2000/60
    ginger = int(chicken_legs) / ratio_ginger
    dic = {hy_new:'oyster_sauce:',hxj_new:'hoisin_sauce:',wjx_new:'taste_fresh:',crlk_new:'dark_soy_sauce:',byz_new:'abalone_sauce:',ginger:'ginger:'}
    for key, value in dic.items():
        print(value+str(int(key))+'g')
    print('water:' +str(int(shui)) +'g')
main()