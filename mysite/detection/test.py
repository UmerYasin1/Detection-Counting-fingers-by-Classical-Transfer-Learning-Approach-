# import tensorflow as tf
# import numpy as np
# from keras_preprocessing import image
#
#
#
# new_model = tf.keras.models.load_model(r'E:\Programming force\CNN\02-09-2021\wepapp\first_try2.h5')
#
# new_model.summary()
#
# def pridict(path):
#
#     img_pred = image.load_img('/Dataset/MyDrive/Dataset/val/0L/ea0d961b-9762-46cc-bade-7e69b5bd9542_0L.png',
#                               target_size=(224, 224, 3))
#     img_pred = image.img_to_array(img_pred)
#     img_pred = np.expand_dims(img_pred, axis=0)
#
#     result = new_model.predict(img_pred)
#     print(result)
#     predicted_categories = tf.argmax(result, axis=1)
#     pridict = predicted_categories.numpy()
#
#
#     return pridict
import glob
import os

def remove():
    files = glob.glob(r'E:\Programming force\CNN\02-09-2021\wepapp\mysite\images\*')

    for f in files:

        os.remove(f)