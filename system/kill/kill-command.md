## killall
The killall command takes the following form:
```bash
killall [process name]
```
Replace [process name] with the name of any process that you wish to terminate. killall will terminate all programs that match the name specified. By default, killall sends SIGTERM (15) which terminates running process that match the name specified. You may specify a different signal using the -s option as follows:
```bash
killall -s 9 [process name]
```
This sends SIGKILL signal which is more at killing some particularly unruly processes.

## kill
The kill command terminates individual processes as specified by their process ID numbers or “PIDs.” Commands take the following form:
```bash
kill [PID]
```
This sends SIGTERM to the PID specified. You may specify multiple PIDs on the command line to terminate processes with kill. You may also send alternate system signals with kill. The following examples all send the SIGKILL signal to the PID specified:
```bash
kill -s KILL [PID]
kill -KILL [PID]
```

Issue one of the following commands to get a list of all of the available signals:
```bash
kill -l
killall -l
```