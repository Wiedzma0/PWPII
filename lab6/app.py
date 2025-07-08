from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []
task_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def show_tasks():
    return render_template('tasks.html', tasks=tasks)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add', methods=['POST'])
def add_task():
    global task_id
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'id': task_id, 'text': task_text, 'done': False})
        task_id += 1
    return redirect(url_for('show_tasks'))

@app.route('/done/<int:id>')
def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = True
            break
    return redirect(url_for('show_tasks'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('show_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
