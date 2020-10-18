from reachability import ReachabilityObserver, Reachability


class ObserverA(ReachabilityObserver):
    def reachability_update(self, isonline: bool) -> None:
        if isonline:
            print("ObserverA: We are online")
        else:
            print("ObserverA: We are offline")


class ObserverB(ReachabilityObserver):
    def reachability_update(self, isonline: bool) -> None:
        if isonline:
            print("ObserverB: We are online")
        else:
            print("ObserverB: We are offline")


if __name__ == "__main__":
    # The client code.

    reachability = Reachability()
    observer_a = ObserverA()
    reachability.attach(observer_a)
    observer_b = ObserverB()
    reachability.attach(observer_b)

    def f(isonline):
        if isonline:
            print("FunctionA: We are online")
        else:
            print("FunctionA: We are offline")

    reachability.attach_func(f)
    reachability.start_notify()
