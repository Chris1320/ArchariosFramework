# README for Developers

## How the code is structured?

+ The program is now ported to Python 3. The program has been
  broken down into little pieces called 'modules'. The API
  provides methods to integrate with Archários Framework.

## Comment Tags

+ Comment tags are used to easily understand
  the logic of a program. The comment tags
  labels the code if it has errors, needs to
  be frequently updated, where you left off,
  and more.

+ Comment tags definitions and examples
      * DEV0001 : Requires Attention Tag
      * DEV0002 : Frequently Update Tag
      * DEV0003 : Where You Left Your Code (WYLYC) Tag
      * DEV0004 : Under Construction Tag
      * DEV0005 : Mentioned line is for debugging purposes.
                  Comment the mentioned line if not debugging.
      * DEV0006 : Feature request Tag

## Program Development Cycle

+ Archários Framework uses the 'Scrum Development Cycle'.

## New framework module (For Framework Contributors):
+ If you want to contribute and wanted to create a new extension for the
  framework (like misc.py module), you need to follow these guidelines:

      * `Try` to follow the PEP 0008 Guideline.
      * Use meaningful function and variable names.
      * Use the logger.py module to log information.
      * All modules must use the module template provided by Archarios Framework.

