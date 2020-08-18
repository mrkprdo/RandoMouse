# RandoMouse ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mrkprdo/RandoMouse) ![GitHub last commit](https://img.shields.io/github/last-commit/mrkprdo/RandoMouse) ![GitHub](https://img.shields.io/github/license/mrkprdo/randomouse) 

## Just make my mouse move randomly.
Author: Mark Prado ![GitHub followers](https://img.shields.io/github/followers/mrkprdo?label=follow%20@mrkprdo&style=social) ![Twitter Follow](https://img.shields.io/twitter/follow/mrkprdo?style=social)

<br>

## Requirements:
- Windows 10
- Python 3.7+
- Pip


## Installation:

`pip install randomouse`
<br>
or
<br>
`git clone https://github.com/mrkprdo/RandoMouse.git`

Then use it as a regular python module.

## Usage:

```python
from randomouse import RandoMouse

rm = RandoMouse()
#Runs the default setup timer=60secs and speed=0.001secs (mouse travel)
rm.start()

#set timer
rm.set_timer(600)

#set speed
rm.set_speed(1)
```

