## Import a CSV / JSON file. If condition is met, print two attributes for that condition.
First I would ask why you would want to write a program to support both CSV/JSON files. Because they are very different and serves different purpose and usages.
* CSV: CSV is table format that maps very well to data sets or tabular data, but not all data is tabular! The only scenario that I would use CSV file is I am doing some "streaming" large data set and I need to consider storage space.
* JSON: It is primarily a way to store simple object trees. JSON has no concept of type beyond primitives "string, integer, float, boolean, null" and the collection types array and object.

Second, I would suggest to break this into two files. "json-import.py" and "csv-import.py". I would also ask the size of the files, see if we need to break large data file into small data files. Or we might even want to save data into a database for faster access next time.

Third, I would ask how often this operation is, if it is one time deal, then a simple program is fine, otherwise if it is very frequently, we might want to automate it.

Regarding to conditions, what kind of conditions/requirements are we talking about here? Any examples? Because this will change the way of we loading the file, for example, load a JSON file to string? Dict?