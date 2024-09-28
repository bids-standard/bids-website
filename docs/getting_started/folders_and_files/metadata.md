Metadata are stored in .json and .tsv files.

These files are language-agnostic, meaning you can work with them in, for example: Python, Matlab, or R.

This page covers common ways to read/write these files in common languages for neuroscience analysis.

More extensive example templates can be found
[here](https://github.com/bids-standard/bids-starter-kit/tree/main/templates),
well as [MATLAB / Octave code](https://github.com/bids-standard/bids-starter-kit/tree/main/matlabCode)
and [Python code](https://github.com/bids-standard/bids-starter-kit/tree/main/pythonCode)
to help you generate some of those files.

## JSON Files

JSON stands for JavaScript Object Notation
and as its name indicates takes its syntax from the JavaScript language.

JSON files are text files that take the following structure:

```json
{
    "key": "value",
    "key2": "value2",
    "key3": {
        "subkey1": "subvalue1"
    }
}
```

Note that they can be nested (curly brackets within curly brackets).
Here are some common ways to read / write these files.

### Editing JSON file online

Working with JSON can be a headache if you do not have the proper tools.

To get started we suggest playing around with JSON in an online editor,
to get a feeling for how JSON works.

See for example this one: [http://jsoneditoronline.org/](http://jsoneditoronline.org/)

Online editors can also usually tell you if you forgot a comma,
forgot to close a bracket or something similar.
And even fix mistakes for you.

![](../../assets/img/autofix.png)

### Editing JSON file on your computer

If you need to edit JSON files on your computer, it will make your life easier
if you use a modern code editor like:

-   [visual studio code](https://code.visualstudio.com/)

Modern code editors can tell you if you have a valid JSON file
and highlight the lines where you have errors.
Most of them usually also have code formatting extensions
that can automatically indent your JSON like
[Prettier for vscode](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

#### Matlab / Octave

There are many toolboxes in Matlab for reading / writing JSON files.

Since MATLAB R2016b, you can use the built-in functions `jsonencode` (to write) and `jsondecode` (to read) JSON files.
Hopefully they should be available in Octave 6.1 next year.

The [JSONio library](https://github.com/gllmflndn/JSONio) will allow you to read
and write JSON files with matlab and octave (see examples below to use `jsonwrite` and `jsonread`).

SPM12 uses the JSONio library by calling `spm_jsonwrite` and `spm_jsonread` and
it has [other interesting functions to help you with BIDS](https://en.wikibooks.org/wiki/SPM/BIDS).

[bids-matlab](https://github.com/bids-standard/bids-matlab) has 2 functions
(`bids.util.jsonencode` and `bids.util.jsondecode`) that act as wrappers and
will use whatever implementation (SPM, JSONio, MATLAB) is available.

The examples below are for the [JSONio library](https://github.com/gllmflndn/JSONio):

##### Reading a `.json` file

```matlab
    jsonread([filename])
```

##### Writing a `.json` file

```matlab
root_dir = './';
project = 'temp';
sub_id = '01';
ses_id = '01';
acquisition = 'anat';

anat_json_name = fullfile(root_dir,project,...
                            ['sub-' sub_id],...
                            ['ses-' ses_id],...
                            acquisition,...
                            ['sub-' sub_id '_ses-' ses_id '_T1W.json']);

% Assign the fields in the Matlab structure that can be saved as a json:
anat_json.Manufacturer = 'GE';
anat_json.ManufacturersModelName =  'Discovery MR750';
anat_json.MagneticFieldStrength = 3;
anat_json.PulseSequence = 'T1 weighted SPGR';

json_options.indent = '    '; % this makes the json lThe BIDS statistical models are written in JSON files.

If you have never heard of JSON, this section is for you.

Here we will quickly:

- explain some of the terms that you need to be familiar to work with JSON
- suggest some tools that you may want to use to make it easier for you to work
  with JSON.ook pretier when opened in a txt editor
jsonwrite(loc_json_name,anat_json,json_options)
```

#### Python

In Python, JSON support is built into the core library,
meaning you don't need to install anything to read/write JSON files.
In addition, the structure of JSON is almost identical
to that of Python dictionaries (assuming you are only storing text / numbers in the dictionary).

##### Reading a `.json` file

```python

import json
with open('myfile.json', 'r') as ff:
    data = json.load(ff)
```

##### Writing a `.json` file

```python
import json
data = {'field1': 'value1', 'field2': 3, 'field3': 'field3'}
with open('my_output_file.json', 'w') as ff:
    json.dump(data, ff)
```

#### R

There is a new package to help intract with BIDS datasets: [bidser](https://github.com/bbuchsbaum/bidser)

There are several packages for reading and writing JSON files from R.
In this example, we will be using jsonlite.
Remember to install and call a package before using it.

[jsonlite](https://github.com/jeroen/jsonlite)

```R
    install.packages('jsonlite')
```

##### Reading a `.json` file

```R
    library(jsonlite)
    data = fromJSON('myfile.json', pretty=TRUE)
```

##### Writing a `.json` file

```R
    library(jsonlite)
    data = '{"field1": "value1", "field2": 3, "field3": "field3"}'
    writeLines(data, file="myData.json")
```

### Interoperability issues

Many parts of JSON files are often loaded as
[`structures`](https://nl.mathworks.com/help/matlab/ref/struct.html) by MATLAB / Octave,
where a `key` in a JSON file becomes `fieldname` in that structure.

Here is an example with a simple `example.json`

```json
{
    "key": "value"
}
```

loaded with bids-matlab

```matlab
>> json_content = bids.util.jsondecode('example.json')

json_content =

  struct with fields:

    key: 'value'
```

There are however some strict rules for what makes a valid fieldname in MATLAB and octave.

Fieldnames must:

-   start with a letter, otherwise assigning to that field will error

-   contain only letters, numbers, and/or the underscore character, otherwise assigning to that field will error, and

-   must be no longer than `namelengthmax` (currently 63) characters, otherwise
    you will receive a warning and the field name will be truncated

If there are keys in your JSON that do not comply to those rules,
they keys will be renamed when loading which can lead to some headaches down the line.

For example when loading the `bad_keys.json`

```json
{
    "@foo": "@foo",
    "1": "1",
    "x1": "x1",
    "x_1": "x_1",
    "/t": "/t",
    "%f": "%f"
}
```

We get some quite different fieldnames when read with matlab:

```matlab
>> jsondecode(fileread('bad_keys.json'))

ans =

  struct with fields:

    x_foo: '@foo'
       x1: '1'
     x1_1: 'x1'
      x_1: 'x_1'
      x_t: '/t'
      x_f: '%f'
```

or with JSONio for Octave (though at least here we get a warning):

```matlab
>> jsonread('bad_keys.json')
Warning: Duplicate key.

ans =

  struct with fields:

    x_foo: '@foo'
       x1: 'x1'
      x_1: 'x_1'
      x_t: '/t'
      x_f: '%f'
```

This can lead to some unexpected behavior if you did not know about this.

If you load this `collision.json`

```json
{
    "1": "1",
    "x1": "x1",
    "x_1": "x_1"
}
```

and try to retrieve the value associated to the `key` `x1`, you will in fact be
getting the value for the key `1`.

```matlab
>> json_content = bids.util.jsondecode('collision.json');
>> json_content.x1

       x1: '1'
```

#### Why and when does this matter for BIDS?

In most cases this will not be an issue,
but this could be problem if in your `events.tsv`
you have named some of your trial_type things like `1_face`,
`2_sound` and then want to annotate those events in a side car JSON file like this.

```json
{
    "trial_type": {
        "LongName": "",
        "Description": "image type",
        "Levels": {
            "1_face": "A face is displayed",
            "2_sound": "A sound is played"
        }
    }
}
```

If you do this, it will be much harder to work with that JSON file for anyone who uses MATLAB or Octave.

```{attention}
So in general here are some suggestions on how to name your events:
-   start with a letter
-   make sure they contain only letters, numbers, and/or the underscore character
-   make sure they are must be no longer than currently 63 characters
```

### More about JSON

#### JSON terms

The main "building blocks" of JSON you must be familiar with are `Objects` and `Arrays`.

##### Objects

In JSON, objects

-   are opened and closes by curly brackets `{ }`

-   are a collection of key–value pairs where:

    -   the keys are strings
    -   the key and the value are separated by a colon `:`

For example, this is an object.

```json
{ "Key": "value", "Key2": 1 }
```

As you can see, in JSON strings start and end with double quotes `"`.
Also note the comma between the key-value pairs but not after the last key-value pair.

##### Arrays

In JSON, arrays are:

-   are opened and closes by square brackets `[ ]`
-   an ordered list of zero or more elements, each of which may be of any type (string, number..)
-   elements must be separated by a comma

```json
["this", "is", 1, "JSON", "array"]
```

#### A note on Booleans

In JSON boolean values must be typed as lowercase with no quotes:

-   `true`
-   `false`

#### JSON "styling"

In JavaScript it is custom to use CamelCase to write code,
this is why most of keys you will see in JSON are also in CamelCase.

<!-- Add link to camelcase wikipedia -->

For example:

```json
{ "ThisIsTrue": true, "ThisIsTrue": false }
```

It is common to indent JSON files to improve readability.

```json
{
  "ThisIsTrue": true,
  "ThisIsTrue": false
}
```

Finally, you cannot add comments in JSON files,
but the BIDS stats model allows you to add a `"Description"` key
to most objects to give explanations to the reader.

#### Nesting

JSON allows to "nest" objects within objects, to create arrays of objects
and combine all those elements however deep you want or need.

Just remember to place commas:

-   between array elements
-   between key-value pairs
-   unless this is the last element (or key-value pair)

```json
{
  "MixedArray": ["This", "is", "one", "array"],
  "ArrayOfNumbers": [0, 0, 1, 0, 0],
  "ArrayOfObjects": [
    {
      "NestedObject": true,
      "Content": { "value": 0 }
    },
    {
      "NestedObject": false,
      "Content": 1
    }
  ]
}
```

#### JSON schema

If the content of your JSON must follow certain rules, like

!!! note

    your JSON file must contain a key-value pair
    -   with a key called: "Version"
    -   with a value that must be a number

Then you can specify those rules in what is called a JSON schema.

##### Online

If you are working on a JSON file in the browser like with [http://jsoneditoronline.org/](http://jsoneditoronline.org/),
and if there is a JSON schema for the JSON file you are working on
you can also use that schema to validate while editing
by clicking `Options --> JSON schema --> URL`
and give it the URL to the schema.

See the example below using the [BIDS stats model schema](https://bids-standard.github.io/stats-models/BIDSStatsModel.json):

![](../../assets/img/schema_in_browser.png)

##### On your computer

If you want to validate a JSON file you are editing using a JSON schema
you can do so by adding the following key-value pair in your BIDS stats model,
(here using the BIDS stats model schema as an example)

```json
  "$schema": "https://raw.githubusercontent.com/bids-standard/stats-models/gh-pages/BIDSStatsModel.json",
```

For vs-code you can also add this to your settings:

```json
"json.schemas": [
    {"fileMatch": [
            "model-*_smdl.json"
        ],
        "url": "https://raw.githubusercontent.com/bids-standard/stats-models/gh-pages/BIDSStatsModel.json"
    }
]
```

[Source](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings)

Example of JSON syntax error and BIDS stats model schema error in VS code:

![](../../assets/img/vs_code_validation.png)

## TSV files

A Tab-Separate Values (TSV) file is a text file where tab characters (`\t`) separate fields that are in the file.
It is structured as a table, with each column representing a field of interest,
and each row representing a single datapoint.

Below are ways to read / write TSV files in common languages.

### Matlab

#### Reading a `.tsv` file

```matlab
table_content = readtable(filename, ...
                            'FileType', 'text', ...
                            'Delimiter', '\t', ...
                            'TreatAsEmpty', {'N/A','n/a'});
```

#### Writing a `.tsv` file

##### Matlab

```matlab
root_dir = pwd;
bidsProject = 'temp';
mkdir(fullfile(root_dir, bidsProject));
bids_participants_name = 'participants.tsv';

participant_id = ['sub-01'; 'sub-02'];
age = [20 30]';
sex = ['m';'f'];

t = table(participant_id,age,sex);
writetable(t, fullfile(root_dir, bidsProject, bids_participants_name), ...
              'FileType', 'text', ...
              'Delimiter', '\t');
```

##### Octave

The `writetable` function is not implemented in older version of Octave
(e.g 4.2.2) and the `table` function differs from its matlab counterpart.
These are still in development for future
[releases](https://github.com/apjanke/octave-tablicious) so some of the scripts
provided in the BIDS starter-kit repository in the matlab code folder
to create .tsv might not work with octave because of that reason.

### Python

In Python, the easiest way to work with TSV files is to use the Pandas library.
This provides a high-level structure to organize, manipulate, clean, and
visualize tabular data.
You can install `pandas` with the following command:

`pip install pandas`

#### Reading a `.tsv` file

There are many ways to read a `.tsv` file in Pandas.
One option is the following:

```python
import pandas as pd
pd.read_csv('./ds001/participants.tsv', delimiter='\t')
```

Note that this function will default to using `,` as a delimiter, so we explicitly give it the tab character.

#### Writing a `.tsv` file

You can write to a `.tsv` file using the `to_csv` method of a pandas DataFrame:

```python
import pandas as pd
df = pd.read_csv('./ds001/participants.tsv', delimiter='\t')

# Add an extra column for demonstration
df['subject_id'] = range(len(df))

# Show contents of the dataframe
df.head()
    Out:
          participant_id sex  age  subject_id
    0         sub-01   F   26           0
    1         sub-02   M   24           1
    2         sub-03   F   27           2
    3         sub-04   F   20           3
    4         sub-05   M   22           4

# Save as a .tsv file
df.to_csv('my_new_file.tsv', sep='\t')
```

### Excel

-   Create a file with the following columns
    (at least, for other values see paragraph the
    [BIDS spec](https://bids-specification.readthedocs.io/en/latest/03-modality-agnostic-files.html#participants-file))
    -   participant_id
    -   age
    -   sex

-   Save as tab separated `.txt` and change extension to `.tsv`

### R

Reading and writing tab separated files comes natively in R, no need for extra packages.

#### Reading a `.tsv` file

In this example, we assume the .tsv includes column names (headers),
and explicitly set column separator (delimiter) to tab ('\t')

```R
data = read.table('myFile.tsv', header=TRUE, sep='\t')
```

#### Writing a `.tsv` file

When writing files, column and row names are always saved, we remove row names,
and quotes from the outpur explicitly by setting them to FALSE.

```R
data = cbind.data.frame(
  participant_id = c('sub-01', 'sub-02'),
  age = c(20,30),
  sex = c('m','f'))

write.table(data, file='myData.tsv',sep='\t',
  row.names = FALSE, quote = FALSE)
```
