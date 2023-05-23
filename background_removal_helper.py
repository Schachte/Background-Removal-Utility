from carvekit.web.schemas.config import MLConfig
from carvekit.web.utils.init_utils import init_interface
from PIL import Image
import torch
import os

def background_removal(input_dir, output_dir, input_extension=".png"):
    SEGMENTATION_NETWORK = "tracer_b7"
    PREPROCESSING_METHOD = "stub"
    POSTPROCESSING_METHOD = "fba"
    SEGMENTATION_MASK_SIZE = 512
    TRIMAP_DILATION = 8
    TRIMAP_EROSION = 8
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    BACKGROUND_COLOR = (0, 0, 0)  # Black background

    config = MLConfig(
        segmentation_network=SEGMENTATION_NETWORK,
        preprocessing_method=PREPROCESSING_METHOD,
        postprocessing_method=POSTPROCESSING_METHOD,
        seg_mask_size=SEGMENTATION_MASK_SIZE,
        trimap_dilation=TRIMAP_DILATION,
        trimap_erosion=TRIMAP_EROSION,
        device=DEVICE,
        background_color=BACKGROUND_COLOR
    )

    interface = init_interface(config)

    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(input_extension):
            image_path = os.path.join(input_dir, file_name)
            image = Image.open(image_path)

            if image.mode != "RGB":
                image = image.convert("RGB")

            print(f"Beginning removal on {file_name}...")
            result = interface([image])

            result_file_name = file_name.replace(input_extension, ".png")
            result_path = os.path.join(output_dir, result_file_name)
            result[0].save(result_path)
            print(f"Saved {file_name} to {result_path}")
