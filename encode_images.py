import torch
import clip
import glob
from pathlib import Path
from PIL import Image

device="cuda:0"
basedir=Path('Data/Urban_scene_dataset_Amsterdam')
outputfile='clip_ams'

def main():
  model, preprocess = clip.load("ViT-L/14@336px", device=device)

  output = []
  outputalist = []
  pattern = (basedir / '*.jpg')
  for f in glob.glob(str(pattern)):
    i = Path(f).stem
    with Image.open(f) as image:
      image_input = preprocess(image).unsqueeze(0).to(device)
      with torch.no_grad():
          image_features = model.encode_image(image_input)
    outputalist.append([int(i), image_features])
 
  for i, e in sorted(outputalist): 
    print(i,e[0,:8])
    output.append(e)
  image_encodings = torch.stack(output, dim=1).to('cpu').to(torch.float32).squeeze(0)
  torch.save(image_encodings, outputfile)


if __name__=="__main__":
  main()
