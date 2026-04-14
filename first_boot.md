[#](#) First things first

## Windows Debloater
https://www.reddit.com/r/OptimizedGaming/comments/su6cq7/windows_1011_optimization_guide/
https://www.revi.cc
https://github.com/Raphire/Win11Debloat
chris titus win util

### add to /etc/default/grub
GRUB_CMDLINE_LINUX="mitigations=off" - do it only if it's slow cause it turns of cpu mitigations which may compromise security

/etc/pacman.conf
parallel donwloads = 15

/etc/makepkg.conf
MAKEFLAGS = "-j$(nproc)"

Add Defaults pwfeedback to your sudoers file

xdg-ninja to spring clean