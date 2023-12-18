
# hell with you nvidia


#setup
- Window Manager 
	-  Hyprland
- shell
	- Ohmyzsh with starship
- Terminal
	- Foot(rec @bugswriter) // Alacritty (default)
- Panel
	- Waybar
- Notify Daemon
	- Dunst
- Launcher
	- Rofi
- File Manager
	- lf + nautilus ( shit its not working), thunar maybe or hifile we will see

#dots
Nope.. just started using so....
This looks nice... https://github.com/linuxmobile/hyprland-dots
changed keybinds

#base-packages
wayland ( says its preinstalled ... )
xorg-xwayland for running x applications
xorg-xlsclients ( to check which apps are using x server)
qt5-wayland qt6-wayland glfw-wayland (provides support for ... don't care)

found some problems in firefox....
k solved ._. ( https://www.fosskers.ca/en/blog/wayland )

paru -S hpyland-git(aur) hyprpicker-git alacritty(opacity 0.8) waybar-git rofi dunst nwg-look wf-recorder wlogout wlsunset

#dependencies
paru -S colord ffmpegthumbnailer gnome-keyring grimblast-git gtk-engine-murrine \
imagemagick kvantum pamixer playerctl polkit-kde-agent qt5-quickcontrols        \
qt5-quickcontrols2 swww ttf-font-awesome tumbler     \
ttf-jetbrains-mono ttf-icomoon-feather xdg-desktop-portal-hyprland-git xdotool  \
xwaylandvideobridge-cursor-mode-2-git cliphist qt5-imageformats qt5ct

#cool_packages/apps
image2sixel : https://www.youtube.com/watch?v=E_hDQoPbd0k