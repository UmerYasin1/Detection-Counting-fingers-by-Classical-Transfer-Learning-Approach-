# Detection-Counting-fingers-by-Classical-Transfer-Learning-Approach-

## Problem Statement
Train a model on Fingers dataset to classify or detect them and prompt or massage will be generated to ask you to input required image in train model and your model will detect, is this required image or not.

## Solution:
For this project I build a web application on Django and integrate it with my train model develop on pretrained neural network VGG19 TensorFlow and after training use my  trained weights (.h5) into a function in my backend (Views.py) file and build a user interface with the help of boostrap4. 

## Functional Approach 
<ol>
<li>TensorFlow</li>
<li>Keras</li>
<li>Python </li>
<li>Django</li>
<li>Sqlite3</li>
<li>Html / CSS / Bootstrap4</li>
<li>Numpy</li>
<li>Pandas</li>  
<li>matplotlib</li>  
</ol>

## Data Set 
We have total 18000 fingers dataset and we split it into validation or train dataset with ¼ ratio, and we resize these all images into (224,224) dimensions. 

![alt text](https://github.com/UmerYasin1/Detection-Counting-fingers-by-Classical-Transfer-Learning-Approach-/blob/1fbf086650b7442b510db7536344af7f86aa5f36/download.png?raw=true)

## Experimental Evaluation 
We trained a model on TensorFlow using classical transfer learning We set learning rate for model 0.001 and use Adam optimization algorithm and Cross Entropy function as activation function. We use online google Colab notebook to run our model.  

### We just take three epoch and achieve 95-99 percent accuracy rate.

![alt text](https://github.com/UmerYasin1/Detection-Counting-fingers-by-Classical-Transfer-Learning-Approach-/blob/4137f4c4030a3a186538f53069584ccfa05eeab7/loss.png?raw=true)

![alt text](https://github.com/UmerYasin1/Detection-Counting-fingers-by-Classical-Transfer-Learning-Approach-/blob/4137f4c4030a3a186538f53069584ccfa05eeab7/resuilt.png?raw=true)

## Web Application 

![alt text](https://github.com/UmerYasin1/Detection-Counting-fingers-by-Classical-Transfer-Learning-Approach-/blob/4137f4c4030a3a186538f53069584ccfa05eeab7/Home%20page.PNG?raw=true)

## Conclusion 
 
From our results we clearly see that how vgg19 is so power to classify images. During training model, we also compared it to Mobilenet-V2, Resnet50 and Resnet150 and check how their accuracy varies in between 70-80 percent, but Vgg19 proves it’s power with accuracy of 95-99 percent.  

## References 

<ol> 
<li> Transfer learning and fine-tuning [https://www.tensorflow.org/tutorials/images/transfer_learning]  </li>
<li> Classify images of 0,1,2,3,4 or 5 fingers https://www.kaggle.com/koryakinp/fingers/code Pavel Koryakin (updated 2 years ago (Version 2))  </li>
<li> Save and load models [https://www.tensorflow.org/tutorials/keras/save_and_load] </li>
</ol>
