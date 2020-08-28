# CONTRIBUTING TO THIS PROJECT

Only members of TEAM-085 of the Andela/Facebook Build for SDG Cohort 2 are allowed to make contributions to this project, for any contributors outside this team, go [here](#external-contributors) to see steps on contributing.

This document will be regularly updated as the need arises, so it is important to always pull for updates.

⚠️ **Important** ⚠️<br>
-   See the [README](README.md) to setup your environment first.
-   If you install any new dependencies, ensure you run
    ```
    pip freeze > requirements.txt
    ```
    to add the new dependencies to the requirements.txt file.

## Issues

The development progress will be tracked using issues. Issues will be created whenever a new feature needs to be added, a bug needs to be fixed, or any change needs to be made to the code, dependencies or documentation. Before opening a new issue, always check to confirm there are no open issues addressing it already.

## How to Contribute

-   [ ] To contribute, firstly fork this repository.
-   **Ensure you state on the slack channel exactly what you're working on at the moment so that multiple people don't work on the same feature or fix simultaenously.**
-   Ensure that you're working on a feature or fix within an issue that has been assigned to you.
-   **If you wish to work on a new feature, or fix a bug that you noticed outside your immediate task, indicate on the slack group first to ensure no one else is working on it and ensure you create an issue for it or ask to be assigned to the current issue.**
-   [ ] Write your code on the `dev` branch of your forked repository.
-   [ ] When you're done, create a pull request from your `dev` branch to the `dev` branch of the [Upstream Frontend Repository](https://github.com/BuildForSDGCohort2/Team-085-Backend/tree/dev)

## Contribution to Production
-   [ ] Successful additions are pushed to the [staging branch](https://github.com/BuildForSDGCohort2/Team-085-Backend/tree/staging) for further review and testing.
-   [ ] If any bugs or discrepancies are encounter on the `staging` branch, a issue will be created with the `bug` label and assigned to a developer to fix.
-   [ ] When the `staging` branch is at a state that is production ready, it will then be pushed to the `develop` branch for final review.

## Important Notes

-   All commits within each pull request are treated as one, therefore if ther is an error with one commit, the entire push will be rejected. It is advised that pull requests are opened based on a single feature or function, and they should contain as few lines of code or commits as is necessary. Avoid trying to do too much at once.

## Code Style
It is extremely important that everyone follows the same code style. We'll be using the [Udacity](udacity.com) style guide for this project, because it is concise and easy to follow.

-   All Indentations must be 4 spaces long, that is `  `.
-   The [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) is the code style of choice.
-   [Code Style Guide4 for Git](https://udacity.github.io/git-styleguide/)

## External Contributors
