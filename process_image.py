import io
import base64
from PIL import Image
from rembg import remove

def process_image(input_path, output_txt_path, max_size=400):
    print(f"Reading {input_path}...")
    with open(input_path, 'rb') as i:
        input_data = i.read()
    
    print("Removing background...")
    output_data = remove(input_data)
    
    img = Image.open(io.BytesIO(output_data))
    
    # Resize image to save base64 space (e.g. max width/height of 400px)
    img.thumbnail((max_size, max_size))
    
    print(f"Resized image to {img.size}")
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    # Prepend the data URI scheme so it's ready to use in SVG
    data_uri = f"data:image/png;base64,{img_str}"
    
    with open(output_txt_path, 'w') as f:
        f.write(data_uri)
    
    print(f"Saved base64 string to {output_txt_path}")

if __name__ == '__main__':
    input_file = "ChatGPT Image Aug 16, 2026, 10_44_39 PM.png"
    output_file = "avatar_base64.txt"
    process_image(input_file, output_file)
