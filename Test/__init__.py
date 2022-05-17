"""
四大组件：

1. 触发器 triggers: 用于设定触发任务的条件
2. 任务存储器 job stores: 存放任务，可在内存中或数据库中
3. 执行器 executors:   执行任务，可以设定执行模式为单线程或线程池
4. 调度器 schedules:   把上面三个组件作为参数，通过创建调度器实例来实现
"""
import sched
from datetime import date, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# from __future__ import annotations

import logging

from apscheduler.schedulers.sync import Scheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.workers.sync import Worker


def Test1():
    ...
    # def my_job(text):
    #     print(text)
    #
    # sched = BlockingScheduler()
    # sched.add_job(my_job, "date", run_date=datetime(2022, 5, 16, 22, 17, 0), args=["date running"])
    #
    # sched.start()


sched = BlockingScheduler()


@sched.scheduled_job("interval", id="my_job_id", hours=2)
def my_job(text):
    print(text)


sched.start()


if __name__ == '__main__':
    def say_hello():
        print("Hello!")


    logging.basicConfig(level=logging.DEBUG)
    try:
        with Scheduler() as scheduler, Worker(
                scheduler.data_store, portal=scheduler.portal
        ):
            scheduler.add_schedule(say_hello, IntervalTrigger(seconds=1))
            scheduler.wait_until_stopped()
    except (KeyboardInterrupt, SystemExit):
        pass