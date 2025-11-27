# Converters

The following list of converters is provided to help you convert your raw data
into a BIDS compliant dataset.

## MRI Converters

Converters for processing MRI data.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="MRI") }}

## MRS Converters

Converters for processing MRS data.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="MRS") }}

## PET Converters

Converters for processing PET data.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="PET") }}

## EEG/MEEG/iEEG Converters

Converters for processing EEG, MEEG, and/or iEEG data.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="EEG") }}

## Physio Converters

Physiological data converters.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="physiological") }}

## BIDS Converters

Converters that take a BIDS dataset as input to convert it into something else.
Not mentioned here are the many software that can import a BIDS data as data
structure they are more familiar with.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="BIDS") }}

## Miscellaneous Converters

Not exactly BIDS converters but are common tools that can used by other BIDS
converters.

{{ MACROS___generate_converter_table(file="converters.yml", data_type="MISC") }}
