# Bee Background Removal

This is a sample repository used as an experiment to improve the segmentation applied to the bees in the [Big Bee Project](https://big-bee.net/). The idea is that background removal can be applied as a pre-processing step for image input. This would allow the model to be trained on images with purely black backgrounds, which have shown to have higher accuracy. 

## Local Development Setup

1. Clone the repository
2. Setup virtual environment - `virtualenv env`
3. Active the environment - `source env/bin.activate`
4. Install dependencies - `pip install -r requirements.txt`

## Option 1: Commercial

Option 1 presents an out of the box solution using a commercial API from Photoroom. You can grab an API here [from here](https://www.photoroom.com/api/docs) which provides 10 free images.

There are already examples of input from `./photos` and associated output using `Photoroom` inside of `./commercial_results`. Once you grab your API key, you can run this yourself:

```sh
python commercial_remover.py
```

## Option 2: Opensource removal using Carvekit

Option 2 presents a non-tuned example using [Carvekit](https://github.com/OPHoperHPO/image-background-remove-tool). 

Data is fed in from `./photos` and output in `./results`. For simplicity, sample images for input and output have been included in this repo.

_Running the script_
```sh
python remover.py
```

_Using the API_

```python
from background_removal_helper import background_removal

input_directory = "./photos"
output_directory = "./results"
input_extension = ".jpeg"

print(f"Removing background from all {input_extension} files")
background_removal(input_directory, output_directory, input_extension)
print("Background removal complete")
```