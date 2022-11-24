from tkinter import Text

from flask import Flask, render_template
from numpy.core.setup_common import file

app = Flask (__name__)

@app.route ('/staff')
def staff():
    file1 = Text ("staff_week_day.txt", 'r')
    file2 = open ("staff.weekend.txt", 'r')
    file3 = file1+file2
   def staff_shift(file1, file2 ):
       for key, value in nums.items ( ):
           print (key, 'is', value)

    page_content = render_template (
        "staff.html",
      
    )
