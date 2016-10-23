from flask import Flask, request, redirect, url_for
app = Flask(__name__)


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/uploads/police.jpg')
    return "File Uploaded!"

  else:
    page='''
        <html>
          <body>
            <form action="" method="post" name="form" enctype="multipart/form-Data">
              <input type="file" name="datafile"/>
              <input type="submit" name="submit"/>
            </form>
          </body>
        </html>
    '''
    return page, 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
