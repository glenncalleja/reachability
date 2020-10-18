Reachability
========================================================================

*This is a work-in-progress package. Any contributions and suggestions, especially for a more Pythonic solution are welcome.*

**Reachability** is a Python 3 package which allows you to monitor and observe online reachability, and react to these status changes as necessary.

This is done by periodically pinging the Cloudflare DNS IP (1.1.1.1). Reachability is customisable, so you can change the interval and host to ping as necessary.

To start with, we can easily check the current status from an instance of the reachability class:

```python
from reachability import Reachability

reachability = Reachability()
print(reachability.isonline())
```

The above show `True` if connected to the internet, or `False` if not.

To set up Reachability, instead you can use:

```python
reachability = Reachability(host='8.8.4.4', port=53, timeout=3, status_check_interval=4)
```

The above will instead ping 8.8.4.4 (Google's DNS Service), on port 53 with a timeout of 3 seconds. status_check_interval is used in more advanced use cases to monitor any status changes as shown below.

# Observing changes
## Functions and Lambdas

```python
reachability.attach_func(lambda x: print(x))
reachability.start_notify()
```

This will print `True` or `False` on each status change. If for example, we are initially connected to the internet, `True` will be printed. If the Internet connection is then interrupted, the lambda will be executed again this time printing `False`.

This will continue until

```
reachability.stop_notify()
```
is called. Note however that the lambda will still be attached. To detach it, we must call

```python
reachability.detach_func(x)
```
where x is a reference to the lambda or function.

Obviously, you can also use something like

```
def f(isonline):
    if isonline:
        print("FunctionA: We are online")
    else:
        print("FunctionA: We are offline")
    
reachability.attach_func(f)
```
## Observers

Another option is to use an Observer Class as demonstrated below:

```python
from reachability import ReachabilityObserver, Reachability


class ObserverA(ReachabilityObserver):
    def reachability_update(self, isonline: bool) -> None:
        if isonline:
            print("ObserverA: We are online")
        else:
            print("ObserverA: We are offline")
    
reachability = Reachability()
observer_a = ObserverA()
reachability.attach(observer_a)
reachability.start_notify()
```

`ReachabiltyObserver` is a simple interface. Classes which use it will implement 
```python
def reachability_update(self, is_online: bool) -> None
```
This method will then be called on Online Reachability changes.

You can have multiple observers attached to a reachability instance. To detach them, simply call 
```python
reachability.attach(observer_a) #Detach ObserverA
reachability.stop_notify() #Stop any further notifications
```



