1. Download the repo and store all files in `$HOME`
2. Download prerequisites: tmux, cv2
```
sudo apt-get update
sudo apt-get python3-opencv tmux
```
4. Make all files executable
```
chmod u+x ./archive.sh
chmod u+x ./capture.py
chmod u+x ./tmux.Studio
```
3. Setup `crontab -e`

```
59 23 * * * /home/%USER%/archive.sh
@reboot /home/%USER%/tmux.Studio
```
4. Reboot or Execute the tmux file

```
./tmux.Studio
```
5. On your other PC go to `http://$Server_IP:8000`
