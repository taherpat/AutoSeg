import cv2
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import matplotlib.pyplot as plt
import gradio as gr

# import segmentation_models_pytorch as smp

##set the device to cuda for sam model
# device = torch.device('cuda')


# image= cv2.imread('image_4.png', cv2.IMREAD_COLOR)
def get_masks( image, model_type):
    print(image)
    # image_pil = Image.fromarray(image.astype('uint8'), 'RGB')
    # print(image_pil)
    if model_type == 'vit_h':
        sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
    if model_type == 'vit_b':
        sam = sam_model_registry["vit_b"](checkpoint="sam_vit_b_01ec64.pth")
        
    if model_type == 'vit_l':
        sam = sam_model_registry["vit_l"](checkpoint="sam_vit_l_0b3195.pth")
    else:
        sam=  sam_model_registry["vit_l"](checkpoint="sam_vit_l_0b3195.pth")
    
    # print(image.shape)
    #set the device to cuda for sam model
    # sam.to(device= device)

    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(image)
    composite_image = np.zeros_like(image)
    colors = plt.cm.jet(np.linspace(0, 1, len(masks)))  # Generate distinct colors

    for i, mask_data in enumerate(masks):
        mask = mask_data['segmentation']
        color = colors[i]
        composite_image[mask] = (color[:3] * 255).astype(np.uint8)  # Apply color to mask
    print(composite_image.shape, image.shape)
    
    # Combine original image with the composite mask image
    overlayed_image = (composite_image * 0.5 + torch.from_numpy(image).resize(738, 1200, 3).cpu().numpy() * 0.5).astype(np.uint8)

    return overlayed_image




iface = gr.Interface(
    fn=get_masks,
    inputs=["image", gr.components.Dropdown(choices=['vit_h', 'vit_b', 'vit_l'], label="Model Type")],
    outputs="image",
    title="SAM Model Segmentation and Classification",
    description="Upload an image, select a model type, and receive the segmented and classified parts."
)

iface.launch()