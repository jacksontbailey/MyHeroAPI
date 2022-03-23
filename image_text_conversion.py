import io, os, asyncio, sys
from google.cloud import vision
from typing import List

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = None #Insert json file name for Google Creds
client = vision.ImageAnnotatorClient()



async def get_image_text(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    await texts



async def list_items_in_folder(parent_folder):
    print("started list_items function")
    dict_of_files = {}
    files = os.listdir(parent_folder)


    for f in files:
        child_path = f"{parent_folder}/{f}"
        print(f"This is the child path #{len(child_path)}{child_path}")
        dict_of_files[child_path] = await asyncio(get_image_text(child_path))
    return dict_of_files

if __name__== "__main__":
    primary_folder = None #insert file path for image folder.
    api_data = asyncio.run(list_items_in_folder(primary_folder))
    print(api_data)
else:
    args: List[str] = sys.argv
    primary_folder = args[1]
    api_data = asyncio.run(list_items_in_folder(primary_folder))
    print(api_data)
