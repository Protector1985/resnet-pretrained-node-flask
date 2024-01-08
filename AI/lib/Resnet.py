from torchvision import models, transforms
from PIL import Image
import requests
import torch


class Resnet:
    def resnet_processor(self, image_buffer):
        
        #buffer from node.js => image
        image = Image.open(image_buffer.stream)
        
        #show the image to check if it was transmitted correctly
        #image.show()
        
        #loading the pretrained resnet101 for easy inference
        resnet = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
        
        img_pre_processor = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            )
        ])
        
        processed_img = img_pre_processor(image)
        
        #hint, you can show the preprocessed image if you remove ToTensor and Normalize
        
        #resnet expects images in batches. We need to add an dimension to the tensor
        img_batch = torch.unsqueeze(processed_img, 0)
        
        
        #IMPORTANT - we are not training the model so we have to set it to eval mode
        resnet.eval()
        
        output = resnet(img_batch)
        #print(output)
        """OUT: tensor([[[[-0.6623, -0.6794, -0.6965,  ..., -1.4672, -1.4843, -1.4843],
          [-0.6794, -0.6794, -0.6794,  ..., -1.4672, -1.4843, -1.5014],
          [-0.6794, -0.6794, -0.6794,  ..., -1.4672, -1.4843, -1.5014],
          ...,"""

        #Load the imageNet classes from a github repo that I found
        resp = requests.get("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt")
        class_names = []
        if resp.status_code == 200:
            # turn the contents into a list 
            class_names = resp.text.splitlines()
            _, index = torch.max(output, 1)
            
            #index outputs a tensor like tensor([273]) change it to an actual index
            
            #if we want to ouput the percentage then we need to with softmax
            percentage = torch.nn.functional.softmax(output,dim=1)
            
            print(class_names[index[0]])
            
              
        else:
            print("Couln't retrieve the data")
        
        
       
        
        