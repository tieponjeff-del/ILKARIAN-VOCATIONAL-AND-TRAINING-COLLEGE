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
<title>ILKARIAN VOCATIONAL AND TRAINING COLLEGE</title>
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
<p>📍 Ilkarian, TRANS MARA SOUTH, Narok County, Kenya</p>
</div>

<div class="container">
<div class="card">
<h2>Welcome to Ilkarian VTC</h2>
<p>Ilkarian Vocational and Training College is a premier TVET institution located in <b>Ilkarian Centre, Trans Mara South Sub-County, Narok County</b>. We are committed to providing quality technical and vocational education to the youth of Trans Mara South and beyond.</p>
<p><b>Motto:</b> Skills for Self Reliance</p>
</div>

<div class="card">
<h2>Our Courses</h2>
<ul>
<li>Electrical Installation</li>
<li>Building & Construction / Masonry</li>
<li>Fashion Design & Garment Making</li>
<li>Hair Dressing & Beauty Therapy</li>
<li>ICT & Computer Packages</li>
<li>Motor Vehicle Mechanics</li>
<li>Plumbing</li>
<li>Carpentry and Joinery</li>
</ul>
</div>

<div class="card">
<h2>Contact Us</h2>
<p><b>Location:</b> Ilkarian Centre, Trans Mara South, Narok County</p>
<p><b>Sub-County:</b> Trans Mara South (Not West)</p>
<p><b>County:</b> Narok County, Kenya</p>
<p><b>Email:</b> ilkarianvtc@gmail.com</p>
<p><b>Phone:</b> 0700 000 000</p>
<a class="btn" href="#">Apply Now</a>
</div>
</div>

<div class="footer">
<p>&copy; 2026 Ilkarian Vocational and Training College - Trans Mara South | All Rights Reserved</p>
</div>
</body>
</html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
