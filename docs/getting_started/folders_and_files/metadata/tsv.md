# TSV files

A Tab-Separate Values (TSV) file is a text file where tab characters (`\t`) separate fields that are in the file.
It is structured as a table, with each column representing a field of interest,
and each row representing a single datapoint.

## Reading a `.tsv` file

=== "python"

    In Python, the easiest way to work with TSV files is to use the Pandas library.
    This provides a high-level structure to organize, manipulate, clean, and
    visualize tabular data.
    You can install `pandas` with the following command:

    ```bash
    pip install pandas
    ```

    ```python
    import pandas as pd
    data = pd.pd.read_csv("file.tsv", sep="\t", headers=True)
    ```

=== "MATLAB"

    Since MATLAB R2013b, there is a [`readtable`](https://www.mathworks.com/help/matlab/ref/readtable.html) function
    that can load TSV files.

    ```matlab
    table_content = readtable('file.tsv', ...
                              'FileType', 'text', ...
                              'Delimiter', '\t', ...
                              'TreatAsEmpty', {'N/A','n/a'});
    ```

=== "octave"

    ```matlab
    ```

=== "R"

    Reading and writing tab separated files comes natively in R, no need for extra packages.

    In this example, we assume the .tsv includes column names (headers),
    and explicitly set column separator (delimiter) to tab (`'\t'`)

    ```R
    data = read.table('myFile.tsv', header=TRUE, sep='\t')
    ```

=== "Excel / [LibreOffice Calc](https://www.libreoffice.org/)"

## Writing a `.tsv` file

## Matlab

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

## Octave

The `writetable` function is not implemented in older version of Octave
(e.g 4.2.2) and the `table` function differs from its matlab counterpart.
These are still in development for future
[releases](https://github.com/apjanke/octave-tablicious) so some of the scripts
provided in the BIDS starter-kit repository in the matlab code folder
to create .tsv might not work with octave because of that reason.

## Excel

-   Create a file with the following columns
    (at least, for other values see paragraph the
    [BIDS specification](https://bids-specification.readthedocs.io/en/latest/03-modality-agnostic-files.html#participants-file))
    -   participant_id
    -   age
    -   sex

-   Save as tab separated `.txt` and change extension to `.tsv`

## R

### Writing a `.tsv` file

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
