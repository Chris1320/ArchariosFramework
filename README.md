# Archários Framework v0.0.2.3 :: The Novice's Ethical Hacking Framework
## Copyright (C) 2018, 2019 :: Catayao56 <Catayao56@gmail.com>
[Archarios Framework](https://github.com/Catayao56/ArchariosFramework.git) is an Ethical Hacking Framework.
It was created on Wednesday, June 27, 2018.
It provides tools that you need for
reconnaissance, scanning, exploitation,
encryption, password cracking, and more!
Archarios Framework is maintained by Catayao56,
and is the child of the old toolkit and framework,
Shadow Suite Toolkit.

## What's new?
+ Archarios Framework now supports Windows Operating Systems!
+ File Integrity Test
+ Transitioning to new `config_handler` module.
+ `module info`, `module test`, and `module reload` commands now test all modules if `*` is supplied.
+ MODULE UPDATE: Updated sample module description.
+ FIX: userlevel error when running as root/administrator.
+ FIX: Added `shell=True` argument on subprocess calls.

+ ATTENTION: Contributors needed!
     * I can't do this without contributors or even testers,
       please help me!
          + Co-Developers
    	  + Testers (Windows and Linux systems)

## Full Feature List
+ Open Source
     * Archários is protected by the GNU General Public License, means
       that you can freely download, modify, and distribute the software.
       Just give "creds" to us and the developers that made the awesome
       tools.

+ Create Custom Modules from template
     * Do you know Python? Do you know how to code in Python? Do you want
       to create your own module that can penetration test a Class A network
       in just three seconds? (exagerrated) Archários Framework provides
       a module template to help you start creating your custom module. It also
       provides an Application Programming Interface (API) to help you on
       the integration of Archários Framework and your custom module.

+ Pre-installed modules
     * It's okay if you don't know how to program. Archários Framework has an
       arsenal! It provides you tools written in different languages. Python,
       Ruby, Perl, PHP, and many more!

+ Services
     * Its too bad if you need to open multiple instances of Archários Framework
       just to do other tasks... So services just've come! Start those services
       such as servers, background hash crackers, and many more!

+ Secrets
     * We know this is not really necessary, But its fun to look at the code to
       see Archários Framework secrets!

## License and Copying

+ This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

+ See LICENSE file.

## Credits

* Development Team
    + Project Lead: Catayao56

* Others
    + Offensive Security: Kali Linux, exploit-db, and Kali NetHunter
    + Termux Development Team: Termux Android Emulator

## Requirements
+ Tested Operating Systems are Kali, Mint, Ubuntu, and Termux Terminal Emulator for Android.
	
+ Not yet tested for Windows Operating Systems...

+ Internet Connection. (for performing remote attacks and/or updating)
+ Python Interpreter version 3.
+ Dependencies
	* Dependencies can be installed automatically in the program. (Needs Internet Connection)
	* To manually install, type "sudo python3 core/update.py" and "bash instdeps.bash".


## Installing & Running
------------------------
1.Installing and Running
      - [LINUX] Enter these commands in your terminal:

      $ sudo apt update && apt upgrade -y [1]
      $ sudo apt install python3 git [2]
      $ git clone https://gitlab.com/Catayao56/ArchariosFramework.git [3]
      $ cd ArchariosFramework/src && chmod 755 ArchariosFramework.py [4]
      $ ./ArchariosFramework.py [5]
      [Archários] $ full update [6]
      [Archários] $ help [7]

      [1] Update repository package list/s.
      [2] Install Python interpreter and Git client.
      [3] Clone Archários Framework from Catayao56's Gitlab repository.
      [4] Changes directory to ArchariosFramework/src and changes file mode to executable.
      [5] Run 'ArchariosFramework.py'.
      [6] Type 'full update' on Archários's console to update
          the program and dependencies.
      [7] Type 'help' on Archários's console to see the help menu.

2.Questions? Feature requests? Bugs?
      
      -Just contact us and we'll respond as soon as possible. You can also create a merge request on https://gitlab.com/Catayao56/ArchariosFramework.git
