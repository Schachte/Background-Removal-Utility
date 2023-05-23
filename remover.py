from background_removal_helper import background_removal

input_directory = "./photos"
output_directory = "./results"
input_extension = ".jpeg"

print(f"Removing background from all {input_extension} files")
background_removal(input_directory, output_directory, input_extension)
print("Background removal complete")