import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ilkarian Vocational and Training College | Trans Mara South | Narok</title>
<meta name="description" content="Ilkarian Vocational and Training College is a leading TVET institution in Ilkarian, Trans Mara South, Narok County. Offering Electrical, Building, Fashion, ICT, Beauty and more.">
<meta name="keywords" content="Ilkarian VTC, Ilkarian College, Vocational College Trans Mara South, TVET Narok, Ilkarian Training College, Trans Mara South Colleges">
<meta name="author" content="Ilkarian Vocational and Training College">
<meta name="google-site-verification" content="paste-your-google-code-here-later">

<!-- For Google to show you -->
<meta property="og:title" content="Ilkarian Vocational and Training College - Trans Mara South">
<meta property="og:description" content="Empowering Skills for Self Reliance - Located in Ilkarian, Trans Mara South, Narok County">
<meta property="og:type" content="school">

<style>
body { font-family: Arial, sans-serif; margin:0; background:#f4f6f9; }
.header { background:#0d2a54; color:white; padding:30px; text-align:center; }
.header h1 { margin:0; font-size:28px; }
.header p { margin:5px; font-size:16px; color:#ffcc00; }
.container { padding:20px; max-width:900px; margin:auto; }
.card { background:white; padding:20px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); margin-bottom:20px; }
h2 { color:#0d2a54; border-bottom:2px solid #ffcc00; padding-bottom:10px; }
ul { line-height:1.8; }
.footer { background:#0d2a54; color:white; text-align:center; padding:15px; margin-top:20px; }
.btn { background:#0d2a54; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; }
</style>
</head>
<body>
<div class="header">
<h1>ILKARIAN VOCATIONAL AND TRAINING COLLEGE</h1>
<p>Empowering Skills for Self Reliance</p>
<p>📍 Ilkarian, TRANS MARA SOUTH, Narok County, Kenya - TVET Institution</p>
</div>
<div class="container">
<div class="card">
<h2>Welcome to Ilkarian VTC - Trans Mara South</h2>
<p>Ilkarian Vocational and Training College is a premier TVET institution located in <b>Ilkarian Centre, Trans Mara South Sub-County, Narok County</b>. We are committed to providing quality technical and vocational education to the youth of Trans Mara South and beyond.</p>
</div>
<div class="card">
<h2>Our Courses in Trans Mara South</h2>
<ul>
<li>Electrical Installation - Trans Mara South</li>
<li>Building & Construction</li>
<li>Fashion Design & Garment Making</li>
<li>Hair Dressing & Beauty Therapy</li>
<li>ICT & Computer Packages</li>
<li>Motor Vehicle Mechanics</li>
<li>Plumbing</li>
<li>Carpentry and Joinery</li>
</ul>
</div>
<div class="card">
<h2>Contact - Ilkarian VTC Trans Mara South</h2>
<p><b>Location:</b> Ilkarian Centre, Trans Mara South, Narok County</p>
<p><b>Email:</b> ilkarianvtc@gmail.com</p>
</div>
</div>
<div class="footer">
<p>&copy; 2026 Ilkarian Vocational and Training College - Trans Mara South, Narok | TVET College in Trans Mara South</p>
</div>
</body>
</html>
    """

@app.route('/sitemap.xml')
def sitemap():
    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://ilkarian-vocational-and-training-college.onrender.com/</loc></url>
</urlset>""", 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
