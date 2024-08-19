import os
import pandas as pd

# Define a function to extract information from each XML text
def extract_info_from_xml(xml_text, filename):
    # Find the index of "Manufacturer" followed by the next '<' character
    start_index = xml_text.find('term="Manufacturer">') + len('term="Manufacturer">')
    end_index = xml_text.find('<', start_index)
    manufacturer = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Pixel Spacing X">') + len('term="Pixel Spacing X">')
    end_index = xml_text.find('<', start_index)
    pixel_spacing_X = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="Pixel Spacing Y">') + len('term="Pixel Spacing Y">')
    end_index = xml_text.find('<', start_index)
    pixel_spacing_Y = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="Slice Thickness">') + len('term="Slice Thickness">')
    end_index = xml_text.find('<', start_index)
    slice_thickness = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="Number of Rows">') + len('term="Number of Rows">')
    end_index = xml_text.find('<', start_index)
    number_of_rows = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Number of Columns">') + len('term="Number of Columns">')
    end_index = xml_text.find('<', start_index)
    number_of_columns = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Number of Slices">') + len('term="Number of Slices">')
    end_index = xml_text.find('<', start_index)
    number_of_slices = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Mfg Model">') + len('term="Mfg Model">')
    end_index = xml_text.find('<', start_index)
    mfg_model = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Reconstruction">') + len('term="Reconstruction">')
    end_index = xml_text.find('<', start_index)
    reconstruction = xml_text[start_index:end_index].strip()
    
    image_resolution = str(number_of_rows) + 'x' + str(number_of_columns) + str(number_of_slices) \
    + ', ' + str(pixel_spacing_X) + 'x' + str(pixel_spacing_Y) + 'x' + str(slice_thickness) + 'mm'

    # Create a dictionary to hold the extracted information
    data = {
        'Manufacturer': manufacturer,
        'Image': image_resolution,
        'Mfg Model': mfg_model,
        'Reconstruction': reconstruction,
        'Filename': filename
    }

    return data

# Define the directory where your XML files are located
directory = 'E:\SDU_University\PhD Project\Paper - KAN\Metadata\METADATA-PET-ALL'

# Initialize an empty list to hold the data for each file
data_list = []

# Iterate over each XML file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            xml_text = file.read()
        xml_data = extract_info_from_xml(xml_text, filename)
        if xml_data is not None:
            data_list.append(xml_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)


# Delete every 3rd row to reduce the size
indices_to_keep = list(range(2, len(df), 3))
df = df.loc[indices_to_keep]

# Display the DataFrame
print(df)
