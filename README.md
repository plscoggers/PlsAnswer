I had a coworker that would never answer skype, I later learned this was because he never actually had skype turned on.
I created this script to prevent that from happening, but I never wanted to use it.
Then Skype started just randomly crashing and not notifying me that it crashed.
Then this became a necessity.

Don't be like my coworker, leave your messaging tool open so people can communicate.
Don't be like my office, don't use Skype to message each other.

I'm not responsible for any negative side effects, and please don't use maliciously.
This program can be easily modified to run basically any program of known location on the host machine that you wish to have constantly running.

Please only use this to restart processes quickly that you wish to keep running.

Usage

```
python PlsAnswer.py --processes_name process1.exe process2.exe process3.exe --processes_location X:/path/to/process1 X:/path/to/process2 X:/path/to/process3
```

Do not include the actual .exe file in the processes_location
This is an infinite loop so to shut down you'll have to close the terminal running the app