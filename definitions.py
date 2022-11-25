import random

IMAGEDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset/images/"
NEWCSVDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset_new/"
NEWIMAGEDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset_new/images/"

RESIZE = 500
IMG_NUM_EACH_TYPE = 500

START = 1
END = 29 # Type_num + 1

def random_crop(img_width, img_height):
    point_x = random.randint(int(img_width*0.3), int(img_width*0.6))
    point_y = random.randint(0, int(img_height*0.25))
    up = point_y
    left = 0 if point_x - RESIZE/2 <= 0 else point_x - RESIZE/2
    right = img_width if point_x + RESIZE/2 >= img_width else point_x + RESIZE/2
    down = img_height if point_y + RESIZE >= img_height else point_y + RESIZE
    #print(left, up, right, down)
    return (left, up, right, down)


def is_1(type):
    return 1 if type == 1 else 0
def is_2(type):
    return 1 if type == 2 else 0
def is_3(type):
    return 1 if type == 3 else 0
def is_4(type):
    return 1 if type == 4 else 0
def is_5(type):
    return 1 if type == 5 else 0
def is_6(type):
    return 1 if type == 6 else 0
def is_7(type):
    return 1 if type == 7 else 0
def is_8(type):
    return 1 if type == 8 else 0
def is_9(type):
    return 1 if type == 9 else 0
def is_10(type):
    return 1 if type == 10 else 0
def is_11(type):
    return 1 if type == 11 else 0
def is_12(type):
    return 1 if type == 12 else 0
def is_13(type):
    return 1 if type == 13 else 0
def is_14(type):
    return 1 if type == 14 else 0
def is_15(type):
    return 1 if type == 15 else 0
def is_16(type):
    return 1 if type == 16 else 0
def is_17(type):
    return 1 if type == 17 else 0
def is_18(type):
    return 1 if type == 18 else 0
def is_19(type):
    return 1 if type == 19 else 0
def is_20(type):
    return 1 if type == 20 else 0
def is_21(type):
    return 1 if type == 21 else 0
def is_22(type):
    return 1 if type == 22 else 0
def is_23(type):
    return 1 if type == 23 else 0
def is_24(type):
    return 1 if type == 24 else 0
def is_25(type):
    return 1 if type == 25 else 0
def is_26(type):
    return 1 if type == 26 else 0
def is_27(type):
    return 1 if type == 27 else 0
def is_28(type):
    return 1 if type == 28 else 0
