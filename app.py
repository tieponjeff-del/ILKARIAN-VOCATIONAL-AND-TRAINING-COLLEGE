from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ILKARIAN VOCATIONAL AND TRAINING COLLEGE - Narok County</title>
<style>
body{margin:0;font-family:Arial,sans-serif;background:#f5f7fb;color:#222;}
.header{background:#0d2a54;color:white;padding:50px 20px;text-align:center;}
.header h1{margin:0;font-size:33px;letter-spacing:1px;}
.header p{font-size:18px;color:#ffeb3b;margin-top:10px;}
.badge{background:#ff9800;color:white;padding:8px 20px;border-radius:25px;font-weight:bold;display:inline-block;margin-top:15px;}
.section{background:white;margin:18px;border-radius:12px;padding:22px;box-shadow:0 2px 8px rgba(0,0,0,0.08);}
h3{color:#0d2a54;border-left:5px solid #ff9800;padding-left:12px;font-size:20px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;}
.card{border:1px solid #e0e0e0;border-radius:10px;padding:14px;background:#fcfdff;}
.card b{color:#0d2a54;}
.card span{font-size:11px;background:#e3f2fd;color:#0d2a54;padding:3px 8px;border-radius:10px;display:inline-block;margin-top:4px;}
table{width:100%;border-collapse:collapse;margin-top:12px;}
th,td{border:1px solid #ccc;padding:10px;text-align:left;font-size:14px;}
th{background:#0d2a54;color:white;}
.footer{background:#0d2a54;color:white;text-align:center;padding:25px;line-height:1.6;}
.highlight-link{display:inline-block;background:yellow;color:red;border:3px solid red;padding:12px 25px;font-weight:bold;text-decoration:none;border-radius:10px;margin:15px 0;animation:blink 1.2s infinite;}
@keyframes blink{50%{background:white;}}
</style>
</head>
<body>

<div class="header">
<h1>ILKARIAN VOCATIONAL AND TRAINING COLLEGE</h1>
<p>Ilkarian, Lolgorian - Trans Mara West, Narok County | TVETA Registered</p>
<div class="badge">JANUARY / MAY / SEPTEMBER INTAKE ONGOING</div>
<p style="margin-top:15px;color:white;">P.O BOX 45, Lolgorian | Skills for Employment & Self-Reliance</p>
</div>

<div class="section">
<h3>About The College</h3>
<p><b>ILKARIAN VOCATIONAL AND TRAINING COLLEGE</b> is a public TVET institution located at Ilkarian near Lolgorian in Narok County. We are fully registered by TVETA under Ministry of Education. We offer KNEC, NITA and TVET CDACC examined Diploma, Certificate and Artisan courses.</p>
<p><b>Motto:</b> Skills, Innovation and Integrity | <b>Exam Bodies:</b> KNEC, NITA, CDACC</p>
</div>

<div class="section">
<h3>🎓 DIPLOMA COURSES (Level 6) - 2 to 3 Years</h3>
<p><b>Entry:</b> KCSE C- and above / Pass in Certificate</p>
<div class="grid">
<div class="card"><b>Diploma in Electrical & Electronics Engineering</b><br><span>Power / Telecom</span></div>
<div class="card"><b>Diploma in Building Technology</b></div>
<div class="card"><b>Diploma in Civil Engineering</b></div>
<div class="card"><b>Diploma in Plumbing Technology</b></div>
<div class="card"><b>Diploma in Automotive Engineering</b></div>
<div class="card"><b>Diploma in Mechanical Engineering</b></div>
<div class="card"><b>Diploma in Welding and Fabrication</b></div>
<div class="card"><b>Diploma in Fashion Design and Garment Making</b></div>
<div class="card"><b>Diploma in Food and Beverage Management</b></div>
<div class="card"><b>Diploma in Hairdressing and Beauty Therapy</b></div>
<div class="card"><b>Diploma in ICT</b></div>
<div class="card"><b>Diploma in Business Management</b></div>
<div class="card"><b>Diploma in Supply Chain / HR</b></div>
<div class="card"><b>Diploma in General Agriculture</b></div>
</div>
</div>

<div class="section">
<h3>📜 CERTIFICATE COURSES (Level 5) - 1 to 2 Years</h3>
<p><b>Entry:</b> KCSE D Plain and above</p>
<table>
<tr><th>Course Name</th><th>Exam Body</th><th>Duration</th></tr>
<tr><td>Certificate in Electrical Installation / Engineering</td><td>KNEC / NITA</td><td>2 Years</td></tr>
<tr><td>Certificate in Building Technology / Masonry / Carpentry</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Plumbing</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Motor Vehicle Mechanics</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Welding and Fabrication</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Fashion Design & Tailoring</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Hairdressing & Beauty Therapy</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Food & Beverage / Catering</td><td>KNEC</td><td>2 Years</td></tr>
<tr><td>Certificate in ICT</td><td>KNEC</td><td>1 Year</td></tr>
<tr><td>Certificate in Business Management</td><td>KNEC</td><td>1 Year</td></tr>
</table>
</div>

<div class="section">
<h3>🔧 ARTISAN & GRADE TEST - 3 to 9 Months</h3>
<div class="grid">
<div class="card">Artisan in Electrical Grade III, II, I</div>
<div class="card">Artisan in Motor Vehicle Mechanics</div>
<div class="card">Artisan in Building / Masonry / Plumbing</div>
<div class="card">Artisan in Carpentry / Welding</div>
<div class="card">Artisan in Garment Making</div>
<div class="card">Artisan in Hairdressing & Beauty</div>
<div class="card">Artisan in Food & Beverage</div>
</div>
</div>

<div class="section" style="text-align:center;background:#fffde7;border:2px dashed #ff9800;">
<h3 style="border:none;text-align:center;">🏫 OUR SISTER INSTITUTIONS</h3>
<p><b>Lolgorian Vocational and Training College & Olkiloriti Senior School</b></p>
<a href="https://olkiloriti-school-8.onrender.com" target="_blank" class="highlight-link">CLICK TO OPEN OLKILORITI SENIOR SCHOOL</a>
<p style="font-size:13px;">Also visit Lolgorian VTC</p>
</div>

<div class="footer">
<p><b>ILKARIAN VOCATIONAL AND TRAINING COLLEGE</b></p>
<p>Location: Ilkarian, Lolgorian, Trans Mara West, Narok County</p>
<p>TVETA Registered | Ministry Approved | KNEC & NITA Centre</p>
<p>© 2026 Ilkarian Vocational and Training College</p>
</div>

</body>
</html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
