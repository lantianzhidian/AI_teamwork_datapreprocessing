import pandas as pd
from PIL import Image


from definitions import *




train_csv = pd.DataFrame(pd.read_csv('cloud_dataset/train.csv', sep = ','))
for type in range(START,END):
    train_csv_n = train_csv[train_csv['Code'] == type]
    image_number = train_csv_n.size / 2 # 2 colnums 
    image_count = 0 # image_num counter
    df = pd.DataFrame(columns=['file_name', 'type1', 'type2', 'type3', 'type4',\
        'type5', 'type6', 'type7', 'type8', 'type9', 'type10', 'type11', 'type12',\
            'type13', 'type14', 'type15', 'type16', 'type17', 'type18', 'type19', 'type20',\
                'type21', 'type22', 'type23', 'type24', 'type25', 'type26', 'type27', 'type28']) # dataFrame format
    
    #print(train_csv_n)
    for index in train_csv_n.index: # xian ba yuan you de tupian resize, bu gou zai jia
        '''if image_count >= IMG_NUM_EACH_TYPE:
            break'''
        image_count += 1
        img_name = train_csv_n.loc[index].values[0] # get img name of one type
        #print(img_name)
        img = Image.open(IMAGEDIR + img_name)
        out = img.resize((RESIZE, RESIZE), Image.ANTIALIAS)
        out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png') # new image name
        df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
            is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame
    #df.to_csv(NEWCSVDIR + 'train.csv', mode = 'a', index = False, header = False) # write dataFrame to csv file
    while (image_count < IMG_NUM_EACH_TYPE):
        for index in train_csv_n.index:
            if image_count >= IMG_NUM_EACH_TYPE:
                break
            img_name = train_csv_n.loc[index].values[0]
            img = Image.open(IMAGEDIR + img_name)
            # FLIP_LEFT_RIGHT
            image_count += 1
            img_l_r = img.transpose(Image.FLIP_LEFT_RIGHT)
            out = img_l_r.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame
            # FLIP_LEFT_RIGHT_90
            image_count += 1
            img_l_r_90 = img_l_r.transpose(Image.ROTATE_90)
            out = img_l_r_90.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame
            # FLIP_LEFT_RIGHT_270
            image_count += 1
            img_l_r_270 = img_l_r.transpose(Image.ROTATE_270)
            out = img_l_r_270.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame

            # FLIP_TOP_BOTTOM
            image_count += 1
            img_t_b = img.transpose(Image.FLIP_TOP_BOTTOM)
            out = img_t_b.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame

            # 90
            image_count += 1
            img_90 = img.transpose(Image.ROTATE_90)
            out = img_90.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame

            # 180
            image_count += 1
            img_180 = img.transpose(Image.ROTATE_180)
            out = img_180.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame

            # 270
            image_count += 1
            img_270 = img.transpose(Image.ROTATE_270)
            out = img_270.resize((RESIZE, RESIZE), Image.ANTIALIAS)
            out.save(NEWIMAGEDIR + str(type) + '_' + str(image_count) + '.png', 'png')
            df.loc[image_count] = [str(type) + '_' + str(image_count) + '.png', is_1(type), is_2(type), is_3(type), is_4(type), is_5(type), is_6(type), is_7(type),\
                is_8(type), is_9(type), is_10(type),is_11(type), is_12(type), is_13(type), is_14(type), is_15(type), is_16(type), is_17(type), is_18(type), is_19(type), is_20(type),\
                    is_21(type), is_22(type), is_23(type), is_24(type), is_25(type), is_26(type), is_27(type), is_28(type)] # insert data in dataFrame
    
    df.to_csv(NEWCSVDIR + 'train.csv', mode = 'a', index = False, header = False) # write dataFrame to csv file

'''
for index in train_csv_6.index:
    file_name = train_csv_6.loc[index].values[0]
    img = Image.open(IMAGEDIR + file_name)
    out = img.resize((500, 500), Image.ANTIALIAS)
    out.save(PWD + str(index) + '.png', 'png')
'''
    


#print(train_csv_6.head(133))

