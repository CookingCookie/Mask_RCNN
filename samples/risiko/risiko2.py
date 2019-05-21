# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:12:23 2019

@author: Cookie
"""

def get_polygons_and_objects(annotation):
    polygons = []
    objects = []
    region_list = annotation.get("regions")
    
    for region in region_list:
        shape_attrs = region.get("shape_attributes")
        region_attrs = region.get("region_attributes")
        #print("Shape: {} | Region: {}".format(shape_attrs, region_attrs))
        
        x = shape_attrs.get("x")
        y = shape_attrs.get("y")
        width = shape_attrs.get("width")
        height = shape_attrs.get("height")
        #print("X: {} | Y: {} | W: {} | H: {}".format(x, y, width, height))
        
        all_points_x = (x, x, x+width, x+width)
        all_points_y = (y, y+height, y+height, y)
        polygon = {"name": "polygon", 
                   "all_points_x": all_points_x, 
                   "all_points_y": all_points_y}
        
        polygons.append(polygon)        
        objects.append(region_attrs)
        
        #print("Polygon: {}".format(polygon))
        #print("Objects: {}".format(region_attrs))
        #print("\n")
    return polygons, objects


def get_polygons_and_objects2(annotation):
    return [r['shape_attributes'] for r in a['regions'].values()], [s['region_attributes'] for s in a['regions'].values()]
     
   
if __name__ == "__main__":
    dataset_dir = "C:/Users/Cookie/Downloads"
    
    annotations = json.load(open(os.path.join(dataset_dir, "risiko.json")))
    annotations = annotations.get("_via_img_metadata")
    annotations = list(annotations.values())
    #print("Annotation: {}".format(annotations))
    
    for a in annotations:
        polygons, objects = get_polygons_and_objects(a)
    
