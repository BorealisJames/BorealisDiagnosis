from flask import Flask, send_file, request, render_template
from helper_funcs import format_scandir_output
from plot_logs import generate_logs
from plot_mavros_logs import generate_mavros_logs
from plot_node_stats import generate_node_logs
import os

app = Flask(__name__, static_folder="templates") # default is a folder named "static" but I changed it templates cause its a small project

@app.route("/")
def index():
    return render_template("index.html", latest_logs="Not Yet Generated", latest_mavros_logs="Not Yet Generated")

# dynamic url routing
@app.route('/<path:directory_path>')
def path_dir(directory_path):
    print(directory_path)
    try:
        scandir_out = os.scandir(directory_path)
        _dir_list, _file_list = format_scandir_output(scandir_out)
        return render_template("show_files_dir.html", file_list=_file_list, dir_list=_dir_list, latest_logs="Not Yet Generated", latest_mavros_logs="Not Yet Generated")
    except: # if scandir fails that means path given is a file
        print("Sending file")
        return send_file(directory_path)

@app.route("/run_mavors_script/", methods=['POST'])
def route_generate_mavros_logs():
    print("Running the mavros script ...")
    mavros_plt_handler, mavroslogs_latest_directory = generate_mavros_logs()

    # Not used
    mavros_plt_handler.close()
    return render_template('index.html', latest_mavros_logs=mavroslogs_latest_directory)

@app.route("/run_logs_script/", methods=['POST'])
def route_generate_logs_logs():
    print("Running the logs script ...")
    logs_plt_hander, logs_latest_directory = generate_logs()

    # Not used
    logs_plt_hander.close()
    return render_template('index.html', latest_logs= logs_latest_directory)
