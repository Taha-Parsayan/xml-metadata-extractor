# XML metadata extractor

### Description
Typically, MRI and PET images contain metadata within xml files. Each subject has it's own xml file and therefore, it would be time-consumming to open all the files one by one and read their information to report in an article.
In here, I provided 2 python files to automatiically open and read the xml files for MRI and PET metadata within the related folders.

*Extracted information for MRI:*

Manufacturer: The name of the manufacturer of the imaging equipment.
Pixel Spacing X: The pixel spacing in the X direction.
Pixel Spacing Y: The pixel spacing in the Y direction.
Slice Thickness: The thickness of the imaging slices.
Matrix X: The number of pixels in the X dimension of the image matrix.
Matrix Y: The number of pixels in the Y dimension of the image matrix.
Matrix Z: The number of pixels in the Z dimension of the image matrix.
Mfg Model: The model of the imaging equipment.
Pulse Sequence: The pulse sequence used in the imaging.
TE (Echo Time): The echo time parameter used in the imaging.
TR (Repetition Time): The repetition time parameter used in the imaging.
Coil: The type of coil used in the imaging.
Image Resolution: A string combining Matrix X, Matrix Y, Matrix Z, Pixel Spacing X, Pixel Spacing Y, and Slice Thickness into a descriptive format.

*Extracted information for PET:*

Manufacturer: The name of the manufacturer of the imaging equipment.
Image Resolution:
Number of Rows: Number of rows in the image matrix.
Number of Columns: Number of columns in the image matrix.
Number of Slices: Number of slices in the image stack.
Pixel Spacing X: The pixel spacing in the X direction.
Pixel Spacing Y: The pixel spacing in the Y direction.
Slice Thickness: Thickness of each image slice.
Image Resolution Format: Combines the number of rows, columns, slices, pixel spacings, and slice thickness into a single descriptive string.
Mfg Model: The model of the imaging equipment.
Reconstruction: The type of reconstruction used in the imaging process.

---
You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material
- for any purpose, even commercially.

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but
