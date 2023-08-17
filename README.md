Download the repo
Make all files exacutable
`
chmod u+x archive.sh
chmod u+x capture.py
chmod u+x tmux.Studio
`

setup crontab -e
`
59 23 * * * /home/%USER%/archive.sh
`

Execute the tmux file
`
./tmux.Studio
`
