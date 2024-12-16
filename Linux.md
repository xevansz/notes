[#](#) First things first

### add to /etc/default/grub
GRUB_CMDLINE_LINUX="zswap.enabled=1 rhgb quiet mitigations=off"

/etc/pacman.conf
parallel donwloads = 15

/etc/makepkg.conf
MAKEFLAGS = "-j$(nproc)"

Add Defaults pwfeedback to your sudoers file

xdg-ninja to spring clean

## for power saving
- [ ] auto-cpufreq
- [ ] tlp
- [ ] thermald
- [ ] preload
- [ ] powertop - to check the battery usage

# nvidia
nvidia-open driver
optimus-manager

## useful packages
https://espanso.org/
jitsi - a video conference app
screensy.marijn.it
tmpfiles.org
`0x0` -> `~/bin/0x0`, 0x0.st client (to share public files)
scp
python -m https:(your_server_name) to share your files to all devices in the network


- `yt-dlp`
- `mpv`
- `htop`
- `ncdu`
- `proxychains-ng` to use proxy on app what doesn't actually support it
- `linux-pf` TuxOnIce, -ck patchset etc.
- `weechat` IRC client
- `openssh` must-have
- `socat` Better than `netcat`

Advanced tools:

- `ettercap`, `arpspoof`, `sslstrip`, `nftables` take router over and forward packets through your computer
- `aircrack-ng-svn`, `airdrop-ng-svn` cracks and drops air (if it works)
- `john` crack passwords
- `gcc` `musl` to make C programs, musl is to make them extra-small (statically)
- `busybox` (for http server and temporary cgi)
- ~~`lxc`~~ systemd-nspawn for simple app sandboxing
- `wireshark` and/or `tcpdump` to sniff packets

- [ ] concky, screenlets
      f.lux
      transmission deluge qbittorrent
      nextcloud - check it out
      Mattersmast - do check it
      logseg - obsidian alternative
- [ ] zmfw.sh
- [ ] Timeshift ( to take a backup of the system)
- [ ] sxiv - image viewer
- [ ] ytfzf - youtube
- [ ] motrix.app
      nixos package management nix-config-file


# KDE stuff
https://www.reddit.com/r/unixporn/comments/138ht06/kde_catppuccin_setup_of_my_dreams/
https://www.reddit.com/r/unixporn/comments/uf72ba/kde_kde_plasma_with_polybar/
Konsave: https://github.com/Prayag2/konsave

# android stuff
SeedVault:https://github.com/seedvault-app/seedvault
Jmptfs
mptfs
