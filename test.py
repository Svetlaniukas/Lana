from itertools import chain

from flask import render_template

import app


@app.route ('/staff')
def staff(current_staff_shift=None):
    staff_week_day = open ("staff_week_day.txt", 'r')
    staff_weekend = open ("staff.weekend.txt", 'r')

    def items():
        current_staff_shift ={}
        current_staff_shift = dict (chain (staff_week_day.items ( ), staff_weekend.items ( )))

    page_content = render_template ("staff.html",
    current_time_and_date = current_staff_shift,
                                    )

    return page_content


if __name__ == "__main__":
    app.run (debug=True)

