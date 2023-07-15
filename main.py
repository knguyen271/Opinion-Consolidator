import youtube_comments as youtube
import text_preprocess as textPrep
import data_analysis as dataAnal
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import sys

def run_program():
    topic = input.get()
    if(topic == ""):
        print('') 
    else:
        instruct.config(text='Looking for: ' + topic)
        instruct2.config(text='Do Not Close')
        instruct2.pack()
        estimate.config(text='Estimated Time : 1 min')
        estimate.pack()
        window.update()
        input.place_forget()
        submit_button.place_forget()
        progress_bar.place(x=175, y=675)
        start_loading()
        window.update()
        get_results(topic)
                
def run_gui():
    window.title("Opinion Consolidator")
    window.geometry('1000x750')
    window.resizable(False, False)
    
    input.config(font=('Helvetica bold', 16))
    input.place(x=210, y=675)

    submit_button.config(font=('Helvetica bold', 14))
    submit_button.place(x=670, y= 669)

    instruct.config(font=('Helvetica bold', 32))
    instruct.pack()

    instruct2.config(font=('Helvetica bold', 26))    
    estimate.config(font=('Helvetica bold', 16))
    average.config(font=('Helvetica bold', 16))
    vibe.config(font=('Helvetica bold', 26))
    num_of_comments.config(font=('Helvetica bold', 16))
    back_button.config(font=('Helvetica bold', 10))

    window.mainloop()

def reset_gui():
    back_button.place_forget()
    for widget in window.winfo_children():
        widget.pack_forget()
    
    instruct.config(text='Type The Topic In The Box Below')
    instruct.pack()
    input.place(x=210, y=675)
    submit_button.place(x=670, y= 669)

def get_results(topic):
    estimate.pack_forget()
    instruct2.pack_forget()
    links = youtube.get_links(topic)
    thread = threading.Thread(target=youtube.get_comments(links))
    thread.start()
    print(threading.active_count())
    comments = youtube.return_comments()
    cleaned_comments = []
    for comment in comments:
        cleaned = textPrep.clean_text(comment)
        cleaned_comments.append(cleaned)

    comments = cleaned_comments
    polarity = []
    for comment in comments:
        polarity.append(dataAnal.getPolarity(comment))
    
    progress_bar.place_forget()

    average_polarity = dataAnal.get_average(polarity)
    back_button.place(x=10, y= 10)
    instruct.config(text='Results: ' + topic)
    if(average_polarity > 0.6):
        vibe.config(text='Overall Opinion is Extremely Positive')
    elif(average_polarity > 0):
        vibe.config(text='Overall Opinion is Positive')
    elif(average_polarity == 0):
        vibe.config(text='Overall Opinion is Neutral')
    elif(average_polarity > -0.6):
        vibe.config(text='Overall Opinion is Negative')
    else:
        vibe.config(text='Overall Opinion is Extremely Negative')
    vibe.pack()
    average.config(text='Average Polarity Score: ' + str(average_polarity))
    average.pack()
    num_of_comments.config(text='Number of Comments ' + str(len(comments)))
    num_of_comments.pack()

    window.protocol("WM_DELETE_WINDOW", exit_program)
    get_bar_chart(polarity)
    dataAnal.get_frequency(comments)

def get_bar_chart(values):
    fig = Figure(figsize=(6, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(values, bins=40, edgecolor='black')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Polarity Of Comments')
    bar_chart = FigureCanvasTkAgg(fig, master=window)
    bar_chart.draw()
    bar_chart.get_tk_widget().pack()

   
def exit_program():
    sys.exit()    

def start_loading():
    progress_bar['value'] = 0
    increment_loading()

def increment_loading():
    value = progress_bar['value']
    if value < 100:
        progress_bar['value'] += 1
        window.after(100, increment_loading)

window = tk.Tk()
input = tk.Entry(window, width='40')
instruct = tk.Label(window, text='Type The Topic In The Box Below')
instruct2 = tk.Label(window, text='')
estimate = tk.Label(window, text='')
average = tk.Label(window, text='')
vibe = tk.Label(window, text='')
num_of_comments = tk.Label(window, text='')
progress_bar = ttk.Progressbar(window, orient='horizontal', length=600, mode='determinate')
submit_button = tk.Button(window, text="Find Opinions", command=run_program)
back_button = tk.Button(window, text='Back', command=reset_gui)
thread1 = threading.Thread(target=run_gui())
thread1.start()