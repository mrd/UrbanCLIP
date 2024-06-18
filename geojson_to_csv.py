import json
import sys
import csv

outputfile = "ams_image_list.csv"

with open(sys.argv[1]) as fp:
  gj = json.load(fp)

with open(outputfile, 'w') as fp:
  csvw = csv.writer(fp)
  csvw.writerow(['ID','X','Y','angle','primary_function','secondary_function','expert_primary','expert_secondary'])
  for i,feat in enumerate(gj['features']):
    y, x = feat['geometry']['coordinates']
    url = feat['properties']['url']
    rating = feat['properties']['average_walkability']
    csvw.writerow([i,y,x,0,rating])
    imgfile = url[url.rfind('/')+1:]
    print(f'mv img/{imgfile} Data/Urban_scene_dataset_Amsterdam/{i}.jpg')
    
