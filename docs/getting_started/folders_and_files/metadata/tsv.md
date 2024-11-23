# TSV files

A Tab-Separate Values (TSV) file is a text file where tab characters (`\t`) separate fields that are in the file.
It is structured as a table, with each column representing a field of interest,
and each row representing a single datapoint.

## Python

In Python, the easiest way to work with TSV files is to use the [Pandas library](https://pandas.pydata.org/).
This provides a high-level structure to organize, manipulate, clean, and visualize tabular data.
You can install `pandas` with the following command:

```bash
pip install pandas
```

## MATLAB / Octave

Since MATLAB R2013b,
there is a [`readtable`](https://www.mathworks.com/help/matlab/ref/readtable.html) function that can load TSV files,
and a [`writetable`](https://www.mathworks.com/help/matlab/ref/writetable.html) function to write them.

For Octave, the `writetable` function is not implemented in older version of Octave
(e.g 4.2.2) and the `table` function differs from its MATLAB counterpart,
so it may be easier to rely on [bids-matlab](https://github.com/bids-standard/bids-matlab) functions
([`bids.util.tsvwrite`](https://bids-matlab.readthedocs.io/en/main/utility_functions.html#bids.util.tsvwrite) and
[`bids.util.tsvread`](https://bids-matlab.readthedocs.io/en/main/utility_functions.html#bids.util.tsvread))
to help you work with those files.

## R

Reading and writing tab separated files comes natively in R, no need for extra packages.

## Reading a `.tsv` file

=== "python"

    In this example, we assume the .tsv includes column names (headers),
    and explicitly set column separator (delimiter) to tab (`'\t'`).

    ```python
    import pandas as pd
    data = pd.read_csv("file.tsv", sep="\t", headers=True)
    ```

=== "MATLAB"

    ```matlab
    table_content = readtable('file.tsv', ...
                              'FileType', 'text', ...
                              'Delimiter', '\t', ...
                              'TreatAsEmpty', {'N/A','n/a'});
    ```

=== "octave"

    The example below uses the [bids-matlab](https://github.com/bids-standard/bids-matlab) library.

    ```matlab
    table_content = bids.util.tsvread('file.tsv');
    ```

=== "R"

    In this example, we assume the .tsv includes column names (headers),
    and explicitly set column separator (delimiter) to tab (`'\t'`)

    ```R
    data = read.table('file.tsv', header=TRUE, sep='\t')
    ```

=== "Excel / LibreOffice Calc"

    Excel, [LibreOffice Calc](https://www.libreoffice.org/) and similar software to work with tables
    should have no problem opening TSV files.

## Writing a `.tsv` file

=== "python"

    ```python
    import pandas as pd

    participants = pd.DataFrame(
        {
            "participant_id": ["sub-01", "sub-02"],
            "age": [20, 30],
            "sex": ["m", "f"],
        }
    )
    participants.to_csv("participants.tsv")
    ```

=== "MATLAB"

    ```matlab
    participant_id = ['sub-01'; 'sub-02'];
    age = [20; 30]';
    sex = ['m'; 'f'];
    participants = table(participant_id, age, sex);

    writetable(participants, ...
               'participants.tsv', ...
               'FileType', 'text', ...
               'Delimiter', '\t');
    ```

=== "Octave"

    The example below uses the [bids-matlab](https://github.com/bids-standard/bids-matlab) library.

    ```matlab
    participants = struct(...
        'participant_id', ['sub-01', 'sub-02'];
        'age', [20, 30]';
        'sex', ['m', 'f']
        );

    bids.util.tsvwrite('participants.tsv', participants);
    ```

=== "R"

    When writing files, column and row names are always saved,
    we remove row names and quotes from the output explicitly by setting them to `FALSE`.

    ```R
    participant_id <- c('sub-01', 'sub-02');
    age <- c(20, 30);
    sex <- c('m', 'f');
    participants <- data.frame(participant_id, age, sex)
    write.table(participants,
                file='participants.tsv',
                sep='\t',
                row.names = FALSE,
                quote = FALSE)
    ```
