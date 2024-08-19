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
    
    start_index = xml_text.find('term="Matrix X">') + len('term="Matrix X">')
    end_index = xml_text.find('<', start_index)
    matrix_X = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Matrix Y">') + len('term="Matrix Y">')
    end_index = xml_text.find('<', start_index)
    matrix_Y = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Matrix Z">') + len('term="Matrix Z">')
    end_index = xml_text.find('<', start_index)
    matrix_Z = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Mfg Model">') + len('term="Mfg Model">')
    end_index = xml_text.find('<', start_index)
    mfg_model = xml_text[start_index:end_index].strip()

    start_index = xml_text.find('term="Pulse Sequence">') + len('term="Pulse Sequence">')
    end_index = xml_text.find('<', start_index)
    pulse_sequence = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="TE">') + len('term="TE">')
    end_index = xml_text.find('<', start_index)
    TE = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="TR">') + len('term="TR">')
    end_index = xml_text.find('<', start_index)
    TR = xml_text[start_index:end_index].strip()
    
    start_index = xml_text.find('term="Coil">') + len('term="Coil">')
    end_index = xml_text.find('<', start_index)
    coil = xml_text[start_index:end_index].strip()
    
    image_resolution = str(matrix_X) + 'x' + str(matrix_Y) + str(matrix_Z) \
    + ', ' + str(pixel_spacing_X) + 'x' + str(pixel_spacing_Y) + 'x' + str(slice_thickness) + 'mm'

    # Create a dictionary to hold the extracted information
    data = {
        'Manufacturer': manufacturer,
        'Image': image_resolution,
        'Mfg Model': mfg_model,
        'Pulse Sequence': pulse_sequence,
        'Filename': filename,
        'TE': TE,
        'TR': TR,
        'Coil': coil
    }

    return data

# Define the directory where your XML files are located
directory = 'E:\SDU_University\PhD Project\Paper - KAN\Metadata\METADATA-MRI-ALL'

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
