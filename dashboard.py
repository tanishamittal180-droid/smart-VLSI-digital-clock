import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time

from backend import clock
from ai_engine import predict_alarm
import streamlit.components.v1 as components

#################################################
# PAGE SETTINGS
#################################################

st.set_page_config(
    page_title="AI Smart VLSI Clock",
    layout="wide"
)


#################################################
# UPDATE REAL TIME CLOCK
#################################################

clock.update()


#################################################
# TITLE
#################################################

st.title("⏰ AI Smart VLSI Digital Clock Dashboard")


#################################################
# SIDEBAR SETTINGS
#################################################

st.sidebar.title("Settings")

mode=st.sidebar.selectbox(
"Time Mode",
[
"24 Hour",
"12 Hour"
]
)


#################################################
# ALARM SETTINGS
#################################################

st.sidebar.subheader("Alarm Settings")

alarm_hour=st.sidebar.number_input(
"Alarm Hour",
min_value=0,
max_value=23,
value=clock.alarm_hour
)

alarm_min=st.sidebar.number_input(
"Alarm Minute",
min_value=0,
max_value=59,
value=clock.alarm_min
)

clock.alarm_hour=alarm_hour
clock.alarm_min=alarm_min

clock.alarm_enabled=st.sidebar.toggle(
"Enable Alarm",
value=True
)


#################################################
# STOPWATCH
#################################################

stopwatch_enable=st.sidebar.toggle(
"Enable Stopwatch",
True
)

if stopwatch_enable:
    clock.stopwatch+=1


#################################################
# TIME FORMAT
#################################################

display_hour=clock.hour

if mode=="12 Hour":

    if display_hour>12:
        display_hour-=12

    elif display_hour==0:
        display_hour=12


#################################################
# TOP CARDS
#################################################

col1,col2,col3,col4=st.columns(4)

with col1:

    st.metric(

        "Current Time",

        f"{display_hour:02}:{clock.minute:02}:{clock.second:02}"

    )


with col2:

    st.metric(

        "Date",

        f"{clock.day:02}/{clock.month:02}"

    )


with col3:

    st.metric(

        "Stopwatch",

        f"{clock.stopwatch}"

    )


with col4:

    ampm="AM"

    if clock.hour>=12:
        ampm="PM"

    st.metric(

        "AM/PM",

        ampm

    )


#################################################
# CURRENT ALARM
#################################################

st.divider()

st.subheader("Current Alarm")

st.info(

f"Alarm Time : {clock.alarm_hour:02}:{clock.alarm_min:02}"

)


#################################################
# ALARM STATUS
#################################################

st.divider()

st.subheader("Alarm Status")


if clock.alarm:

    st.error(

        "🚨 ALARM RINGING"

    )

    st.balloons()

else:

    st.success(

        "🟢 Alarm Waiting"

    )


#################################################
# SMART COMMAND INPUT
#################################################

st.divider()

st.subheader("Smart Command")

command=st.text_input(

"Enter command",

placeholder="Set alarm at 6:45"

)


if command:

    cmd=command.lower()

    if "alarm" in cmd:

        try:

            t=cmd.split("at")[1]

            hr,minu=t.split(":")

            clock.alarm_hour=int(hr)

            clock.alarm_min=int(minu)

            st.success(

                f"Alarm updated → {hr}:{minu}"

            )

        except:

            st.error(

                "Use format: Set alarm at 6:45"

            )


#################################################
#################################################
# ALARM STATUS + SOUND
#################################################

st.divider()

st.subheader("Alarm Status")

if clock.alarm:

    st.error(
        "🚨 ALARM RINGING 🚨"
    )

    st.balloons()

    alarm_html = """
    <audio autoplay loop>
        <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg"
        type="audio/ogg">
    </audio>
    """

    st.components.v1.html(
        alarm_html,
        height=0
    )

else:

    st.success(
        "🟢 Alarm Waiting"
    )


#################################################
# ANALYTICS GRAPH
#################################################

st.divider()

st.subheader("Wakeup Analytics")


days=[

"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat",
"Sun"

]

hours=[

6,
7,
6,
8,
7,
8,
9

]


df=pd.DataFrame({

"Day":days,
"Wakeup":hours

})


fig=plt.figure()

plt.plot(

df["Day"],
df["Wakeup"]

)

plt.xlabel("Days")

plt.ylabel("Wakeup Time")

st.pyplot(fig)


#################################################
# SYSTEM STATUS
#################################################

st.divider()

st.subheader("Simulation Status")


status={

"Hour":clock.hour,
"Minute":clock.minute,
"Second":clock.second,

"Alarm Hour":clock.alarm_hour,
"Alarm Minute":clock.alarm_min,

"Alarm Enabled":clock.alarm_enabled,

"Alarm Active":clock.alarm,

"Stopwatch":clock.stopwatch

}

st.json(status)


#################################################
# RAW LOGS
#################################################

st.divider()

st.subheader("System Logs")


st.code(

f"""

Clock Time:

{clock.hour}:{clock.minute}:{clock.second}

Date:

{clock.day}/{clock.month}

Alarm:

{clock.alarm_hour}:{clock.alarm_min}

Alarm Enabled:

{clock.alarm_enabled}

Stopwatch:

{clock.stopwatch}

"""

)


#################################################
# AUTO REFRESH
#################################################

time.sleep(1)

st.rerun()