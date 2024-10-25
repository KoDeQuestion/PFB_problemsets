# PFB 2024: Project Proposal  
Konstantin Queitsch

## Academic Lab Matcher

### Description of problem, biological or other (3-4 sentences)

For first year graduate students in biomedical/life science programs, determining which labs might make for good rotations can be daunting. The aim of this "game"/"program" is to allow users (academics or labs) to populate a profile and match themselves with corresponding profiles (labs or academics) that place an emphasis on the same things (research interests, mentorship styles, work-life-balance, etc.)

### Proposed programming solution (1-3 sentences per sub-point)

Generate a Class framework, that houses user profiles as "records" with "attributes". Records for the class can then be matched between users.

#### Overview of features/stages/components to be implemented
* Generating the class records 
    * Creating a template of questions / scales for weights that users can fill in.
        * Questions might be multiple choice rather than open ended to make encoding / parsing of answers easier downstream.
    * Generating and populating Dummy "Labs" records (maybe named for the TAs).
    * Importing and parsing class records to populate a combined database.
* Writing Code to Match Class Records and Match Rank
    * Weighting the attribute matches appropriately
* Writing Code to Output the Matches in a Compelling/Informative Manner.

#### How the proposed code solves the problem
"Labs/users" can make themselves a record, populate the attributes, and see how which labs they best match with! 
#### Desired inputs (data sets, files etc)
Users could be prompted to fill out attributes, and place an importance on them. User input could either be done in command line - if we're limiting to maybe 5 attributes and 5 weights.
Alternatively, we could have user submitted files that are then parsed by our code! I prefer this.
Alternatively, we could allow students to submitted files to be parsed and also try to scrap webpages for labs for the information... But that seems hard with unpredictable websites/incomplete information. 

#### Desired outputs (files, output to screen, plots, web pages, etc)
A ranked list of labs based on matched attributes factoring in the weighted importance to the student. Ideally with plots explaining how a given user arrived at their results.
Preferably generate a web page for results that shows plots of the matchings. Example alignment heatmap for a given attribute (labs could be arranged in the quadrants based on matches)

![Example Alignment Heatmap](https://www.researchgate.net/profile/Noel-Malod-Dognin/publication/316241039/figure/fig1/AS:616384237146118@1523968862475/Relationships-between-alignment-scores-The-heat-map-presents-the-agreements-between-the.png)


#### Potential challenges that may be encountered

Determining how to associate importance to a given attribute for the class - nested structures?

### Anticipated programming concepts (logic, data structures, modules, algorithms, etc.) to be used in implementing the solution (1-2 sentences for each concept)

* FileIO - How to read in semi variable information, determining how to out matches in an informative, fun manner.
* Classes - Each student/lab would be a "record" in a class, allowing for many attributes to be associated with each student/lab.
* Plotting/Visualization - We'd have to learn how to generate basic heatmaps in python. 
