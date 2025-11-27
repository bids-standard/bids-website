These are the three main types of files you'll find in a BIDS dataset:

1.  `.json` files that contain `key: value` metadata
1.  `.tsv` files that contain tables of metadata
1.  Raw data files (for example: `.jpg` files for images or `.nii.gz` files for fMRI data.)

BIDS has a standardized way of naming files that tries to implement the
following principles:

-   Do not include white spaces in file names
    -   They make scripting harder.

-   Use only letters, numbers, hyphens, and underscores.
    -   Some operating systems cannot handle special characters.

-   Do not rely on letter case (`UPPERCASE` and `lowercase`)
    -   For some operating systems `a` is the same as `A`.

-   Use separators and case in a systematic and meaningful way.
    -   [`thisIsCamelCase`](https://en.wikipedia.org/wiki/Camel_case)
    -   [`this_is_snake_case`](https://en.wikipedia.org/wiki/Snake_case)

Source: [Datalad RDM course](https://psychoinformatics-de.github.io/rdm-course/02-structuring-data/index.html)

## Filename template

<!--
    check the css file src/_static/myfile.css
    to modify the color related to the different "var" below
 -->

<h3 style="padding: 40px; text-align:center; width: 100%; border-style: solid">
    <span style="color: var(--key)">key1</span>
    <span style="color: black">-</span>
    <span style="color: var(--label)">value1</span>
    <span style="color: var(--underscore)">_</span>
    <span style="color: var(--key)">key2</span>
    <span style="color: black">-</span>
    <span style="color: var(--label)">value2</span>
    <span style="color: var(--underscore)">_</span>
    <span style="color: var(--suffix)">suffix</span>
    <span style="color: var(--ext)">.extension</span>
</h3>

<p>
    <ul>
        <li><span style="color: var(--suffix)">Suffixes</span> are preceded by an <span style="color: var(--underscore)">underscore</span></li>
        <li>Entities are composed of <span style="color: var(--key)">key</span><span style="color: black">-</span><span style="color: var(--label)">value</span> pairs separated by <span style="color: var(--underscore)">underscores</span></li>
        <li>There is a limited set of <span style="color: var(--suffix)">suffixes</span> for each data type (anat, func, eeg, …)</li>
        <li>For a given <span style="color: var(--suffix)">suffix</span>, some entities are <b>required</b> and some others are <b>[optional]</b>.</li>
        <li><span style="color: var(--key)">Entity keys</span> and <span style="color: var(--suffix)">suffixes</span> can only contain letters and/or numbers.</li>
        <li><span style="color: var(--label)">Entity values</span> can only contain letters and/or numbers and/or the "+" character.</li>
        <li>Entity <span style="color: var(--key)">key</span><span style="color: black">-</span><span style="color: var(--label)">value</span> pairs have a specific order in which they must appear in filename.</li>
        <li>Some entities <span style="color: var(--key)">key</span><span style="color: black">-</span><span style="color: var(--label)">value</span> can only be used for
derivative data.</li>
    </ul>
</p>

## Modalities

{{ MACROS___generate_filename_templates() }}
