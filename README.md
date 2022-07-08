# MACLab Tools
Small collection of code I've used in the past to help me with experiments / analyses
in the MACLab at University of Iowa

Right now this is still going to be a random collection of python scripts that accomplish 
a somewhat random assortment of tasks I used during my PhD to create, modify, or otherwise
manipulate sound files, design experiments, or analyze data.

I'll update this Read Me as I actually find and add these scripts.

The final goal of this project is to actually merge all of these into a single GUI
to share with my current and former labs to ease audio processing and stimuluse design
for research assistants and graduate students.

Current scripts:
- batch_rename.py: This is a simple GUI for renaming all files with a given extension
in a particular folder by appending or prepending characters. I found this useful when
I had made modifications to a large set of files (such as by adding noise, or vocoding)

- orthographic_overlap.py: This is still a work in progress. A basic script to take a 
word list of varying length and iterate over every word to create item sets that
consist of targets, onset competitors (cohorts), offset competitors (rhymes) based
on orthographic overlap. 3 basic parameters at the beginning of the script are 
equal_lenths (should all items in a set have the same number of characters),
cohort_overlap (minimum number of characters onset competitors should share with target),
rhyme_overlap (minimum number of characters offset competitors should share with target)