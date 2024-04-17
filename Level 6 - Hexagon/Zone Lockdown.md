#pwn 
# Description
This is an emergency! Your network was infiltrated, and you immediately need to initiate a zone lockdown!

You do have access to the system (user `minion`), and you know the lockdown script.

But damn, one must become the `boss` to execute it!

Notes:

- there are multiple instances running - if yours is broken, switch to another one
- `ssh ch.hackyeaster.com -l minion -p <PORT>` where `<PORT>` is one of: `2411`, `2412`, `2413`, `2414`
- password for **both** `minion` and `boss`: `letmein`
- script to run: `/home/boss/lockdown.sh`
- you'll be kicked off a server if the lockdown is triggered by someone else
- the servers are restarted every hour at x:00

# Solution
Once we connect to the service let's have a look at the lay of the land. There's nothing in minion's home directory except for some bash profile files.
\
![ls -al](../Screenshots/Pasted%20image%2020240417212554.png)

\
Can we just `su boss` to switch user? According to the challenge description the password for both is letmein.
\
![su boss fail](../Screenshots/Pasted%20image%2020240417212813.png)

\
What about information on our current user?
\
![id](../Screenshots/Pasted%20image%2020240417213047.png)

\
So we belong to the root group! Is there anything interesting in `/root/`?
\
![ls -al /root/](../Screenshots/Pasted%20image%2020240417213438.png)

\
Not really. How about files we can write to?  `find / -writable -type d 2>/dev/null`
\
![finding etc group](../Screenshots/Pasted%20image%2020240417213650.png)
\
The /etc/group file is writable, this could be something that can be leveraged to escalate privileges.

Is there any SUID binary? `find / -perm -g=s -o -perm -u=s -type f 2>/dev/null`
And the only one that stands out is `/opt/reset` and it belongs to the user with the id 1001
\
![/opt/reset](../Screenshots/Pasted%20image%2020240417213956.png)
\
Which happens to be the id for boss.
\
![boss = 1001](../Screenshots/Pasted%20image%2020240417214111.png)
\
But running this binary just kicks me out, as it can be seen by running `strings /opt/reset`
\
![strings from reset](../Screenshots/Pasted%20image%2020240417214245.png)
\
So let's go back and explore how adding ourselves to a group can be used to escalate privileges.
Modifying directly the /etc/group file can add a user to a group by appending the name of the user at the end of the line. Like it shows in the current file for the root group. `vi /etc/group`
\
![vi /etc/group](../Screenshots/Pasted%20image%2020240417215458.png)
\
But adding ourselves to the boss group, which doesn't even exist, wouldn't give us access to the boss' home directory, as shown by running `ls -al /home/`
\
![boss directory permissions](../Screenshots/Pasted%20image%2020240417215723.png)
\
So what to do then? Enter the wheel group. According to 
https://www.bevansbench.com/blog/unlocking-secrets-linux-wheel-group-journey-history-modern-day
```
The Wheel Group as a Safety Net

Enter the wheel group. It's like a bouncer for the VIP lounge. Being in the wheel group doesn't automatically grant you all the permissions. Instead, it allows you to use commands like `su` or `sudo` to temporarily escalate your privileges. This way, you have to actively request access, and the system can keep a log of what you're doing. It's a more controlled way to handle those superuser powers.
```
This is a group that was traditionally used to give access to `su` or `sudo`. And since there's no sudo on this machine, then maybe if we belong to the wheel group we'll be able to `su boss` to become the boss!

So we `vi /etc/group` and modify the line belonging to wheel
\
![adding minion to the wheel group](../Screenshots/Pasted%20image%2020240417220708.png)
\
And we exit vi by using `wq!` since it's not possible to write a backup file for vi in our current environment.

Doing `id` doesn't show the wheel group yet, as it's necessary to log out and log back in for the change to take effect. So we exit from the session and create a new one.
\
![id after logout and login](../Screenshots/Pasted%20image%2020240417220918.png)
\
And now we can `su boss` with the letmein password
\
![becoming the boss](../Screenshots/Pasted%20image%2020240417221101.png)
\
And finally run the lockdown.sh script to get the flag `he2024{z0ne_l0ckd0wn_succ3ssfully_tr1gg3r3d}`
\
![running lockdown.sh](../Screenshots/Pasted%20image%2020240417221209.png)
