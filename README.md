# Uno scripting

This here is sort of an example of how one can use an arduino UNO to control something in your computer. Basically, you have a script that sort of listens to a certain port, and trigger a command or other scripts.

I use a Linux machine with some ricing, so is highly probable that you would have to make your own scripts for your own system.

## What I used

- mpd
- mpc
- pamixer
- xbacklight

The important thing is that you make sure you get the debouncing working and that your buttons are actually working correctly, else things can go a bit weird, I had to change a button because it had some flicker problems.