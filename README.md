# projectsort
Simple tools for organizing your projects

**Setup**

After cloning the repository, you'll first want to create a directory on your machine that you will add to your PATH so you can run these scripts from anywhere. If you already have a directory for your homemade scripts, you can skip this step.

*Example*

`mkdir $HOME/bin`

Next, you'll add the directory to your machine's PATH.

If you run your bash as a login shell, you can put this in your `.bash_profile`. Otherwise, place this in your `.profile`:

```
if [ -d "$HOME/bin" ] ; then
  PATH="$HOME/bin:$PATH"
fi
```

and then

`source .bash_profile` or `source .profile`

Now you can place the scripts and included directories in your newly created directory. From your local repo:

`rsync -a {config,datefile,projectsort,utils} $HOME/bin/`

If you didn't call your user scripts directory `bin`, make sure you replace it with your directory in the above command.

Give the scripts permission to run:

`chmod 755 datefile projectsort`

And you're all set!

**datefile**

`datefile` is a simple python script that makes a copy of a file and prefixes a date-timestamp to the copy.

Usage is as simple as

`datefile file_to_date`

Output:

```
15:21:18 wheresmyjetpack~ datefile file_to_date
Current Time : 2015-11-05-15-21-21
New Filename :  ./2015-11-05-15-21-21-file_to_date
```

Now you have your original file and a timestamped copy.

*Workflow*

`datefile` is meant to be used in a workflow where one is making edits to the undated file (using it as a working copy), while running `datefile` periodically to retain previous versions of your work. 

**projectsort**

`projectsort` uses files created by `datefile` to organize all of your work. First, you are going to need to tell the config what directory will be your "Projects" directory. This is the directory that `projectsort` will search for timestamped files to organize.

In `config/projectsort_config.py`, set `projects_dir = '/full/path/to/projects'`.

Once that's done, you can run `projectsort` (no arguments) and it wil create a new directory for every corresponding day prefized to a timestamped file. Then it places those timestamped files into that directory.

Output:

```
15:34:35 wheresmyjetpack~/Projects projectsort
[+] Created directory: /Users/wheresmyjetpack/Projects/2015-11-05
[+] Moved 2015-11-05-15-31-49-file_to_date into /Users/wheresmyjetpack/Projects/2015-11-05
[+] Moved 2015-11-05-15-33-35-file_to_date2 into /Users/wheresmyjetpack/Projects/2015-11-05
[+] Moved 2015-11-05-15-33-39-file_to_date3 into /Users/wheresmyjetpack/Projects/2015-11-05
```
