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
<title>Lolgorian Technical & Vocational College | Narok County</title>
<style>
body{margin:0;font-family:Arial,sans-serif;background:#f2f6fc;color:#222;}
.top{background:#002366;color:white;padding:8px;text-align:center;font-size:14px;}
.header{background:linear-gradient(#0d47a1,#1976d2);color:white;padding:40px 20px;text-align:center;}
.header h1{margin:0;font-size:30px;line-height:1.2;}
.header h2{margin:10px 0;font-weight:normal;font-size:18px;color:#ffeb3b;}
.badge{background:white;color:#0d47a1;padding:5px 15px;border-radius:20px;font-weight:bold;display:inline-block;margin-top:10px;}
.nav{display:flex;flex-wrap:wrap;justify-content:center;background:white;box-shadow:0 2px 4px #0002;position:sticky;top:0;z-index:10;}
.nav a{padding:12px 18px;text-decoration:none;color:#0d47a1;font-weight:bold;}
.section{background:white;margin:15px;border-radius:12px;padding:20px;box-shadow:0 2px 8px #0001;}
h3{color:#0d47a1;border-bottom:3px solid #ff9800;display:inline-block;padding-bottom:5px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:15px;}
.card{border:1px solid #ddd;border-radius:10px;padding:15px;background:#fafcff;}
.card b{color:#002366;}
.btn{display:inline-block;background:#0d47a1;color:white;padding:14px 28px;text-decoration:none;border-radius:8px;font-weight:bold;margin:5px;}
.btn-whatsapp{background:#25D366;}
.btn-call{background:#ff6f00;}
table{width:100%;border-collapse:collapse;margin-top:10px;}
th,td{border:1px solid #ccc;padding:8px;text-align:left;font-size:14px;}
th{background:#0d47a1;color:white;}
.footer{background:#001a4d;color:white;text-align:center;padding:20px;margin-top:20px;}
</style>
</head>
<body>

<div class="top">TVETA Registered | MoE Approved | KNEC & NITA Exam Centre | Code: 2750/0001</div>

<div class="header">
<h1>LOLGORIAN TECHNICAL & VOCATIONAL COLLEGE</h1>
<h2>Skills for Employment & Self Reliance - Lolgorian, Narok County</h2>
<p>P.O BOX 45 - Lolgorian | Email: info@lolgoriantechnical.ac.ke</p>
<span class="badge">JANUARY / MAY / SEPTEMBER INTAKE ONGOING</span><br><br>
<a href="https://wa.me/254712345678?text=Hello%20Lolgorian%20Technical%20College%20I%20want%20to%20apply" class="btn btn-whatsapp">Apply on WhatsApp</a>
<a href="tel:+254712345678" class="btn btn-call">Call Now</a>
</div>

<div class="nav">
<a href="#diploma">Diploma</a>
<a href="#certificate">Certificate</a>
<a href="#artisan">Artisan</a>
<a href="#short">Short Courses</a>
<a href="#contact">Contact</a>
</div>

<div class="section">
<h3>About The College</h3>
<p><b>Lolgorian Technical & Vocational College</b> is a premier TVET institution located in Lolgorian, Trans Mara West, Narok County. We train youth in market-driven technical skills with modern workshops, industrial attachment and job linkages.</p>
<p><b>Our Mission:</b> To provide quality technical training for industrial growth.</p>
</div>

<div class="section" id="diploma">
<h3>🎓 DIPLOMA COURSES (2-3 Years) - KNEC - C- & Above / Certificate Pass</h3>
<div class="grid">
<div class="card"><b>1. Diploma in Electrical & Electronics Engineering (Power Option)</b><br>Modules I, II, III</div>
<div class="card"><b>2. Diploma in Building Technology</b><br>Construction & Management</div>
<div class="card"><b>3. Diploma in Civil Engineering</b></div>
<div class="card"><b>4. Diploma in Plumbing & Water Technology</b></div>
<div class="card"><b>5. Diploma in Automotive Engineering</b><br>Motor Vehicle Mechanics</div>
<div class="card"><b>6. Diploma in Fashion Design & Garment Making</b></div>
<div class="card"><b>7. Diploma in Hairdressing & Beauty Therapy (Cosmetology)</b></div>
<div class="card"><b>8. Diploma in Food & Beverage (Catering)</b><br>Production & Service</div>
<div class="card"><b>9. Diploma in ICT (Information Communication Technology)</b></div>
<div class="card"><b>10. Diploma in Business Management</b></div>
<div class="card"><b>11. Diploma in Supply Chain Management</b></div>
<div class="card"><b>12. Diploma in Human Resource Management</b></div>
<div class="card"><b>13. Diploma in Agricultural Engineering</b></div>
<div class="card"><b>14. Diploma in Welding & Fabrication</b></div>
</div>
</div>

<div class="section" id="certificate">
<h3>📜 CERTIFICATE COURSES (1-2 Years) - KNEC/NITA - D+ & D Plain</h3>
<table>
<tr><th>Course</th><th>Exam Body</th><th>Duration</th></tr>
<tr><td>Certificate in Electrical Installation (Wireman)</td><td>NITA / KNEC</td><td>1 Year</td></tr>
<tr><td>Certificate in Building Construction Technology</td><td>KNEC</td><td>2 Years</td></tr>
<tr><td>Certificate in Plumbing</td><td>NITA / KNEC</td><td>1 Year</td></tr>
<tr><td>Certificate in Masonry</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Carpentry & Joinery</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Motor Vehicle Mechanics</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Welding & Metal Fabrication</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Fashion Design & Tailoring</td><td>NITA</td><td>1 Year</td></tr>
<tr><td>Certificate in Hairdressing & Beauty Therapy</td><td>NITA</td><td>6 Months - 1 Yr</td></tr>
<tr><td>Certificate in Food & Beverage / Catering</td><td>KNEC</td><td>1-2 Years</td></tr>
<tr><td>Certificate in ICT / Computer Packages & Repair</td><td>KNEC</td><td>6 Months - 1 Yr</td></tr>
<tr><td>Certificate in Business Management / Salesmanship</td><td>KNEC</td><td>1 Year</td></tr>
<tr><td>Certificate in General Agriculture</td><td>KNEC</td><td>1 Year</td></tr>
</table>
</div>

<div class="section" id="artisan">
<h3>🔧 ARTISAN / GRADE TEST (3-6 Months) - NITA - KCPE & Open</h3>
<p>For Class 8 leavers. You get Grade III, II, I certificate to start job or own business.</p>
<div class="grid">
<div class="card">Artisan in Electrical Installation</div>
<div class="card">Artisan in Motor Vehicle Mechanics</div>
<div class="card">Artisan in Tailoring / Dressmaking</div>
<div class="card">Artisan in Hairdressing (Salon)</div>
<div class="card">Artisan in Plumbing</div>
<div class="card">Artisan in Masonry / Building</div>
<div class="card">Artisan in Welding</div>
<div class="card">Artisan in Carpentry</div>
</div>
</div>

<div class="section" id="short">
<h3>⚡ SHORT COURSES (1 Week - 3 Months) - College Certificate</h3>
<p>Computer Packages, Solar Installation, Biogas, Motorcycle Repair, Cake Baking, Barista, Driving Theory, Entrepreneurship, Beauty (Braiding, Makeup, Nail Tech), CCTV Installation.</p>
<p><b>Fees:</b> From Ksh 3,500 per course. Hostel available Ksh 3,000/month.</p>
</div>

<div class="section" id="contact" style="text-align:center;">
<h3>📞 ADMISSION & CONTACT</h3>
<p><b>College Location:</b> Lolgorian Town, Narok County - Opposite Ilkarian Market, Near Olkiloriti</p>
<p><b>Call / WhatsApp:</b> 0712 345 678 / 0745 678 901</p>
<p><b>Email:</b> admission@lolgoriantechnical.ac.ke</p>
<p><b>Requirements:</b> KCPE/KCSE result slip, Copy of ID/Birth Cert, 2 Passports</p>
<br>
<a href="https://wa.me/254712345678?text=Jambo%2C%20naomba%20admission%20letter%20for%20Lolgorian%20Technical%20College" class="btn btn-whatsapp">💬 APPLY ON WHATSAPP NOW</a>
<br><br>
<iframe src="https://www.google.com/maps?q=Olkiloriti,Lolgorian&z=14&output=embed" width="100%" height="200" style="border:0;border-radius:10px;"></iframe>
</div>

<div class="footer">
<p><b>LOLGORIAN TECHNICAL & VOCATIONAL COLLEGE</b></p>
<p>Approved by TVETA & Ministry of Education | ISO Certified Training</p>
<p>© 2026 | Built by Jeff Web Solutions, Lolgorian | Sister: <a href="https://olkiloriti-school-8.onrender.com" style="color:yellow;">Olkiloriti Senior School</a></p>
</div>

</body>
</html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
