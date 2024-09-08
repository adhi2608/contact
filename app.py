from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for contacts
contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    number = request.form['number']
    contacts.append({'name': name, 'number': number})
    return redirect(url_for('index'))

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    print(f"Editing contact with ID: {contact_id}")  # Debug line
    if request.method == 'POST':
        contacts[contact_id]['name'] = request.form['name']
        contacts[contact_id]['number'] = request.form['number']
        return redirect(url_for('index'))
    return render_template('/edit.html', contact=contacts[contact_id], contact_id=contact_id)

@app.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    contacts.pop(contact_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
