# Contributing to Genropy Projects

We'd love for you to contribute to our source code and to make our projects even 
better than they are today! Here are the guidelines we'd like you to follow:

 - [Code of Conduct](#coc)
 - [Questions or Problems](#question)
 - [Issues and Bugs](#issue)
 - [Feature Requests](#feature)
 - [Submission Guidelines](#submit)
 - [Coding Rules](#rules)
 - [Commit Message Guidelines](#commit)
 - [Signing the CLA](#cla)

## <a name="coc"></a> Code of Conduct

As contributors and maintainers of Genropy projects, we pledge to respect everyone 
who contributes by posting issues, updating documentation, submitting pull requests, 
providing feedback in comments, and any other activities.

Communication through any Genropy channels (GitHub, Gitter, mailing lists, Google+, 
Twitter, etc.) must be constructive and never resort to personal attacks, trolling, 
public or private harassment, insults, or other unprofessional conduct.

We promise to extend courtesy and respect to everyone involved in this project 
regardless of gender, gender identity, sexual orientation, disability, age, race, 
ethnicity, religion, or level of experience. We expect anyone contributing to Genropy
projects to do the same.

If any member of the community violates this code of conduct, the maintainers of the 
Genropy projects may take action, removing issues, comments, and PRs or blocking accounts 
as deemed appropriate.

If you are subject to or witness unacceptable behavior, or have any other concerns, please 
email us at info@genropy.org.

## <a name="question"></a> Got a Question or Problem?

If you have questions about how to use any Genropy project library, please direct these to 
the appropriate channels.

## <a name="issue"></a> Found an Issue?
If you find a bug in the source code or a mistake in the documentation, you can help us by
submitting an issue to the appropriate GitHub Repository. Even better you can submit a 
Pull Request with a fix.

**Please see the Submission Guidelines below**.

## <a name="feature"></a> Want a Feature?
You can request a new feature by submitting an issue to the appropriate GitHub Repository.  
If you would like to implement a new feature then consider what kind of change it is:

* **Major Changes** that you wish to contribute to the project should be discussed first in 
our chnnels so that we can better coordinate our efforts, prevent duplication of work, and 
help you to craft the change so that it is successfully accepted into the project.
* **Small Changes** can be crafted and submitted to the GitHub Repository as a Pull Request.

## <a name="submit"></a> Submission Guidelines

### Submitting an Issue

Before you submit your issue, search the archive. It may be that it was already addressed. 
If your issue appears to be a bug, and hasn't been reported, open a new issue. Help us to 
maximize the effort we can spend fixing issues and adding new features, by not reporting 
duplicate issues. Providing the following information will increase the chances of your issue 
being dealt with quickly:

* **Overview of the Issue** - If an error is being thrown, a non-minified stack trace helps.
* **Motivation or Use Case** - Explain why this is a bug for you.
* **Library Name and Version(s)** - Please indicate if it is a regression bug.
* **Operating System** - Is this a problem with all platforms or only yours?
* **Reproduce the Error** - If possible, provide a live example. Minimally, please provide an 
unambiguous set of steps to reproduce the issue.
* **Related Issues** - Has a similar issue been reported before?
* **Suggest a Fix** - If you can't fix the bug yourself, perhaps you can point to what might 
be causing the problem (line of code or commit).

### Submitting a Pull Request
Before you submit your pull request consider the following guidelines:

* Search the appropriate GitHub Repository for an open or closed Pull Request that relates to your 
submission. You don't want to duplicate effort.
* Please sign our [Contributor License Agreement (CLA)](#cla) before sending Pull Requests. We cannot 
accept code without this.
* Make your changes in a new git branch:

	```shell
	git checkout -b my-fix-branch master
	```

* Create your patch, **including appropriate test cases**.
* Follow our [Coding Rules](#rules).
* Run the full test suite and ensure that all tests pass.
* Commit your changes using a descriptive commit message that follows our
  [commit message conventions](#commit).
  
	```shell
	git commit -a
	```

	> Note: The optional commit `-a` command line option will automatically "add" and "rm" edited files.

* Build your changes locally to ensure all the tests pass

	```shell
	karma start
	```

* Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```

* In GitHub, send a Pull Request to the master branch.
* If we suggest changes then:
	* Make the required updates.
  	* Re-run the test suite to ensure tests are still passing.
  	* Rebase your branch and force push to your GitHub Repository (this will update your Pull Request):

    ```shell
    git rebase master -i
    git push -f
    ```

### After Your Pull Request is Merged

After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:

* Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

    ```shell
    git push origin --delete my-fix-branch
    ```

* Check out the master branch:

    ```shell
    git checkout master -f
    ```

* Delete the local branch:

    ```shell
    git branch -D my-fix-branch
    ```

* Update your master with the latest upstream version:

    ```shell
    git pull --ff upstream master
    ```

## <a name="rules"></a> Coding Rules
To ensure consistency throughout the source code, keep these rules in mind as you are working:

* All features or bug fixes **must be tested** by one or more specs.
* All public API methods **must be documented**. To see how we document our APIs, please check 
out the existing docs.
* Instead of complex inheritance hierarchies, we **prefer simple objects**.

## <a name="commit"></a> Git Commit Guidelines

We have very precise rules over how our git commit messages can be formatted.  This leads to **more
readable messages** that are easy to follow when looking through the **project history**.

### Commit Message Format
Each commit message consists of a **header** or title, a **body** and an optional **footer**.

Good commit messages serve at least three important purposes:

* To speed up the reviewing process.

* To help us write a good release note.

* To help the future maintainers of the project (it could be you!), say five years into the future, 
to find out why a particular change was made to the code or why a specific feature was added.

Structure your commit message like this:

From: [[http://git-scm.com/book/ch5-2.html]]

> ```
> Short (50 chars or less) summary of changes
> 
> More detailed explanatory text, if necessary.  Wrap it to about 72
> characters or so.  In some contexts, the first line is treated as the
> subject of an email and the rest of the text as the body.  The blank
> line separating the summary from the body is critical (unless you omit
> the body entirely); tools like rebase can get confused if you run the
> two together.
> 
> Further paragraphs come after blank lines.
> 
>   - Bullet points are okay, too
> 
>   - Typically a hyphen or asterisk is used for the bullet, preceded by a
>     single space, with blank lines in between, but conventions vary here
>
> If applicable, add a footer with Breaking Changes or GitHub issues that 
> this commit Closes.
> ```

#### DO
* Write the summary line and description of what you have done in the imperative mode, 
that is as if you were commanding someone. Start the line with "Fix", "Add", "Change" 
instead of "Fixed", "Added", "Changed".
* Always leave the second line blank.
* Line break the commit message description (to make the commit message readable without having 
to scroll horizontally in `gitk`).
* Add a footer line (after a blank line) with informations about **Breaking Changes**, 
and is also the place to reference GitHub issues that this commit **Closes**.

#### DON'T
* Don't end the summary line with a period - it's a title and titles don't end with a period.

#### TIPS
* If it seems difficult to summarize what your commit does, it may be because it includes several 
logical changes or bug fixes, and are better split up into several commits using `git add -p`.

#### REFERENCES
The following blog post has a nice discussion of commit messages:

"On commit messages":http://who-t.blogspot.com/2009/12/on-commit-messages.html

## <a name="cla"></a> Signing the CLA

Please sign our Contributor License Agreement (CLA) before sending pull requests. For any code changes 
to be accepted, the CLA must be signed. It's a quick process, we promise! You can sign the CLA 
[here]().

> Note: This document is based on the Aurelia and AngularJS Contributor docs.
