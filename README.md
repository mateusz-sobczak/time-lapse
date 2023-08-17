1. Download the repo and store all files in `$HOME`
2. Make all files executable
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
4. Execute the tmux file

```
./tmux.Studio
```
5. On your other PC go to `http://$Server_IP:8000`
