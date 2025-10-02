# Make commit locally

In this exercise you'll work on making changes to a git repository locally and pushing those to GitHub.

## Task 2.1 Clone from GitHub

Locate your own personal repository generated from the GitHub Classroom link and click on the green `Code` - `Open with GitHub Desktop`:

![Open with GitHub Desktop](https://files.mude.citg.tudelft.nl/open_with_github_desktop.png)

This will open a window in GitHub desktop. Select the location where you would like the _local repository_ to be located, the "Local path." 

![Set location of clone](https://files.mude.citg.tudelft.nl/clone_locate.png)

We strongly encourage you follow these pieces of advice:
1. **Do not** store your local repositories in a location that is backed up using cloud software (e.g., OneDrive, Dropbox, etc). This often interferes with the functioning of git. Instead, we will push to the _remote repositories_ to backup our work.
2. **Do not** store your local repositories in locations with spaces in the file path, especially on Windows. While there are ways to deal with this if it happens, you will save yourself trouble down the line if you avoid using spaces in your folder and file names.
3. **Do** store your local repositories for your project in an organized way. We advise creating a main directory, where each of the sub-directories would be a local git repository. Here is an illustrating of such a structure for your working directories:


```
.
├── coding_projects
│   ├── Project_1
|   ├── ...
|   ├── Week_1_1
|   ├── ...
|   ├── Week_1_4
│       ├── PA04.ipynb
│       └── ...
│   └── ...
```

At this point you can create the local repository by clicking "Clone," which will start the process of downloading the files from GitLab to your computer at the location you chose for local path. If you were successful in cloning the repository, you will see something similar to the figure below.

![Successfull clone](https://files.mude.citg.tudelft.nl/successfull_clone.png)

## Task 2.2 Edit files

Now let's make an edit locally. The benefit from working locally is that you can use other software and that you can edit multiple files together in a single commit. To do so, let's add a figure to this repo and include it in this file. Preferably add a non-binary image like an svg, as git and binary files are not friends.

% ADD YOUR FIGURE HERE
% ![]()

## Task 2.3 Commit your changes

Now let's commit your changes (of multiple files). In GitHub Desktop you should see the addition of a figure and your changes to this file. Make sure you select both of these changes and commit those changes by clicking the blue 'Commit 2 files to main'.

## Task 2.4 Push your changes

Now that we have recorded our commits with git, there is one last thing to do: update the remote repository. We can do this by pushing the commit, using the blue 'Push origin' in the middle of the screen or 'Push origin' in the bar on the top.

## Task 2.5 Check your online repository

Check your repository on GitHub to check whether your changes made it there!

> This exercise uses content from https://teachbooks.io/learn-programming/workflows/git/github_desktop/commits_remote.html by Delft University of Technology, licensed with CC BY 4.0 License

> By Tom van Woudenberg and Robert Lanzafame, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).