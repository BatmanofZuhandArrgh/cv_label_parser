import os
import cv2
import random

from utils.utils import get_yaml

LABELS = get_yaml(config_path='config/obj_cls.yaml')

def plot_one_box(x, img, color=None, label=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.001 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]

        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        text_bottom_left_coord =  (c1[0], c1[1] -2)
        if c2[1] <0:
            c2 = c1[0] + t_size[0], c1[1] + t_size[1] + 3
            text_bottom_left_coord =   (c1[0], c1[1] + t_size[1] +3 -2)
        cv2.circle(img, c1, radius=2, color = (255,255,255))
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, text_bottom_left_coord, 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def draw_bbox(image_path, label_path, output_path):
    
    label_colors = {key: [random.randint(0, 255) for _ in range(3)] for key in LABELS.keys()}

    img = cv2.imread(image_path)
    img_h, img_w, _ = img.shape
    print(img_h, img_w)
    os.makedirs(output_path, exist_ok=True)
    with open(label_path, 'r') as f:
        lines = f.readlines()

    # img = cv2.resize(img, (577, 385), interpolation = cv2.INTER_AREA)
    img_h, img_w, _ = img.shape

    for line in lines:
        label = LABELS[line[0]]
        elements = line.strip().split(' ')[1:]
        elements = [float(x) for x in elements]
        xywh = [a*b for a,b in zip(elements,[img_w, img_h, img_w, img_h])]
        xyxy = (xywh[0] - xywh[2]/2,xywh[1] - xywh[3]/2, xywh[0] + xywh[2]/2,xywh[1] + xywh[3]/2)
        plot_one_box(x=xyxy, img=img, label=label, color=label_colors[line[0]])

    
    # img = cv2.resize(img, (550, 385), interpolation = cv2.INTER_AREA)

    cv2.imwrite(os.path.join(output_path, os.path.basename(image_path)), img)



def draw_folder_bbox():
    pass


def main():
    # eda(folder_path='./sample/input', output_directory='./sample/output/output/analysis')

    # draw_bbox(
    #         image_path = '/home/anhnguyen/Documents/CubeSat/JAXA/obj_train_data/181006_cube1.jpg', 
    #         label_path = '/home/anhnguyen/Documents/CubeSat/JAXA/obj_train_data/181006_cube1.txt',
    #         output_path= './sample/output/viz'
            
    #         )
    draw_bbox(
        image_path = '/home/anhnguyen/Documents/CubeSat/JAXA/obj_train_data/riyo_news_JCUBE20211025.jpg', 
        label_path = '/home/anhnguyen/Documents/CubeSat/JAXA/obj_train_data/riyo_news_JCUBE20211025.txt',
        output_path= './sample/output/viz'
        
        )

if __name__ == '__main__':
    main()