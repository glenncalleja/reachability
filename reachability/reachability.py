from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from .repeat import RepeatedTimer
from typing import Callable
from .onlinecheck import isonline as onlinecheck


class Reachability():
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    def __init__(self, host: str = "1.1.1.1", port: int = 53, timeout: int = 3,
                 status_check_interval: int = 5):
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__repeat_timer = RepeatedTimer(status_check_interval,
                                            self.__check_if_online)

    __host = __port = __timeout = None

    __repeat_timer: RepeatedTimer = None

    __online_state: bool = None

    __class_observers: List[ReachabilityObserver] = []

    __function_observers: Callable[[bool], None] = []

    def __check_if_online(self) -> None:
        """
        Checks if online, and notifies all observers on any changes
        """
        new_state = self.isonline()
        if (new_state != self.__online_state):
            self.__online_state = new_state
            self.__notify()

    def __notify(self) -> None:
        """
        Notify all observers of changes
        """
        for observer in self.__class_observers:
            observer.reachability_update(self.__online_state)

        for function_observer in self.__function_observers:
            function_observer(self.__online_state)

    def start_notify(self) -> None:
        """
        Start the notifications. A message with the current Online Status
        will be sent immediately. A message will also be sent on any
        future status changes.
        """
        self.__repeat_timer.start()
        self.__check_if_online()

    def stop_notify(self) -> None:
        self.__repeat_timer.stop()

    def isonline(self) -> bool:
        return onlinecheck(self.__host, self.__port, self.__timeout)

    def attach(self, observer: ReachabilityObserver) -> None:
        """
        Attach an observer to start receiving Online Status changes
        """
        self.__class_observers.append(observer)

    def detach(self, observer: ReachabilityObserver) -> None:
        """
        Detach an observer to stop receiving Online Status changes
        """
        self.__class_observers.remove(observer)

    def attach_func(self, func: Callable[[bool], None]) -> None:
        """
        Attach a function or lambda to start receiving Online Status changes
        """
        self.__function_observers.append(func)

    def detach_func(self, func: Callable[[bool], None]) -> None:
        """
        Detach a function or lambda to stop receiving Online Status changes
        """
        self.__function_observers.remove(func)

    def detach_all(self):
        """
        Detach all observers, functions or lambda to stop receiving Online
        Status changes
        """
        self.__class_observers.clear()
        self.__function_observers.clear()


class ReachabilityObserver(ABC):
    """
    The Observer interface declares the reachability_update method, used by subjects.
    """

    @abstractmethod
    def reachability_update(self, is_online: bool) -> None:
        """
        Receive Online Status update.
        """
        pass
