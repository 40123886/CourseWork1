from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/artists/')
def index():
  return render_template('index.html')

@app.route('/albums/')
def albums():
  return render_template('albums.html')

@app.route('/singles/')
def singles():
  return render_template('singles.html')

@app.route('/artists/biffy_clyro/')
def artist():
  return render_template('biffy.html')

@app.route('/artists/biffy_clyro/puzzle')
def puzzle():
  return render_template('puzzle.html')

@app.route('/artists/biffy_clyro/blackened_sky')
def blacksky():
  return render_template('blacksky.html')

@app.route('/artists/biffy_clyro/puzzle/folding_stars')
def stars():
  return render_template('folding.html')

@app.route('/artists/biffy_clyro/puzzle/saturday_superhouse')
def saturday():
  return render_template('saturday.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)
