#!/bin/sh

cat << EOF > .git/.commit-message-template
########50 characters############################
Subject
########72 characters##################################################

Problem
# Problem, Task, Reason for Commit

Solution
# Solution or List of Changes

Note
# Special instructions, testing steps, rake, etc

EOF

git config commit.template .git/.commit-message-template
