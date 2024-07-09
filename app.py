from flask import Flask, render_template,request


app = Flask(__name__,template_folder="templates")
poll_data = {
'question': 'Яка страва вам більше подобається?',
'fields': ['Піца з в’яленими томатами та куркою', 'Піца солодка','Піца з грушею і блакитним сиром','Піца Біф енд Кріспі','Піца Діабло','Піца з індичкою']
}

@app.route('/review')
def root():
    return render_template('poll.html',data=poll_data)

@app.route('/poll')
def poll():
    vote = request.args.get('field')

    with open("data.txt","w") as out:
        out.write( vote + '\n' )
        out.close()
    
    return render_template('thanks.html', data=poll_data, votes=vote)


if __name__ == "__main__":
    app.run(debug=True)