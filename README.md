Edited on Github web interface

"how to run"
1. open Terminal
2. type "python src\hello.py"


1. created points.csv file

2. Was able to read data points successfully, and print basic information. 
Changed the number of rows, and the code successfully printed the updated information

3. Performed data quality checks, put in a missing value, lon>180, lat>90, 
and code successfully detected those

4. Created bounding box, preview. png and summary.json.
Tested with faulty data and worked


REFLECTIONS

Abstraction:
These points seem to represent prominent buildings/features in the UPD Campus. They are a good list of where to go in UP Diliman.
The script chose to inspect validity of input, like missing values or the range of values that are acceptable and mappable, and prints the
number of valid values, and their bounding box.

Representation:
Even though these features are areal in nature, we choose to represent them as points for simplicity's sake. The users do not need to see the coordinates of the four corners of a building to know its approximate location, and locate them on a map.
We also assume that the users know what latitude and longitude is, or at least the app they are using know how to ingest long/lat datasets

Responsibility:
The script is correct in inspecting the validity of the range of the values, and the number of missing / invalid values, and drawing the bounding box.
However, the script should add a lon/lat interchange check too. Take the first value for example, if we interchange 14.6549 with 121.0651, the script would say this is an invalid latitude value, and would be omitted. However, if we take a closer look, this should still be a valid location, but there is just an error in the interchange of the 2 coordinates. This is a common error, and the script should check for this before totally omitting the point.

However, if this is indeed a UP Diliman guide to prominent buildings and features, a human should check if the values do belong in or near UP Diliman. A value of 123.898, 10.322 is still acceptable to the script, but this is already in UP Cebu, and is no longer useful to the user base

Scale:
When the number of points go towards the millions, the present script might crash with out-of-memory errors, because the script tends to load all into memory all at once. This error could happen at numerous points in the script, like in reading into the dataframe, and plotting in matplotlib.

CSV text files also tend to occupy more memory because all values are saved as text, but looking at the data, we could have saved these as integers with a scale value, and in binary format, and it would reduce the file size significantly.




