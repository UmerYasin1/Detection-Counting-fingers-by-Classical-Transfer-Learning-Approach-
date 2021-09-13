import numpy as np
import tensorflow as tf
from keras_preprocessing import image


new_model = tf.keras.models.load_model(r'E:\Programming force\CNN\02-09-2021\wepapp\first_try2.h5')

new_model.summary()

def pridict(path):

    img_pred = image.load_img(path,
                              target_size=(224, 224, 3))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)

    result = new_model.predict(img_pred)
    print(result)
    predicted_categories = tf.argmax(result, axis=1)
    pridict = predicted_categories.numpy()


    return pridict