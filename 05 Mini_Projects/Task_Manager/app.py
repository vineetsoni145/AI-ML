from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        option = request.form.get('option')

        if option == 'add':
            return redirect('/add')

        elif option == 'view':
            return redirect('/view')

        elif option == 'delete':
            return redirect('/delete')

        elif option == 'update':
            return redirect('/update')

    return render_template('task.html')


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        taskname = request.form.get('taskname')
        taskdetail = request.form.get('taskdetail')
        taskstatus = request.form.get('taskstatus')

        task = {
            'name': taskname,
            'detail': taskdetail,
            'status': taskstatus
        }

        tasks.append(task)

        print("Task Added :", task)
        print("All Tasks :", tasks)

        return redirect('/add')

    return render_template('add.html')

@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':

        oldname = request.form.get('oldtaskname')

        newname = request.form.get('newtaskname')

        newdetail = request.form.get('newtaskdetail')

        newstatus = request.form.get('newtaskstatus')

        for task in tasks:

            if task['name'] == oldname:

                task['name'] = newname
                task['detail'] = newdetail
                task['status'] = newstatus

                print("Task Updated :", task)

                break

    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():

    if request.method == 'POST':

        taskname = request.form.get('taskname')

        for task in tasks:

            if task['name'] == taskname:

                tasks.remove(task)

                print("Task Deleted :", taskname)
                print("Remaining Tasks :", tasks)

                break

    return render_template('delete.html', tasks=tasks)


@app.route('/view')
def view():

    return render_template('view.html', tasks=tasks)



if __name__ == "__main__":
    app.run(debug=True)