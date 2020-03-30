#!/usr/bin/python
import psutil

#STATUS_RUNNING
#STATUS_SLEEPING
#STATUS_DISK_SLEEP
#STATUS_STOPPED
#STATUS_TRACING_STOP
#STATUS_ZOMBIE
#STATUS_DEAD
#STATUS_WAKE_KILL
#STATUS_WAKING
#STATUS_PARKED
#STATUS_IDLE
#STATUS_LOCKED
#STATUS_WAITING
#STATUS_SUSPENDED
#STATUS_SUSPENDED
#STATUS_PARKED

pid = 25852
p = psutil.Process(pid)

if (p.status() == psutil.STATUS_RUNNING) :
        print('The Process is running', p.status)
p.suspend()

if p.status() == psutil.STATUS_STOPPED :
    print('The Process is suspended', p.status)

p.resume()
if p.status() == psutil.STATUS_RUNNING:
   print('The Process is resumed', p.status)

p.terminate()
print('The Process is terminated', p.status)

