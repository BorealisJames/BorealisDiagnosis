import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os 

def generate_mavros_logs():

    localpose_filename = "localpose_log.csv"
    setpoint_filename = "setpoint_log.csv"
    assigned_filename = "assignedpose_log.csv"

    whereami = 'MavrosLogs/'
    out = os.scandir(whereami)
    dirs_dct = {}
    for entry in out:
        if entry.is_dir():
            dirs_dct[os.path.getctime(entry)] = entry.name # sorting by key is easier (?) than sorting by values
    
    sorted_dirs_dct = sorted(dirs_dct.items(), key=lambda x: x[1], reverse=True)
    newest_directory = sorted_dirs_dct[0][1] + "/"
    print(newest_directory)
    print("Mavroslogs Newest_directory is " + newest_directory)

    report_directory = "Report/"
    new_directory = report_directory + newest_directory

    try:
        os.mkdir(new_directory)
    except Exception as e:
        print(e) # directory already exist ?

    localpose_df = pd.read_csv(whereami + newest_directory + localpose_filename, sep= ",")
    setpoint_df = pd.read_csv(whereami + newest_directory + setpoint_filename, sep= ",")
    assigned_df = pd.read_csv(whereami + newest_directory + assigned_filename, sep= ",")

    figure, (axis, axis2, axis3) = plt.subplots(3,1)
    figure.suptitle('Setpoint vs localpose graph')
    x_localpose_column = localpose_df.iloc[:,0]
    y_localpose_column = localpose_df.iloc[:,1]
    z_localpose_column = localpose_df.iloc[:,2]
    time_localpose_column = localpose_df.iloc[:,3]
    localpose_date_time_in_pandas = pd.to_datetime(time_localpose_column)

    x_setpointpose_column = setpoint_df.iloc[:,0]
    y_setpointpose_column = setpoint_df.iloc[:,1]
    z_setpointpose_column = setpoint_df.iloc[:,2]
    time_setpointpose_column = setpoint_df.iloc[:,3]
    setpoint_date_time_in_pandas = pd.to_datetime(time_setpointpose_column)

    x_assignedpose_column = assigned_df.iloc[:,0]
    y_assignedpose_column = assigned_df.iloc[:,1]
    z_assignedpose_column = assigned_df.iloc[:,2]
    time_assignedpose_column = assigned_df.iloc[:,3]
    assignedpose_date_time_in_pandas = pd.to_datetime(time_assignedpose_column)

    axis.plot(localpose_date_time_in_pandas, x_localpose_column)
    axis.plot(setpoint_date_time_in_pandas, x_setpointpose_column)
    axis.plot(assignedpose_date_time_in_pandas, x_assignedpose_column)

    axis.set_title('X localpose vs setpointpose vs assinged pose')
    axis.legend(["local pose", "setpoint pose", "assigned pose"])
    axis.set_ylabel("Position (m)")
    axis.set_xlabel("Time (24h)")

    axis2.plot(localpose_date_time_in_pandas, y_localpose_column)
    axis2.plot(setpoint_date_time_in_pandas, y_setpointpose_column)
    axis2.plot(assignedpose_date_time_in_pandas, y_assignedpose_column)
    axis2.set_title('Y localpose vs setpointpose vs assinged pose')
    axis2.legend(["local pose", "setpoint pose", "assigned pose"])
    axis2.set_ylabel("Position (m)")
    axis2.set_xlabel("Time (24h)")

    axis3.plot(localpose_date_time_in_pandas, z_localpose_column)
    axis3.plot(setpoint_date_time_in_pandas, z_setpointpose_column)
    axis3.plot(assignedpose_date_time_in_pandas, z_assignedpose_column)
    axis3.set_title('Z localpose vs setpointpose vs assinged pose')
    axis3.legend(["local pose", "setpoint pose", "assigned pose"])
    axis3.set_ylabel("Position (m)")
    axis3.set_xlabel("Time (24h)")

    # Wtf no pixel format?
    figure.set_size_inches(10,15)
    figure.savefig(new_directory + 'mavros_local_vs_setpoint_vs_assigned.png', dpi = 200)
    return plt, newest_directory

if __name__ == "__main__":
    plt_handler, direct = generate_mavros_logs()
    plt_handler.show()