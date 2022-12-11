from tkinter import *
from tkinter.ttk import *
import datetime
import platform

try:
    import winsound

    tp = "windows"
except Exception:
    import os

    tp = "other"

window = Tk()
window.title("Clock")
window.geometry("500x250")
stopwatch_counter_num = 66600
stopwatch_running = False
timer_counter_num = 66600
timer_running = False


def clock():
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split("/")
    hour, minutes, seconds = time2.split(":")
    if int(hour) <= 11 or int(hour) >= 24:
        time = f"{time2} {time3}"
    else:
        time = f"{str(int(hour) - 12)}:{minutes}:{seconds} {time3}"
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)


def alarm():
    main_time = datetime.datetime.now().strftime("%H:%M %p")
    alarm_time = get_alarm_time_entry.get()
    alarm_time1, alarm_time2 = alarm_time.split(" ")
    alarm_hour, alarm_minutes = alarm_time1.split(":")
    main_time1, main_time2 = main_time.split(" ")
    main_hour1, main_minutes = main_time1.split(":")
    main_hour = str(int(main_hour1) - 12) if main_time2 == "PM" else main_hour1
    if (
        int(alarm_hour) == int(main_hour)
        and int(alarm_minutes) == int(main_minutes)
        and main_time2 == alarm_time2
    ):
        for _ in range(3):
            alarm_status_label.config(text="Time Is Up")
            if platform.system() == "Windows":
                winsound.Beep(5000, 1000)  # type: ignore
            elif platform.system() == "Darwin":
                os.system("say Time is Up")
            elif platform.system() == "Linux":
                os.system("beep -f 5000")
        get_alarm_time_entry.config(state="enabled")
        set_alarm_button.config(state="enabled")
        get_alarm_time_entry.delete(0, END)
        alarm_status_label.config(text="")
    else:
        alarm_status_label.config(text="Alarm Has Started")
        get_alarm_time_entry.config(state="disabled")
        set_alarm_button.config(state="disabled")
    alarm_status_label.after(1000, alarm)


def stopwatch_counter(label):
    def count():
        if stopwatch_running:
            global stopwatch_counter_num
            if stopwatch_counter_num == 66600:
                display = "Starting..."
            else:
                tt = datetime.datetime.fromtimestamp(stopwatch_counter_num)
                string = tt.strftime("%H:%M:%S")
                display = string
            label.config(text=display)
            label.after(1000, count)
            stopwatch_counter_num += 1

    count()


def stopwatch(work):
    if work == "start":
        global stopwatch_running
        stopwatch_running = True
        _extracted_from_stopwatch_5("disabled", "enabled", "enabled")
        stopwatch_counter(stopwatch_label)
    elif work == "stop":
        stopwatch_running = False
        _extracted_from_stopwatch_5("enabled", "disabled", "enabled")
    elif work == "reset":
        global stopwatch_counter_num
        stopwatch_running = False
        stopwatch_counter_num = 66600
        stopwatch_label.config(text="Stopwatch")
        _extracted_from_stopwatch_5("enabled", "disabled", "disabled")


# TODO Rename this here and in `stopwatch`
def _extracted_from_stopwatch_5(state, arg1, arg2):
    stopwatch_start.config(state=state)
    stopwatch_stop.config(state=arg1)
    stopwatch_reset.config(state=arg2)


def timer_counter(label):
    def count():
        global timer_running, display
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 66600:
                for i in range(3):
                    display = "Time Is Up"
                    if platform.system() == "Windows":
                        winsound.Beep(5000, 1000)  # type: ignore
                    elif platform.system() == "Darwin":
                        os.system("say Time is Up")
                    elif platform.system() == "Linux":
                        os.system("beep -f 5000")
                timer_running = False
                timer("reset")
            else:
                tt = datetime.datetime.fromtimestamp(timer_counter_num)
                string = tt.strftime("%H:%M:%S")
                display = string
                timer_counter_num -= 1
            label.config(text=display)
            label.after(1000, count)

    count()


def timer(work):
    if work == "start":
        _extracted_from_timer_3()
    elif work == "stop":
        timer_running = False
        _extracted_from_timer_12("enabled", "disabled", "enabled")
    elif work == "reset":
        timer_running = False
        timer_counter_num = 66600
        _extracted_from_timer_12("enabled", "disabled", "disabled")
        timer_get_entry.config(state="enabled")
        timer_label.config(text="Timer")


# TODO Rename this here and in `timer`
def _extracted_from_timer_3():
    global timer_running, timer_counter_num
    timer_running = True
    if timer_counter_num == 66600:
        timer_time_str = timer_get_entry.get()
        hours, minutes, seconds = timer_time_str.split(":")
        minutes = int(minutes) + (int(hours) * 60)
        seconds = int(seconds) + (minutes * 60)
        timer_counter_num = timer_counter_num + seconds
    timer_counter(timer_label)
    _extracted_from_timer_12("disabled", "enabled", "enabled")
    timer_get_entry.delete(0, END)


# TODO Rename this here and in `timer`
def _extracted_from_timer_12(state, arg1, arg2):
    timer_start.config(state=state)
    timer_stop.config(state=arg1)
    timer_reset.config(state=arg2)


tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(stopwatch_tab, text="Stopwatch")
tabs_control.add(timer_tab, text="Timer")
tabs_control.pack(expand=1, fill="both")
time_label = Label(clock_tab, font="calibri 40 bold", foreground="black")
time_label.pack(anchor="center")
date_label = Label(clock_tab, font="calibri 40 bold", foreground="black")
date_label.pack(anchor="s")
get_alarm_time_entry = Entry(alarm_tab, font="calibri 15 bold")
get_alarm_time_entry.pack(anchor="center")
alarm_instructions_label = Label(
    alarm_tab,
    font="calibri 10 bold",
    text="Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes",
)
alarm_instructions_label.pack(anchor="s")
set_alarm_button = Button(alarm_tab, text="Set Alarm", command=alarm)
set_alarm_button.pack(anchor="s")
alarm_status_label = Label(alarm_tab, font="calibri 15 bold")
alarm_status_label.pack(anchor="s")
stopwatch_label = Label(stopwatch_tab, font="calibri 40 bold", text="Stopwatch")
stopwatch_label.pack(anchor="center")
stopwatch_start = Button(
    stopwatch_tab, text="Start", command=lambda: stopwatch("start")
)
stopwatch_start.pack(anchor="center")
stopwatch_stop = Button(
    stopwatch_tab, text="Stop", state="disabled", command=lambda: stopwatch("stop")
)
stopwatch_stop.pack(anchor="center")
stopwatch_reset = Button(
    stopwatch_tab, text="Reset", state="disabled", command=lambda: stopwatch("reset")
)
stopwatch_reset.pack(anchor="center")
timer_get_entry = Entry(timer_tab, font="calibiri 15 bold")
timer_get_entry.pack(anchor="center")
timer_instructions_label = Label(
    timer_tab,
    font="calibri 10 bold",
    text="Enter Timer Time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds",
)
timer_instructions_label.pack(anchor="s")
timer_label = Label(timer_tab, font="calibri 40 bold", text="Timer")
timer_label.pack(anchor="center")
timer_start = Button(timer_tab, text="Start", command=lambda: timer("start"))
timer_start.pack(anchor="center")
timer_stop = Button(
    timer_tab, text="Stop", state="disabled", command=lambda: timer("stop")
)
timer_stop.pack(anchor="center")
timer_reset = Button(
    timer_tab, text="Reset", state="disabled", command=lambda: timer("reset")
)
timer_reset.pack(anchor="center")
clock()
window.mainloop()
