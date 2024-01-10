# Tools for working with bids-website

This README file describes the tools under the `/tools` directory of the bids-website repository.

## Adding Steering Group meeting notes

1. Install all Python requirements under `tools/requirements.txt`
1. Install pandoc
1. Create a folder called `inputs` under `tools`
1. Nest a folder with the year corresponding to the meeting notes you want to add (e.g., `2023`) in `inputs`
1. Getting the meeting notes
    1. Go to the Google Drive folder where the meeting notes you want to add are located
    1. See if you can make minor formatting tweaks (removing weird formatting, cleaning up tables, etc.)
    1. Download them as `.docx` files
    1. Place all files in your "year" folder that you created above
1. From the command line, navigate to `tools`, and then run `make all`
1. Clean up, check the newly added files, commit

## Update the Gantt chart of completed BEPs
