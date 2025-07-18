from PIL import Image
import random

def find_neighbors(coords):
    neighbors = {}
    for coord in coords:
        neighbors[coord] = []
        for other in coords:
            if coord != other and is_touching(coord, other):
                neighbors[coord].append(other)
    return neighbors

def is_touching(coord1, coord2):
    # Check if coord1 and coord2 are within 50 units of each other
    return abs(coord1[0] - coord2[0]) < 50 and abs(coord1[1] - coord2[1]) < 50

def contour(coords):
    neighbors = find_neighbors(coords)
    groups = []
    visited = set()
    
    for coord in coords:
        if coord not in visited:
            group = []
            stack = [coord]
            
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    group.append(current)
                    stack.extend(neighbors[current])
            
            groups.append(group)
    return groups


def create_rectangles(groups):
    rectangles = []
    for group in groups:
        min_x = min(coord[0] for coord in group)
        max_x = max(coord[0] for coord in group)
        min_y = min(coord[1] for coord in group)
        max_y = max(coord[1] for coord in group)
        print(min_x, min_y, max_x, max_y)
        rectangles.append([min_x, min_y, max_x, max_y])  # Store as list of four values
    return rectangles

def extract_pixels(image_array, rectangles):
    groups_of_pixels = []
    for rect in rectangles:
        print(rect)
        min_x, min_y, max_x, max_y = rect
        group_pixels = image_array[min_y:max_y+1, min_x:max_x+1]
        groups_of_pixels.append(group_pixels)
    return groups_of_pixels


def colorize_groups(image_path, groups, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    
    # Assign random colors to each group
    group_colors = {}
    for i, group in enumerate(groups):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for coord in group:
            group_colors[coord] = color
    
    # Apply colors to the corresponding pixels
    for coord, color in group_colors.items():
        if 0 <= coord[0] < img.width and 0 <= coord[1] < img.height:
            pixels[coord[0], coord[1]] = color
    
    img.save(output_path)

'''
def assign_group_colors(groups):
    group_colors = {}
    for i, group in enumerate(groups):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for coord in group:
            group_colors[coord] = color
    return group_colors

def change_pixel_colors(image_path, groups, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    group_colors = assign_group_colors(groups)
    
    for coord, color in group_colors.items():
        if 0 <= coord[0] < img.width and 0 <= coord[1] < img.height:
            pixels[coord[0], coord[1]] = color
    
    img.save(output_path)

# Example usage
coordinates = [(0, 0), (0, 1), (1, 1), (2, 2), (3, 3), (3, 4)]
touching_groups = contour(coordinates)
change_pixel_colors('input_image.png', touching_groups, 'output_image.png')
draw_triangles_around_groups('input_image.png', touching_groups, 'output_image.png')
'''